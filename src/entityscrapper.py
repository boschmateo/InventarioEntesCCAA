import pandas as pd


class EntityScraper:
    
    def __init__(self, driver):
        self.driver = driver
        self.data = None


    def get_data(self):
        return self.data