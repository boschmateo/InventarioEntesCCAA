from selenium.webdriver.support.select import Select
import time

from src.settings import show_versions, options_versions, submit_versions, web_map, go_to_search

from selenium.common.exceptions import NoSuchElementException


class CCAASelector:

    BASE_URL = "https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PubInvCCAA/secciones/FrmSelComunidad.aspx"

    def __init__(self, driver, version="", region=None):
        self.driver = driver
        self.version = version
        self.region = region

        self.driver.get(self.BASE_URL)

        self.select_proper_version()
        self.select_proper_region()
        search = 

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
