show_all_data = "//*[@id='Hyperlink1']"

# Available information for a single entity

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
activity_values = ["codigo", "actividad", "fuente_alta", "inf_fuente_alta", "alta_desde"]

# Components data
components_table = "//*[@id='TABLE1']"
components_values = ["codigo", "componente", "porcentaje_participacion", "porcentaje_voto",
                    "fuente_alta", "inf_fuente_alta", "alta_desde"]

# Historical name data
historical_name_table = "//*[@id='TABLE2']"
historical_name_values = ["nombre", "fuente_alta", "inf_fuente_alta", "fuente_baja",
                         "inf_fuente_baja", "alta_desde", "baja_desde"]

# Historical social capital data
historical_social_capital_table = "//*[@id='TABLE3']"
historical_social_capital_values = ["nombre", "fuente_alta", "inf_fuente_alta", "fuente_baja",
                                  "inf_fuente_baja", "alta_desde", "baja_desde"]
