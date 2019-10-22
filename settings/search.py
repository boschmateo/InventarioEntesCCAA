# Link that allows to go to the search page
go_to_search = "#Cabecera1_lnkbusqueda"

# Entity not available
entity_not_available = "//*[@id='lbl_mensaje']"

# Search parameters

provincia_path = '//*[@id="txtcdprov"]'

ordinal1 = '//*[@id="txtcdcorp"]'

tipo_ente_1_path = '//*[@id="txttiporg1"]'

tipo_ente_2_path = '//*[@id="txttiporg2"]'

ordinal_2 = '//*[@id="txttiporg3"]'

nombre_path = '//*[@id="txtNombre"]'

cif_path = '//*[@id="TxtCIF"]'

buscar_en_historico_nombres = '//*[@id="chkHistorico"]'


# Buttons that allows to submit a search
submit_search = "//*[@id='bt_buscar']"

# Table with the results
results_table_path = "//*[@id='TablaResultados']"

entity_types = {
    'GOBIERNO CA': ["BB"],
    'OA ADMINISTRATIVO': ["BV"],
    'OA COMERCIAL': ["BL"],
    'OA': ["BO"],
    'ENTIDAD PUBLICA EMPRESARIAL': ["BI"],
    'ENTE PUBLICO': ["BU"],
    'AGENCIA': ["BY"],
    'CONSORCIO': ["CC"],
    'FUNDACION': ["HH"],
    'INSTITUCION SIN AL': ["NN"],
    'SOCIEDAD MERCANTIL': ["BP", "XP", "ZP", "FP"],
    'UNIVERSIDAD': ["BW"],
    'CIUDAD AUTONOMA': ["ZZ"],
}