# Inventory of entities of Autonomous Communities: Scraping the data

This scraper obtains the data from the [Inventory of entities of Autonomous Communities](https://serviciostelematicosext.hacienda.gob.es/SGCIEF/PubInvCCAA/secciones/FrmSelComunidad.aspx). The portal shows aggregated information from the different dependent entities of de sixteen autonomous commuities of Spain.
This README focuses on the usage of the web scraper, but more detailed information regarding the structure of the data or the license amongst other things can be foun in `/pdf/respuestas.pdf`.

## Requirements
This scraper has been tested to be fully compatible with Python 3. The necessary libraries are:

```
pip3 install selenium
pip3 install pandas
pip3 install fake-useragent
```

Alternatively this repo has a virtual environment with all necessary modules. It can be activated by doing:
```
source newenv/bin/activate
```

As of now the scraping is done using Chrome automatized with Selenium. The drivers are already downloaded under the `drivers` folder for Windows, Mac and Linux for version 78. If an older or newer version is needed it can be downloaded from the [official website](https://chromedriver.chromium.org/downloads) and replaced by the existing ones.

## Usage

The portals offers a poor search engine that makes tedious for the user to extract the desired information. This scraper aims to ease this search while allowing to obtain the data in a structured format.

The main file the user needs to call is `scraper.py` that accepts a wide variety of arguments:

* __--version__: Specify the desired version of the data that wants to be scraped. Usually two versions are available for each year as 20XX/01 or 200XX/02 (this information can be obtained from the web page at Historial de publicaciones\"). If no version is specified or found on the website, the latest available will be used.
 _Example_: To extract historical data from the second half of 2009 do --version 2009/02"
* __--community__: Obtain only data from a specific group of autonomous communities. Any number of autonomous community can be specified. This are the names of tha available autonomous communities: País Vasco, Cataluña, Galicia, Andalucía, Principado de Asturias, Cantabria, La Rioja, Región de Murcia, Comunitat Valenciana, Aragón, Castilla-La Mancha, Canarias, Navarra, Ceuta, Melilla, Castilla y León. The exact name as specified here must be used in order to map the correct autonomous communities. If this flag and --province is not specified a search of all autonomous communities will be done.
_Example_: To search in La Rioja and Canarias do `python3 scraper.py --community \"La Rioja\" Canarias`
* __--province__: Obtain only data from a specific province of an autonomous community. Any number of provinces can be speficied. The names of the provinces by autonomous communities are:
    - País Vasco: Álava, Guipúzcoa, Vizcaya.
    - Cataluña: Barcelona, Tarragona, Lérida, Gerona.
    - Galicia: Coruña, Lugo, Orense, Pontevedra.
    - Andalucía: Almería, Cádiz, Córdoba, Granada, Huelva, Jaén, Málaga, Sevilla.
    - Principado de Asturias: Asturias.
    - Cantabria: Cantabria.
    - La Rioja: La Rioja.
    - Región de Murcia: Murcia.
    - Comunitat Valenciana: Alicante, Castellón, Valencia.
    - Aragón: Huesca, Teruel, Zaragoza.
    - Castilla-La Mancha: Albacete, Ciudad Real, Cuenca, Guadalajara, Toledo.
    - Canarias: Santa Cruz de Tenerife, Las Palmas.
    - Navarra: Navarra.
    - Extremadura: Badajoz, Cáceres.
    - Illes Balears: Baleares.
    - Madrid: Madrid.
    - Ceuta: Ceuta.
    - Melilla: Melilla.
    - Castilla y León: Palencia, Ávila, Burgos, León, Salamanca, Segovia, Soria, Valladolid, Zamora.

    The exact named speficied here must be used in order to map the correct provinces. If a autonomous community and a province from that autonomous community is speficied, the search will be done only to the provinces as this flag is more restrictive.
    _Example_: To search the province of Tarragona, Madrid and Gerona do: `python3 scraper.py --province Tarragona Madrid Gerona`

* __--type__: Obtain only data from entities that belong to a specific type of entity. The possible values are: GOBIERNO CA, OA ADMINISTRATIVO, OA COMERCIAL, OA, ENTIDAD PUBLICA EMPRESARIAL, ENTE PUBLICO, AGENCIA, CONSORCIO, FUNDACION, INSTITUCION SIN AL, SOCIEDAD MERCANTIL, UNIVERSIDAD, CIUDAD AUTONOMA. If this flag is not specified all types of entities will be searched.
_Example_: To search for entities that correspond to the type SOCIEDAD MERCANTIL and FUNDACION do: `python3 scraper.py --type \"SOCIEDAD MERCANTIL\" FUNDACION`
* __--name__: Obtain only data from entities that match the specified name.
* __--cif__: Obtain only data from entities that match the speficied cif.
* __--headless__: If this flag is set the scraping will begin in headless mode (no GUI will be shown).


Once `scraper.py` has been called the scraping will begin. When it finishes it will create a folder under `./output` following the nomenclature `output_dd-mm-yyyy_hh-mm-ss` with seven different files. Six of them are `.csv` files containing the scraped data and one is called `search_info.txt` that stores all the searches done to the website to obtain such information. It is very usefull for traceability.

## Examples

### Obtain all data
To scrap all the data from the website just run:

```
python3 scraper.py
```

The output of this file is available at `./output/output_11-07-2019_11-38-17/`.
### Filtering data
We desire to obtain:
* All those entities that correspond to the type `SOCIEDAD MERCANTIL` and `FUNDACION`,
* for the autonomous community of `Cataluña` and `Cantabria`,
* for the province of `Huelva`,
* during the second half of 2016.

The script should be called with these arguments:

```
python3 scraper.py --version 2016/02 --community Cataluña Cantabria --province Huelva --type \"SOCIEDAD MERCANTIL\" FUNDACION
```

See that for searching the province of `Huelva` it is not necessary to specifiy its autonomous community `Andalucía`. This is because province is more restrictive than autonomous community, thus making the next call would have been the same:

```
python3 scraper.py --version 2016/02 --community Cataluña Cantabria Andalucía --province Huelva --type \"SOCIEDAD MERCANTIL\" FUNDACION
```

The output of this file is available at `./output/output_11-07-2019_12-47-50/`.
