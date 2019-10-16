import platform

from selenium_wrapper import SeleniumWrapper
from src.searcher import Searcher


class InventarioEntesCCAAScrapper:

    def __init__(self, headless=True):
        # Start the Chrome driver
        self.driver = self._start_chrome_driver(headless=headless)

        Searcher(self.driver, region="Andalucía")

    def _start_chrome_driver(self, headless=True):
        driver_path = "/Users/ru/Documents/Google Drive/REPUBLIQUEMpuntCAT/test_scrapping/chromedriver_mac"
        if headless:
            options = ["--headless"]
        else:
            options = None

        return SeleniumWrapper(options).get_driver()