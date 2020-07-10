import logging
import os
import pandas as pd
from principal import procesos_comunes
from principal import audita_comprimidos
from principal import lee_directorio
from principal import compara_xml
from principal import valida_xml_individual
from principal import valida_xml_entre
from principal import valida_ine_bd
from principal import valida_fuentes_web
from principal import valida_fuentes_pdf