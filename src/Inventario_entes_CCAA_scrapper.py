from selenium.common.exceptions import NoSuchElementException

__author__ = "Roger Bosch Mateo"

import os

from datetime import datetime
from random import shuffle

from selenium_wrapper import SeleniumWrapper
from settings.settings import web_map, province_codes_name
from settings.search import entity_types
from src.searcher import Searcher


class InventarioEntesCCAAScraper:
    """
    Class that receives the desired search by the user and performs it.
    """

    def __init__(self, version, communities, province, entity_types, name, cif, headless):
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

        self.searches = self.find_all_necessary_searches(version, communities, province, entity_types, name, cif)
        print("----------------")
        for search in self.searches:
            print(str(search) + "\n")
        print("-------------------")

        # Randomize the search so it is different every single time
        shuffle(self.searches)

        for search in self.searches:
            while True:
                try:
                    Searcher(self.driver, self.output_folder, search)
                    break
                except NoSuchElementException:
                    print("HEY I BROKE DOWN")


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
        os.mkdir(output_folder + "/img")


        return output_folder

    def find_all_necessary_searches(self, version, communities, province, entity_types, name, cif):
        version = self._version_search(version)
        communities = self._communities_search(communities, province)
        entity_types = self._entity_types_search(entity_types)

        searches_to_do = []
        for community, province_codes in communities.items():
            # This means that a search for the WHOLE community must be done
            if len(province_codes) == 0:
                # This means that no specific entity should be searched
                if len(entity_types) == 0:
                    searches_to_do.append({
                        "version": version,
                        "community": community,
                        "province": None,
                        "entity_type": None,
                        "name": name,
                        "cif": cif
                    })
                # Add a search for each different entity type
                else:
                    for entity_type in entity_types:
                        searches_to_do.append({
                            "version": version,
                            "community": community,
                            "province": None,
                            "entity_type": entity_type,
                            "name": name,
                            "cif": cif
                        })
            # This means that a search for a specific province inside a community must be done
            else:
                # NO specific entity type but specific province code
                if len(entity_types) == 0:
                    for province_code in province_codes:
                        searches_to_do.append({
                            "version": version,
                            "community": community,
                            "province": province_code,
                            "entity_type": None,
                            "name": name,
                            "cif": cif
                        })
                # Specific entity type and specific province
                else:
                    for entity_type in entity_types:
                        for province_code in province_codes:
                            searches_to_do.append({
                                "version": version,
                                "community": community,
                                "province": province_code,
                                "entity_type": entity_type,
                                "name": name,
                                "cif": cif
                            })

        return searches_to_do

    @staticmethod
    def _version_search(version):
        if version is None:
            return ""
        return version

    @staticmethod
    def _communities_search(communities, provinces):
        found_provinces = {}

        if provinces is None:

            communities = InventarioEntesCCAAScraper._get_communities(communities)

            # Add those communities that are not present with the province data
            for community in communities:
                found_provinces[community] = []

        else:
            # For each of the desired provinces to search
            for province in provinces:

                # Find the community that corresponds to the province
                for community, values in web_map.items():
                    if province in values[province_codes_name]:
                        if community not in found_provinces:
                            found_provinces[community] = []
                        # Add the province
                        found_provinces[community].append(values[province_codes_name][province])

            if communities is not None:
                for community in communities:
                    if community not in found_provinces:
                        found_provinces[community] = []

        return found_provinces

    @staticmethod
    def _get_communities(communities):
        # If no communities are specified, a search of all communities must be done
        if communities is None:
            return web_map.keys()
        # If communities are specified, stick to what the user wants
        else:
            return communities

    @staticmethod
    def _entity_types_search(types):
        if types is None:
            return []

        found_entities = []
        for type in types:
            found_entities += entity_types[type]

        return found_entities

    @staticmethod
    def _province_search(provinces):
        if provinces is None:
            return {}

        found_provinces = {}
        # For each of the desired provinces to search
        for province in provinces:

            # Find the community that corresponds to the province
            for community, values in web_map.items():
                if province in values[province_codes_name]:
                    if community not in found_provinces:
                        found_provinces[community] = []
                    # Add the province
                    found_provinces[community].append(values[province_codes_name][province])
        return found_provinces
