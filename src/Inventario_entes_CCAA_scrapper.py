from selenium_wrapper import SeleniumWrapper
from settings.settings import web_map
from src.searcher import Searcher


class InventarioEntesCCAAScrapper:

    def __init__(self, version, communities, headless):

        # Start the Chrome driver
        self.driver = self._start_chrome_driver(headless=headless)

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
        Searcher(self.driver, version=version, community=community)

    def _start_chrome_driver(self, headless=True):
        if headless:
            options = ["--headless"]
        else:
            options = None

        return SeleniumWrapper(options).get_driver()