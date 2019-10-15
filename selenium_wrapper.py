import os
import platform

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

    def get_driver(self):
        return self.driver
