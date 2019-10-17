__author__ = "Roger Bosch Mateo"

import os

from datetime import datetime

from selenium_wrapper import SeleniumWrapper
from settings.settings import web_map
from src.searcher import Searcher


class InventarioEntesCCAAScrapper:
    """
    Class that receives the desired search by the user and performs it.
    """

    def __init__(self, version, communities, headless):
        """
        Constructor that initializes the search desired by the user.
        :param version: String containing the desired historical version
        of the data desired.
        :param communities: List of the names of the autonomous communities
        to extract data from.
        :param headless: Indicates if the scraping should be run with no GUI (True)
        or by default with GUI (False)
        """

        # Start the Chrome driver
        self.driver = self._start_chrome_driver(headless=headless)

        self.output_folder = self._setup_export_folder()

        self.version = self._version_search(version)
        self.communities = self._communities_search(communities)

        for community in communities:
            Searcher(self.driver, self.output_folder, version=version, community=community)

    @staticmethod
    def _start_chrome_driver(headless=True):
        """
        Metohd that starts Selenium with the Chrome driver.
        :param headless: If True no Chrome GUI will be shown, False otherwise
        :return: returns an Instance of the driver
        """
        if headless:
            options = ["--headless"]
        else:
            options = None

        return SeleniumWrapper(options)

    @staticmethod
    def _setup_export_folder():
        main_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_directory = main_directory + "/output/"

        folder_name = datetime.now().strftime("output_%m-%d-%Y_%H-%M-%S")

        output_folder = output_directory + folder_name

        os.mkdir(output_folder)

        return output_folder

    @staticmethod
    def _version_search(version):
        if version is None:
            return ""
        return version

    @staticmethod
    def _communities_search(communities):
        # If no communities are specified, a search of all communities must be done
        if communities is None:
            return web_map.keys()
        # If communities are specified, stick to what the user wants
        else:
            return communities