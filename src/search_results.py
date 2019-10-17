import os

import pandas as pd

from settings.single_entity import activity_columns, components_columns, historical_name_columns, \
    historical_social_capital_columns, generic_data_columns


class SearchResults:

    def __init__(self, output_folder):
        self.output_folder = output_folder

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

    def _single_export(self, file_path, data):
        if os.path.isfile(file_path):
            with open(file_path, "a") as file:
                data.to_csv(file, header=False, index=False)
        else:
            data.to_csv(file_path, index=False)