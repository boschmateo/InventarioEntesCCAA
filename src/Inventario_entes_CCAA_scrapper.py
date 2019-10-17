import os

from datetime import datetime

from selenium_wrapper import SeleniumWrapper
from settings.settings import web_map
from src.searcher import Searcher


class InventarioEntesCCAAScrapper:

    def __init__(self, version, communities, headless):

        # Start the Chrome driver
        self.driver = self._start_chrome_driver(headless=headless)

        self.output_folder = self._setup_export_folder()

        if version is None:
            version = ""

        # If no communities are specified do the search of all the autonomous communities
        if communities is None:
            for community in web_map.keys():
                self._do_search(version, community)
        # Do search in the specified communities
        else:
            for community in communities:
                self._do_search(version, community)

    def _do_search(self, version, community):
        Searcher(self.driver, self.output_folder, version=version, community=community)

    def _start_chrome_driver(self, headless=True):
        if headless:
            options = ["--headless"]
        else:
            options = None

        return SeleniumWrapper(options).get_driver()

    def _setup_export_folder(self):
        main_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_directory = main_directory + "/output/"

        folder_name = datetime.now().strftime("output_%m-%d-%Y_%H-%M-%S")

        output_folder = output_directory + folder_name

        os.mkdir(output_folder)

        return output_folder