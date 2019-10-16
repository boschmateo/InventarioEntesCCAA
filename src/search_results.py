import os

import pandas as pd

from settings.single_entity import activity_values, components_values, historical_name_values, \
    historical_social_capital_values


class SearchResults:

    def __init__(self):
        self.generic_data_columns = ["version", "comunidad", "codigo_ente", "tipo_ente", "accionista_mayoritario",
                                     "nombre", "cif", "capital_social", "finalidad", "regimen_contable",
                                     "regimen_presupuestario", "sector_admin_publica", "fuente_alta", "alta_desde",
                                     "ente_proviene", "direccion", "localidad", "codigo_postal", "provincia",
                                     "telefono", "fax", "sitio_web", "email"]
        self.generic_data = pd.DataFrame(columns=self.generic_data_columns)
        self.actvity_data = pd.DataFrame(columns=activity_values)
        self.components_data = pd.DataFrame(columns=components_values)
        self.historical_names_data = pd.DataFrame(columns=historical_name_values)
        self.historical_social_capital_data = pd.DataFrame(columns=historical_social_capital_values)

    def add_generic_data(self, values):
        self.generic_data = pd.DataFrame(values, columns=self.generic_data_columns)
        print(self.generic_data.head(n=15))

    def export(self):
        # TODO: This should work with the four different outputs
        main_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_directory = main_directory + "/output/"
        output_file = output_directory + "test.csv"

        if os.path.isfile(output_file):
            with open(output_file, "a") as file:
                self.generic_data.to_csv(file, header=False)
        else:
            self.generic_data.to_csv(output_directory + "test.csv")