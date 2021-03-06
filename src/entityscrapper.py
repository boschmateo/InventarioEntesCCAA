__author__ = "Roger Bosch Mateo"

from selenium.common.exceptions import NoSuchElementException

import settings.single_entity as se


class EntityScraper:
    
    def __init__(self, driver, version, region):
        self.driver = driver
        self.version = version
        self.region = region

        self.generic_data = self.extract_generic_data()
        self.activity_data = self.extract_activities_data()
        self.component_data = self.extract_components_data()
        self.historical_name_data = self.extract_historical_name_data()
        self.historical_social_capital_data = self.extract_historical_social_capital_data()

    def extract_generic_data(self):
        generic_data = {}
        generic_data["version"] = self.version
        generic_data["comunidad"] = self.region

        generic_data["codigo_ente"] = self._get_value_from_xpath(se.codigo_ente)
        if generic_data["codigo_ente"] is None:
            generic_data = self.alternative_generic_data_extractor(generic_data)
        else:
            generic_data["tipo_ente"] = self._get_value_from_xpath(se.tipo_ente)
            generic_data["accionista_mayoritario"] = self._get_value_from_xpath(se.accionista_mayoritario)
            generic_data["nombre"] = self._get_value_from_xpath(se.nombre)
            generic_data["cif"] = self._get_value_from_xpath(se.cif)
            generic_data["capital_social"] = self._get_value_from_xpath(se.capital_social)
            generic_data["finalidad"] = self._get_value_from_xpath(se.finalidad)
            generic_data["regimen_contable"] = self._get_value_from_xpath(se.regimen_contable)
            generic_data["regimen_presupuestario"] = self._get_value_from_xpath(se.regimen_presupuestario)
            generic_data["sector_admin_publica"] = self._get_value_from_xpath(se.sector_admin_publica)

            alta1 = self._get_value_from_xpath(se.fuente_alta_1)
            alta2 = self._get_value_from_xpath(se.fuente_alta_2)
            if alta1 is not None or alta2 is not None:
                if alta1 is None:
                    alta1 = ""
                if alta2 is None:
                    alta2 = ""
                alta = alta1 + " " + alta2
            else:
                alta = None
            generic_data["fuente_alta"] = alta

            generic_data["alta_desde"] = self._get_value_from_xpath(se.alta_desde)
            generic_data["ente_proviene"] = self._get_value_from_xpath(se.ente_proviene)

        generic_data["direccion"] = self._get_value_from_xpath(se.direccion)
        generic_data["localidad"] = self._get_value_from_xpath(se.localidad)
        generic_data["codigo_postal"] = self._get_value_from_xpath(se.codigo_postal)
        generic_data["provincia"] = self._get_value_from_xpath(se.provincia)
        generic_data["telefono"] = self._get_value_from_xpath(se.telefono)
        generic_data["fax"] = self._get_value_from_xpath(se.fax)
        generic_data["sitio_web"] = self._get_value_from_xpath(se.sitio_web)
        generic_data["email"] = self._get_value_from_xpath(se.email)

        return generic_data

    def alternative_generic_data_extractor(self, generic_data):
        generic_data["codigo_ente"] = self._get_value_from_xpath(se.codigo_ente_alt)
        generic_data["tipo_ente"] = self._get_value_from_xpath(se.tipo_ente_alt)
        generic_data["accionista_mayoritario"] = None
        generic_data["nombre"] = self._get_value_from_xpath(se.nombre_alt)
        generic_data["cif"] = self._get_value_from_xpath(se.cif_alt)
        generic_data["capital_social"] = self._get_value_from_xpath(se.capital_social_alt)
        generic_data["finalidad"] = self._get_value_from_xpath(se.finalidad_alt)
        generic_data["regimen_contable"] = self._get_value_from_xpath(se.regimen_contable_alt)
        generic_data["regimen_presupuestario"] = self._get_value_from_xpath(se.regimen_presupuestario_alt)
        generic_data["sector_admin_publica"] = self._get_value_from_xpath(se.sector_admin_publica_alt)

        alta1 = self._get_value_from_xpath(se.fuente_alta_1_alt)
        alta2 = self._get_value_from_xpath(se.fuente_alta_2_alt)
        if alta1 is not None or alta2 is not None:
            if alta1 is None:
                alta1 = ""
            if alta2 is None:
                alta2 = ""
            alta = alta1 + " " + alta2
        else:
            alta = None
        generic_data["fuente_alta"] = alta

        generic_data["alta_desde"] = self._get_value_from_xpath(se.alta_desde_alt)
        generic_data["ente_proviene"] = self._get_value_from_xpath(se.ente_proviene_alt)

        return generic_data

    def generic_table_extractor(self, x_path, table_headers):
        table = self.driver.find_element_by_xpath(x_path)

        found_activities = []
        for row in table.find_elements_by_xpath(".//tr"):
            elements = row.find_elements_by_xpath(".//td")
            # If this row is not empty
            if len(elements) != 0 and len(elements) >= len(table_headers):
                activity_data = {}
                activity_data["version"] = self.version
                activity_data["codigo_ente"] = self.generic_data["codigo_ente"]
                for i in range(len(table_headers)):
                    col_name = table_headers[i]
                    element = elements[i]
                    activity_data[col_name] = self._get_text_from_table(element)
                    # activity_data[table_headers[i]] = self._get_text_from_table(elements[i])

                found_activities.append(activity_data)

        return found_activities

    def extract_activities_data(self):
        try:
            return self.generic_table_extractor(se.activity_table, se.activity_columns)
        except NoSuchElementException:
            return []

    def extract_components_data(self):
        # TODO: Extract alternative components table
        try:
            return self.generic_table_extractor(se.components_table, se.components_columns)
        except NoSuchElementException:
            return self.extract_alt_components()

    def extract_alt_components(self):
        try:
            return [{
                "version": self.version,
                "codigo_ente": self.generic_data["codigo_ente"],
                "total_miembros_patronado": self._get_value_from_xpath(se.components_total),
                "n_patronos_designados_cccaa_o_unidades_dependientes": self._get_value_from_xpath(se.components_por_ccaa),
                "n_patronos_designados_adinistraciones_pub": self._get_value_from_xpath(se.components_adm_publicas),
                "n_patronos_sector_privado": self._get_value_from_xpath(se.components_sector_privado)
            }]
        except NoSuchElementException:
            return []

    def extract_historical_name_data(self):
        try:
            return self.generic_table_extractor(se.historical_name_table, se.historical_name_columns)
        except NoSuchElementException:
            return []

    def extract_historical_social_capital_data(self):
        try:
            return self.generic_table_extractor(se.historical_social_capital_table, se.historical_social_capital_columns)
        except NoSuchElementException:
            return []

    def _get_value_from_xpath(self, path):
        try:
            value = self.driver.find_element_by_xpath(path)
            value = value.get_attribute("value")
            if value == "":
                return None
            else:
                return value
        except Exception:
            print("HEY Something wrong with {0}".format(path))
            return None

    def _get_text_from_table(self, element):
        try:
            text = element.text
            if text == "" or text == " ":
                return None
            else:
                return text
        except Exception:
            print("HEY Something wrong with {0}".format(element))
            return None
