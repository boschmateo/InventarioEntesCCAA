show_all_data = "//*[@id='Hyperlink1']"

# Available information for a single entity
generic_data_columns = ["version", "comunidad", "codigo_ente", "tipo_ente", "accionista_mayoritario",
                        "nombre", "cif", "capital_social", "finalidad", "regimen_contable",
                        "regimen_presupuestario", "sector_admin_publica", "fuente_alta", "alta_desde",
                        "ente_proviene", "direccion", "localidad", "codigo_postal", "provincia",
                        "telefono", "fax", "sitio_web", "email"]

# Generic data
codigo_ente = "//*[@id='txtDGCodigoEnte']"
tipo_ente = "//*[@id='TxtDGTipoEnte']"
accionista_mayoritario = "//*[@id='TxtDGAccMayoritario']"
nombre = "//*[@id='txtDGNombre']"
cif = "//*[@id='txtDGCif']"
capital_social = "//*[@id='txtDGCapitalsoc']"
finalidad = "//*[@id='TxtDGFinalidad']"
regimen_contable = "//*[@id='TxtDGRegContable']"
regimen_presupuestario = "//*[@id='txtDGRegPresupuestario']"
sector_admin_publica = "//*[@id='txtDGSecAdmPub']"
fuente_alta_1 = "//*[@id='TxtDGNomFuente']"
fuente_alta_2 = "//*[@id='TxtDGInffuentea']"
alta_desde = "//*[@id='txtDGAltaDesde']"
ente_proviene = "//*[@id='TxtDGEnteProv']"

# Generic data alternative
codigo_ente_alt = "//*[@id='txtCodigoEnte']"
tipo_ente_alt = '//*[@id="TxtTipoEnte"]'
accionista_mayoritario_alt = None
nombre_alt = '//*[@id="txtNombre"]'
cif_alt = '//*[@id="txtCif"]'
capital_social_alt = '//*[@id="txtCapitalsoc"]'
finalidad_alt = '//*[@id="TxtFinalidad"]'
regimen_contable_alt = '//*[@id="TxtRegContable"]'
regimen_presupuestario_alt = '//*[@id="txtRegPresupuestario"]'
sector_admin_publica_alt = '//*[@id="txtSecAdmPub"]'
fuente_alta_1_alt = '//*[@id="TxtNomFuente"]'
fuente_alta_2_alt = '//*[@id="TxtInffuentea"]'
alta_desde_alt = '//*[@id="txtAltaDesde"]'
ente_proviene_alt = '//*[@id="TxtEnteProv"]'

# Postal data (will be included in the same table as generic data)
direccion = "//*[@id='txtDPDireccion']"
localidad = "//*[@id='txtDPLocalidad']"
codigo_postal = "//*[@id='txtDPcdPostal']"
provincia = "//*[@id='TxtDPprovincia']"
telefono = "//*[@id='txtDPtfno']"
fax = "//*[@id='TxtDPfax']"
sitio_web = "//*[@id='TxtDPsiteWeb']"
email = "//*[@id='TxtDPemail']"

# Activity data
activity_table = "//*[@id='TablaDetalle']"
activity_columns = ["codigo", "actividad", "fuente_alta", "inf_fuente_alta", "alta_desde"]

# TODO: Add alternative table
# Components data
components_table = "//*[@id='TABLE1']"
components_columns = ["codigo", "componente", "porcentaje_participacion", "porcentaje_voto",
                     "fuente_alta", "inf_fuente_alta", "alta_desde"]

# Historical name data
historical_name_table = "//*[@id='TABLE2']"
historical_name_columns = ["nombre", "fuente_alta", "inf_fuente_alta", "fuente_baja",
                          "inf_fuente_baja", "alta_desde", "baja_desde"]

# Historical social capital data
historical_social_capital_table = "//*[@id='TABLE3']"
historical_social_capital_columns = ["nombre", "fuente_alta", "inf_fuente_alta", "fuente_baja",
                                  "inf_fuente_baja", "alta_desde", "baja_desde"]
