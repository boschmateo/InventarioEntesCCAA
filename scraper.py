__author__ = "Roger Bosch Mateo"

"""
Main script that calls the scraper with the desired parameters
"""

import argparse

from settings.settings import web_map
from src.Inventario_entes_CCAA_scrapper import InventarioEntesCCAAScrapper

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


parser.add_argument("--headless",
                    action="store_true",
                    help="Start the web browser as headless. This means that no graphical interface "
                         "will be shown during scraping"
                    )
args = parser.parse_args()

# Check autonomous community values
if args.community is not None:

    communities_not_found = []
    count = 0
    for desired_community in args.community:
        if desired_community not in web_map:
            communities_not_found.append(desired_community)
            count += 1

    if len(communities_not_found) != 0:
        parser.error(
            "{0} autonomous communities that can't be identified: {1}.".format(count, ", ".join(communities_not_found)))

InventarioEntesCCAAScrapper(version=args.version, communities=args.community, headless=args.headless)