__author__ = "Roger Bosch Mateo"

import os
import platform
import time
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumWrapper:
    """
    Wrapper for Selenium that simplifies the set-up
    """

    def __init__(self, options=None):
        """
        Selenium wrapper constructor
        :param options: options for running selenium (ex: running in headless mode)
        """
        chrome_options = Options()
        if options is not None:
            for option in options:
                chrome_options.add_argument(option)

        # Start the Chrome driver
        self.driver = webdriver.Chrome(self._get_driver_path(), chrome_options=chrome_options)

        self.latest_response_delay = None
        self.latest_request_time = None
        self.ua = UserAgent()

    @staticmethod
    def _get_driver_path():
        """
        Method that automatically returns the path to the proper
        chrome driver depending on the OS.
        :return: returns the absolute path to the proper chrome driver
        """
        directory = os.path.dirname(os.path.abspath(__file__))

        operating_system = platform.system()
        if operating_system == "Linux":
            file = "chromedriver_linux"
        elif operating_system == "Darwin":
            file = "chromedriver_mac"
        elif operating_system == "Windows":
            file = "chromedriver_win.exe"
        else:
            raise Exception("Can't identify the current OS with an available driver.")

        return directory + "/drivers/" + file

    def get(self, url):
        """
        Method that calls the driver "get" to obtain a website. It acts as
        a centralized point to avoid doing too many requests in a small period
        of time. Adds user-agent spoofing.
        :param url: url of the desired website to obtain
        """
        if self.latest_response_delay is None:
            self._get(url)
        else:
            # TODO: Change 0 for 10
            while time.time() - self.latest_request_time < 0*self.latest_response_delay:
                time.sleep(0.1)
            self._get(url)

    def _get(self, url):
        # Randomize the user-agent header
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": self.ua.random})

        start = time.time()
        self.driver.get(url)
        self.latest_response_delay = time.time() - start
        self.latest_request_time = time.time()

    def find_element_by_xpath(self, path):
        return self.driver.find_element_by_xpath(path)

    def find_element_by_css_selector(self, path):
        return self.driver.find_element_by_css_selector(path)

    def find_elements_by_xpath(self, path):
        return self.driver.find_elements_by_xpath(path)