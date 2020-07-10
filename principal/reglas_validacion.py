import re

def debe_estar_lleno(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Tipo_Certificacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 0
    if vdato == "A":
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + " | Valor debe ser igual a A"
        d['Bandera'] = 1
    return d

def R_Tipo_Solicitud(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("ALT|MOD", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + " Valor debe ser igual a ALT ó MOD"
        d['Bandera'] = 1
    return d

def R_Titular_Nombre_Razon_Social(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("AMENA|ORANGE", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + " Valor debe ser igual a AMENA ó ORANGE"
        d['Bandera'] = 1
    return d

def R_Expediente_Concesional(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Numero_Visado(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fecha_Visado(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Numero_Colegiado(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Colegio_Profesional(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("COITT|COIT", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Valor debe ser igual a COITT ó COIT"
        d['Bandera'] = 1
    return d

def R_NIF_NIE(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Codigo_Emplazamiento(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Compartido(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Cod_INE_Termino_Municipal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Cod_INE_Provincia(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Latitud(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Longitud(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Datum(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Referencia_Catastral(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Emplazamiento_Cota_Terreno_Sobre_Nivel_Mar(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Calle_Poblacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Calle_Tipo_Via(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Calle_Nombre_Via(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Calle_Numero_Portal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Calle_Situacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Codigo_Estacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    return d

def R_Tipo_Sistema(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("GSM|DCS|UMTS|LTE", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores GSM|DCS|UMTS|LTE"
        d['Bandera'] = 1
    return d

def R_Tipo_Estacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("ER1|ER2|ER3|ER4|ER5", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores ER1|ER2|ER3|ER4|ER5"
        d['Bandera'] = 1
    return d

def R_Entorno_Sensible(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Tipo_Potencia_Radiada(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("PIRE", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe ser igual al valor PIRE"
        d['Bandera'] = 1
    return d

def R_Unidad_Potencia_Maxima_Total(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("W", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe ser igual al valor W"
        d['Bandera'] = 1
    return d

def R_Localizacion_Antena(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("EXTERIOR|INTERIOR", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores EXTERIOR|INTERIOR"
        d['Bandera'] = 1
    return d

def R_Tipo_Antena(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("D|N", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores D|N"
        d['Bandera'] = 1
    return d

def R_Polarizacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("V|H|M|L|CR|CL", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores V|H|M|L|CR|CL"
        d['Bandera'] = 1
    return d

def R_Altura_Antena_Sobre_Terreno(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Inclinacion_Haz_Sobre_Horizontal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Tipo_Ganancia(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("ISO", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe ser igual a valor ISO"
        d['Bandera'] = 1
    return d

def R_Apertura_Horizontal_Haz(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Apertura_Vertical_Haz(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Acimut_Maxima_Radiacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Nivel_Lobulos_Secundarios(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Forma_Volumen(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("PARALELEPIPEDO", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe ser igual a valor PARALELEPIPEDO"
        d['Bandera'] = 1
    return d

def R_Distancia_Referencia(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Coeficiente_Reflexion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
    if not re.match("1|2.56|4", vdato):
        d['OK_KO'] = "KO"
        d['Validacion'] = d['Validacion'] + "Debe estar entre los valores 1 ó 2,56 ó 4"
        d['Bandera'] = 1
    return d

def R_Punto_Medida_IdPunto(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Distancia(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Acimut(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Situacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Tipo_Espacio_Sensible(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Tipo_Via(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Nombre_Via(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Numero_Portal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Codigo_Postal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Poblacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Cod_INE_Termino_Municipal(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_PS_Cod_INE_Provincia(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Tecnico_Responsable(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fecha_Medicion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Medidas_IdEquipo(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fecha_Ultima_Calibracion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Umbral_Deteccion_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Longitud_Cable(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Marca_Medidor(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Modelo_Medidor(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Numero_Serie_Medidor(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Marca_Antena(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Modelo_Antena(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Numero_Serie_Antena(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_IdPunto(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_IdEquipo(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Hora_Inicio_Medicion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Nivel_Referencia_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Nivel_Decision_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Valor_Medido_Promediado_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Valor_Calculado_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Fase_Diferencia_Vm(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Documento_Nombre(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Documento_Extension(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Documento_Codificacion(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d

def R_Documento_Contenido(vdato):
    d = dict()
    if vdato is None:
        d['OK_KO'] = "KO"
        d['Validacion'] = "No existe valor"
        d['Bandera'] = 1
        return d
    else:
        d['OK_KO'] = "OK"
        d['Validacion'] = ""
        d['Bandera'] = 0
        return d