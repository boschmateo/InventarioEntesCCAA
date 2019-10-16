from selenium.webdriver.support.select import Select

from src.entityscrapper import EntityScraper
from settings.settings import web_map
from settings.versions import show_versions, options_versions, submit_versions
from settings.single_entity import show_all_data
from settings.search import go_to_search, submit_search, results_table_path

from selenium.common.exceptions import NoSuchElementException


class Searcher:

    BASE_URL = "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PubInvCCAA/secciones/FrmSelComunidad.aspx"

    def __init__(self, driver, version="", region=None):
        self.driver = driver
        self.version = version
        self.region = region

        self.driver.get(self.BASE_URL)

        self.select_proper_version()
        self.select_proper_region()
        self.fill_search_parameters()
        self.scrap_results()

        input("sffds")

    def select_proper_version(self):
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
        region = self.driver.find_element_by_css_selector(web_map[self.region])
        region.click()

        search = self.driver.find_element_by_css_selector(go_to_search)
        search.click()

    def fill_search_parameters(self):
        # TODO: Include all the available parameters to search

        search_button = self.driver.find_element_by_xpath(submit_search)
        search_button.click()

    def scrap_results(self):
        table = self.driver.find_element_by_xpath(results_table_path)

        found_links = []
        for row in table.find_elements_by_xpath(".//tr"):
            elements = row.find_elements_by_xpath(".//td")
            # If this row is not empty
            if len(elements) != 0:
                entity_link = elements[0].find_element_by_xpath(".//a").get_attribute("href")
                found_links.append(entity_link)

        for link in found_links:
            self._scrap_single_entity(link)

    def _scrap_single_entity(self, link):
        # Click to show the info of a specific entity
        self.driver.get(link)

        # Show all data from this entity
        all_data_link = self.driver.find_element_by_xpath(show_all_data)
        all_data_link.click()

        entity = EntityScraper(self.driver)

        return entity.get_data()