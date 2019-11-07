import time

import requests

__author__ = "Roger Bosch Mateo"

from selenium.webdriver.support.select import Select
from random import shuffle

from src.entityscrapper import EntityScraper
from settings.settings import web_map, button_path, img_path
from settings.versions import show_versions, options_versions, submit_versions
from settings.single_entity import show_all_data
from settings.search import go_to_search, submit_search, results_table_path, provincia_path, tipo_ente_1_path, \
    tipo_ente_2_path, nombre_path, cif_path, buscar_en_historico_nombres

from selenium.common.exceptions import NoSuchElementException

from src.search_results import SearchResults


class Searcher:
    """
    Class that from the main web page does a search with the desired parameters and extracts
    all the found information.
    This class does only ONE search of a specific autonomous community. Two extract data from
    N different autonomous communities, this class must be instantated N times, one for each community.
    """

    # Base url of the web to scrap
    BASE_URL = "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PubInvCCAA/secciones/FrmSelComunidad.aspx"

    def __init__(self, driver, output_folder, search_parameters):
        """
        Constructor that intializes the search to extract the data
        :param driver: initialized Selenium driver
        :param output_folder: folder where the output .csv files will be dumped
        :param search_parameters: dictionary with all the parameters for the search
        """
        self.driver = driver
        self.search_results = SearchResults(output_folder, search_parameters)

        self.version = search_parameters["version"]
        self.region = search_parameters["community"]
        self.province = search_parameters["province"]
        self.entity_type = search_parameters["entity_type"]
        self.name = search_parameters["name"]
        self.cif = search_parameters["cif"]

        self.do_search()

    def do_search(self):
        """
        Main method that contains the skeleton (different phases)
        to extract the data
        """
        # Call the website
        self.driver.get(self.BASE_URL)

        # Request the proper historical data
        self.select_proper_version()
        self.save_image()

        # If the entity exists in this historical version, extract the data
        if self.select_proper_region() is True:
            # Do the search
            self.fill_search_parameters()
            # Scrap the results page
            self.scrap_results()
            # Export the data to .csv
            self.search_results.export()

    def select_proper_version(self):
        """
        Method that selects the desired historical data version for this search
        """
        try:
            # See if the submit button is displayed
            submit_button = self.driver.find_element_by_xpath(submit_versions)
        except NoSuchElementException:
            # In case it is not shown, make it appear
            self.driver.find_element_by_xpath(show_versions).click()

            # Get the reference to the submit button
            submit_button = self.driver.find_element_by_xpath(submit_versions)

        # Find all options
        select = Select(self.driver.find_element_by_xpath(options_versions))
        found = False
        for option in select.options:
            # In case one matches the desired search select it
            if self.version in option.text:
                select.select_by_value(option.text)
                self.version = option.text
                self.search_results.update_search_parameter("version", self.version)
                found = True
                break

        # If the specified version didn't match an available historical version
        # select by default the newest one
        if not found:
            select.select_by_index(0)
            self.version = select.options[0].text
            print("The desired historical publication was not found. "
                  "Using latest publication: {0}".format(self.version))

        # Send the form
        submit_button.submit()

    def save_image(self):
        """
        Method that saves the image of the desired autonomous community.
        """
        img = self.driver.find_element_by_xpath(web_map[self.region][img_path]).get_attribute("src")
        img = requests.get(img, stream=True)
        self.search_results.export_image(self.region, img)

    def select_proper_region(self):
        """
        Method that selects the desired region for this search from the
        landing page
        :return: returns True if the region exists for this historical data version,
        False otherwise
        """
        # Click the desired region
        region = self.driver.find_element_by_css_selector(web_map[self.region][button_path])
        region.click()
        time.sleep(1)

        try:
            search = self.driver.find_element_by_css_selector(go_to_search)
            search.click()
            time.sleep(1)
            return True
        except NoSuchElementException:
            # This means that the information of this autonomous community is not available
            # at this version
            return False

    def fill_search_parameters(self):
        """
        Method that fills the search form with all the paramters from the search
        """
        time.sleep(1)
        if self.province is not None:
            self.driver.find_element_by_xpath(provincia_path).send_keys(self.province)

        if self.entity_type is not None:
            self.driver.find_element_by_xpath(tipo_ente_1_path).send_keys(self.entity_type[0])
            self.driver.find_element_by_xpath(tipo_ente_2_path).send_keys(self.entity_type[1])

        if self.name is not None:
            self.driver.find_element_by_xpath(nombre_path).send_keys(self.name)
            self.driver.find_element_by_xpath(buscar_en_historico_nombres).click()

        if self.cif is not None:
            self.driver.find_element_by_xpath(cif_path).send_keys(self.cif)

        # Submit the search
        search_button = self.driver.find_element_by_xpath(submit_search)
        search_button.click()

    def scrap_results(self):
        """
        Method called after the results from the search are shown.
        It obtains all the links from the shown entities and extracts
        the data for each one of the links.
        Finally it updates the variable search_result with the scraped data.
        """
        # Find the table
        table = self.driver.find_element_by_xpath(results_table_path)

        found_links = []
        # For each row the table hase
        for row in table.find_elements_by_xpath(".//tr"):
            elements = row.find_elements_by_xpath(".//td")
            # If this row is not empty
            if len(elements) != 0:
                # Extract the link
                entity_link = elements[0].find_element_by_xpath(".//a").get_attribute("href")
                found_links.append(entity_link)

        # Randomize the list of links so each time the order is different.
        shuffle(found_links)

        generic_data_found = []
        activity_data_found = []
        components_data_found = []
        components_alt_data_found = []
        historical_name_data_found = []
        historical_social_capital_data_found = []
        count = 0
        # For each link found
        for link in found_links:
            # Scrap the data from this entity
            gd, act, comp, hist_name, hist_c_s = self._scrap_single_entity(link)

            # Update the found data variables with the new data
            generic_data_found.append(gd)
            activity_data_found += act
            if len(comp) > 0 and "total_miembros_patronado" in comp[0]:
                components_alt_data_found += comp
            else:
                components_data_found += comp
            historical_name_data_found += hist_name
            historical_social_capital_data_found += hist_c_s

            # TODO: Remove this
            if count == 2:
                pass


            count += 1

        # Add data to the centralized search_result variable
        self.search_results.add_generic_data(generic_data_found)
        self.search_results.add_activity_data(activity_data_found)
        self.search_results.add_components_data(components_data_found)
        self.search_results.add_components_alt_data(components_alt_data_found)
        self.search_results.add_historical_names_data(historical_name_data_found)
        self.search_results.add_historical_social_capital_data(historical_social_capital_data_found)

    def _scrap_single_entity(self, link):
        """
        Method that scraps a single entity. It updates the browser with the
        URL of the desired entity, clicks the button to show all the entity
        data at once and leavs everything prepared for EntityScraper to
        obtain the desired information.
        :param link: Link to the desired entity to scrap.
        :return: returns 5 items, each with a list of the extracted data formatted in dict
        (generic data, activities, components and historical name and social capital).
        """
        # Click to show the info of a specific entity
        self.driver.get(link)

        # Show all data from this entity
        all_data_link = self.driver.find_element_by_xpath(show_all_data)
        all_data_link.click()

        entity = EntityScraper(self.driver, self.version, self.region)

        return entity.generic_data, entity.activity_data, entity.component_data, \
               entity.historical_name_data, entity.historical_social_capital_data
