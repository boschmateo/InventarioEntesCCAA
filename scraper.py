__author__ = "Roger Bosch Mateo"

"""
Main script that calls the scraper with the desired parameters
"""

import argparse

from settings.settings import web_map, province_codes_name
from settings.search import entity_types
from src.Inventario_entes_CCAA_scrapper import InventarioEntesCCAAScraper


def get_missing_parameters(desired_parameters, available_parameters):
    parameters_not_found = []
    for desired_parameter in desired_parameters:
        if desired_parameter not in available_parameters:
            parameters_not_found.append(desired_parameter)

    return parameters_not_found


description = "#TODO: Add description"
parser = argparse.ArgumentParser(description=description)

parser.add_argument("--version",
                    type=str,
                    nargs="?",
                    help="Specify the desired version of the data that wants to be scraped.\n"
                         "Usually two versions are available for each year as 20XX/01 or "
                         "200XX/02 (this information can be obtained from the web page at "
                         "\"Historial de publicaciones\"). If no version is specified or "
                         "found on the website, the latest available will be used. "
                         "Example: To extract historical data from the second half of 2009 "
                         "do --version 2009/02"
                    )

parser.add_argument("--community",
                    type=str,
                    nargs="+",
                    help="Obtain only data from a specific group of autonomous communities. Any "
                         "number of autonomous community can be specified. This are the names "
                         "of tha available autonomous communities: País Vasco, Cataluña, Galicia, "
                         "Andalucía, Principado de Asturias, Cantabria, La Rioja, Región de Murcia, "
                         "Comunitat Valenciana, Aragón, Castilla-La Mancha, Canarias, Navarra, Ceuta, "
                         "Melilla, Castilla y León. If this flag is not specified a search of all "
                         "autonomous communities will be done. "
                         "Example: Search in La Rioja and Canarias do --community \"La Rioja\" \"Canarias\""
                    )

parser.add_argument("--province",
                    type=str,
                    nargs="+",
                    help="TODO"
                    )

parser.add_argument("--type",
                    type=str,
                    nargs="+",
                    help="TODO"
                    )

parser.add_argument("--name",
                    type=str,
                    nargs="?",
                    help="TODO"
                    )

parser.add_argument("--cif",
                    type=str,
                    nargs="?",
                    help="TODO"
                    )

parser.add_argument("--headless",
                    action="store_true",
                    help="Start the web browser as headless. This means that no graphical interface "
                         "will be shown during scraping"
                    )

args = parser.parse_args()

# Check autonomous community values
if args.community is not None:

    communities_not_found = get_missing_parameters(args.community, web_map)
    if len(communities_not_found) != 0:
        parser.error(
            "[--community] {0} autonomous communities that can't be identified: "
            "{1}.".format(len(communities_not_found), ", ".join(communities_not_found)))

if args.province is not None:

    all_provinces = []
    for community in web_map.keys():
        for province in web_map[community][province_codes_name].keys():
            all_provinces.append(province)

    provinces_not_found = get_missing_parameters(args.province, all_provinces)
    if len(provinces_not_found) != 0:
        parser.error(
            "[--province] {0} provinces that can't be identified: "
            "{1}.".format(len(provinces_not_found), ", ".join(provinces_not_found)))

if args.type is not None:

    types_not_found = get_missing_parameters(args.type, entity_types)
    if len(types_not_found) != 0:
        parser.error("[--type] {0} types that can't be identified: "
                     "{1}.".format(len(types_not_found), ", ".join(types_not_found)))

InventarioEntesCCAAScraper(version=args.version, communities=args.community, province=args.province,
                           entity_types=args.type, name=args.name, cif=args.cif, headless=args.headless)


