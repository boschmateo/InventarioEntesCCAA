button_path = "button"
province_codes_name = "province_codes"
img_path = "image"

# This initial map its necessary to ease the search functionality.
web_map = {
    "País Vasco": {
        button_path: "#enlace_Pais_vasco",
        img_path: '//*[@id="img_paisVasco"]',
        province_codes_name: {
            'Álava': "01",
            "Guipúzcoa": "20",
            "Vizcaya": "48",
        },
    },
    "Cataluña": {
        button_path: "#contenedor_columna_2 > div:nth-child(1) > a",
        img_path: '//*[@id="contenedor_columna_2"]/div[1]/img',
        province_codes_name: {
            "Barcelona": "08",
            "Tarragona": "43",
            "Lérida": "25",
            "Gerona": "17"
        }
    },
    "Galicia": {
        button_path: "#contenedor_columna_3 > div:nth-child(1) > a",
        img_path: '//*[@id="img_galicia"]',
        province_codes_name: {
            "Coruña": "15",
            "Lugo": "27",
            "Orense": "32",
            "Pontevedra": "36"
        }
    },
    "Andalucía": {
        button_path: "#contenedor_columna_4 > div:nth-child(1) > a",
        img_path: '//*[@id="img_andalucia"]',
        province_codes_name: {
            'Almería': "04",
            "Cádiz": "11",
            "Córdoba": "14",
            "Granada": "18",
            "Huelva": "21",
            "Jaén": "23",
            "Málaga": "29",
            "Sevilla": "41"
        }
    },
    "Principado de Asturias": {
        button_path: "#contenedor_columna_1 > div:nth-child(2) > a",
        img_path: '//*[@id="img_asturias"]',
        province_codes_name: {
            "Asturias": "33"
        }
    },
    "Cantabria": {
        button_path: "#contenedor_columna_2 > div:nth-child(2) > a",
        img_path: '//*[@id="img_cantabria"]',
        province_codes_name: {
            "Cantabria": "39",
        }
    },
    "La Rioja": {
        button_path: "#contenedor_columna_3 > div:nth-child(2) > a",
        img_path: '//*[@id="img_rioja"]',
        province_codes_name: {
            "La Rioja": "26",
        }
    },
    "Región de Murcia": {
        button_path: "#contenedor_columna_4 > div:nth-child(2) > a",
        img_path: '//*[@id="img_murcia"]',
        province_codes_name: {
            "Murcia": "30"
        }
    },
    "Comunitat Valenciana": {
        button_path: "#contenedor_columna_1 > div:nth-child(3) > a",
        img_path: '//*[@id="img_valencia"]',
        province_codes_name: {
            "Alicante": "03",
            "Castellón": "12",
            "Valencia": "46"
        }
    },
    "Aragón": {
        button_path: "#contenedor_columna_2 > div:nth-child(3) > a",
        img_path: '//*[@id="2img_aragon"]',
        province_codes_name: {
            "Huesca": "22",
            "Teruel": "44",
            "Zaragoza": "50",
        }
    },
    "Castilla-La Mancha": {
        button_path: "#contenedor_columna_3 > div:nth-child(3) > a",
        img_path: '//*[@id="img_castmancha"]',
        province_codes_name: {
            "Albacete": "02",
            "Ciudad Real": "13",
            "Cuenca": "16",
            "Guadalajara": "19",
            "Toledo": "45"
        }
    },
    "Canarias": {
        button_path: "#contenedor_columna_4 > div:nth-child(3) > a",
        img_path: '//*[@id="img_canarias"]',
        province_codes_name: {
            "Santa Cruz de Tenerife": "38",
            "Las Palmas": "35",
        }
    },
    "Navarra": {
        button_path: "#contenedor_columna_1 > div:nth-child(4) > a",
        img_path: '//*[@id="img_navarra"]',
        province_codes_name: {
            "Navarra": "31",
        }
    },
    "Extremadura": {
        button_path: "#contenedor_columna_2 > div:nth-child(4) > a",
        img_path: '//*[@id="img_extremadura"]',
        province_codes_name: {
            "Badajoz": "06",
            "Cáceres": "10"
        }
    },
    "Illes Balears": {
        button_path: "#contenedor_columna_3 > div:nth-child(4) > a",
        img_path: '//*[@id="img_baleares"]',
        province_codes_name: {
            "Baleares": "07"
        }
    },
    "Madrid": {
        button_path: "#contenedor_columna_4 > div:nth-child(4) > a",
        img_path: '//*[@id="img_madrid"]',
        province_codes_name: {
            "Madrid": "00" # Should be 28, but in the website appears as 00
        }
    },
    "Ceuta": {
        button_path: "#contenedor_columna_2 > div:nth-child(5) > a",
        img_path: '//*[@id="img_ceuta"]',
        province_codes_name: {
            "Ceuta": "51",
        }
    },
    "Melilla": {
        button_path: "#contenedor_columna_3 > div:nth-child(5) > a",
        img_path: '//*[@id="img_melilla"]',
        province_codes_name: {
            "Melilla": "52"
        }
    },
    "Castilla y León": {
        button_path: "#contenedor_columna_1 > div:nth-child(5) > a",
        img_path: '//*[@id="img_castillaleon"]',
        province_codes_name: {
            "Palencia": "34",
            "Ávila": "05",
            "Burgos": "09",
            "León": "24",
            "Salamanca": "37",
            "Segovia": "40",
            "Soria": "42",
            "Valladolid": "47",
            "Zamora": "49"
        }
    },
}




