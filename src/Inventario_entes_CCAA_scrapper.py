

class InventarioEntesCCAAScrapper():

    def __init__(self, headless=True):
        # Start the Chrome driver
        self.driver = self._start_chrome_driver(headless=headless)

        # Go to the web to scrap
        self.driver.get("http://www.infosubvenciones.es/bdnstrans/GE/es/concesiones")

    def _start_chrome_driver(self, headless=True):
        driver_path = "/Users/ru/Documents/Google Drive/REPUBLIQUEMpuntCAT/test_scrapping/chromedriver"
        if headless:
            options = ["--headless"]
        else:
            options = None

        return SeleniumWrapper(driver_path, options).get_driver()