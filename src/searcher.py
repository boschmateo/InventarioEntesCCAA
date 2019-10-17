__author__ = "Roger Bosch Mateo"

from selenium.webdriver.support.select import Select

from src.entityscrapper import EntityScraper
from settings.settings import web_map
from settings.versions import show_versions, options_versions, submit_versions
from settings.single_entity import show_all_data
from settings.search import go_to_search, submit_search, results_table_path, entity_not_available

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

    def __init__(self, driver, output_folder, version, community):
        """
        Constructor that intializes the search to extract the data
        :param driver: initialized Selenium driver
        :param output_folder: folder where the output .csv files will be dumped
        :param version: desired historical data to extract
        :param community: name of the autonomous community to extract
        """
        print("Version is {0}\nCommunity is {1}".format(version, community))
        self.driver = driver
        self.version = version
        self.region = community
        self.search_results = SearchResults(output_folder)

    def do_search(self):
        """
        Main method that contains the skeleton (different phases)
        to extract the data
        """
        # Call the website
        self.driver.get(self.BASE_URL)

        # Request the proper historical data
        self.select_proper_version()

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

    def select_proper_region(self):
        """
        Method that selects the desired region for this search from the
        landing page
        :return: returns True if the region exists for this historical data version,
        False otherwise
        """
        # Click the desired region
        region = self.driver.find_element_by_css_selector(web_map[self.region])
        region.click()

        try:
            search = self.driver.find_element_by_css_selector(go_to_search)
            search.click()
            return True
        except NoSuchElementException:
            # This means that the information of this autonomous community is not available
            # at this version
            return False

    def fill_search_parameters(self):
        """
        Method that fills the search form with all the paramters from the search
        """
        # TODO: Include all the available parameters to search

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

        generic_data_found = []
        activity_data_found = []
        components_data_found = []
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
            components_data_found += comp
            historical_name_data_found += hist_name
            historical_social_capital_data_found += hist_c_s

            # TODO: Remove this
            if count == 15:
                break

            count += 1

        # Add data to the centralized search_result variable
        self.search_results.add_generic_data(generic_data_found)
        self.search_results.add_activity_data(activity_data_found)
        self.search_results.add_components_data(components_data_found)
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
