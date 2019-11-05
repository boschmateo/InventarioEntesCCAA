import os

import pandas as pd

from settings.single_entity import activity_columns, components_columns, historical_name_columns, \
    historical_social_capital_columns, generic_data_columns


class SearchResults:

    def __init__(self, output_folder, search_parameters):
        self.output_folder = output_folder
        self.search_parameters = search_parameters

        self.generic_data = None
        self.activity_data = None
        self.components_data = None
        self.historical_names_data = None
        self.historical_social_capital_data = None

    def add_generic_data(self, values):
        self.generic_data = pd.DataFrame(values, columns=generic_data_columns)

    def add_activity_data(self, values):
        # Add two necessary columns to the data t be able to identify the source
        # entity and the current version
        columns = ["version", "codigo_ente"] + activity_columns
        self.activity_data = pd.DataFrame(values, columns=columns)

    def add_components_data(self, values):
        # Add two necessary columns to the data t be able to identify the source
        # entity and the current version
        columns = ["version", "codigo_ente"] + components_columns
        self.components_data = pd.DataFrame(values, columns=columns)

    def add_historical_names_data(self, values):
        # Add two necessary columns to the data t be able to identify the source
        # entity and the current version
        columns = ["version", "codigo_ente"] + historical_name_columns
        self.historical_names_data = pd.DataFrame(values, columns=columns)

    def add_historical_social_capital_data(self, values):
        # Add two necessary columns to the data t be able to identify the source
        # entity and the current version
        columns = ["version", "codigo_ente"] + historical_social_capital_columns
        self.historical_social_capital_data = pd.DataFrame(values, columns=columns)

    def export(self):
        self.add_search_info()

        generic_data_path = self.output_folder + "/generic_data.csv"
        self._single_export(generic_data_path, self.generic_data)

        activity_path = self.output_folder + "/activity_data.csv"
        self._single_export(activity_path, self.activity_data)

        components_path = self.output_folder + "/components_data.csv"
        self._single_export(components_path, self.components_data)

        historical_name_path = self.output_folder + "/historical_name_data.csv"
        self._single_export(historical_name_path, self.historical_names_data)

        historical_social_capital_path = self.output_folder + "/historical_social_capital_data.csv"
        self._single_export(historical_social_capital_path, self.historical_social_capital_data)

    def add_search_info(self):
        if self.search_parameters["province"] is None:
            self.search_parameters["province"] = "All provinces"
        if self.search_parameters["entity_type"] is None:
            self.search_parameters["entity_type"] = "All entities"
        if self.search_parameters["name"] is None:
            self.search_parameters["name"] = "No specific name"
        if self.search_parameters["cif"] is None:
            self.search_parameters["cif"] = "No specific CIF"

        file_path = self.output_folder + "/search_info.txt"
        text = "Search:\n" \
               "\t- Version: {version}\n" \
               "\t- Autonomous community: {community}\n" \
               "\t- Province: {province}\n" \
               "\t- Type: {entity_type}\n" \
               "\t- Name: {name}\n" \
               "\t- CIF: {cif}\n".format(**self.search_parameters)

        if os.path.isfile(file_path):
            with open(file_path, "a") as file:
                file.write(text)
        else:
            with open(file_path, "w") as file:
                file.write(text)

    @staticmethod
    def _single_export(file_path, data):
        if os.path.isfile(file_path):
            with open(file_path, "a") as file:
                data.to_csv(file, header=False, index=False)
        else:
            data.to_csv(file_path, index=False)

    def update_search_parameter(self, key, value):
        self.search_parameters[key] = value

    def export_image(self, community, img_response):
        file_path = self.output_folder + "/img/{community}.png".format(community=community)
        with open(file_path, "wb") as f:
            for chunk in img_response:
                f.write(chunk)
