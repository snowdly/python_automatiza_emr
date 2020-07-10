import re
import datetime
from principal import procesos_comunes


def reglas_validacion_individual(etiqueta, regla, vdato, fichero_nombre):
    d = dict()
    V = []
    fichero_nombre_dividido = fichero_nombre.split('_')
    if regla == 'R_Datos_Certificacion_Tipo_Certificacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if vdato != "A":
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a A')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Tipo_Solicitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ALT|MOD", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ALT ó MOD')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Titular_Nombre_Razon_Social':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("AMENA|ORANGE", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a AMENA ó ORANGE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Expediente_Concesional':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("DGZZ-1200436|DGZZ-1104544|M ZZ-0020004|DGZZ-1400353|DGZZ-1300380|DGZZ-1601470|DGZZ-1105021", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a valores de tabla entregada')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Numero_Visado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Fecha_Visado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Numero_Colegiado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Colegio_Profesional':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("COITT|COIT", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a COITT ó COIT')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_NIF_NIE':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Nombre':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Apellido1':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Apellido2':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Codigo_Emplazamiento':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato != fichero_nombre_dividido[1]:
            d['OK_KO'] = 'KO'
            V.append('El valor debe ser igual ala segunda parte del nombre del fichero xml')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Emplazamiento_Compartido':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Termino_Municipal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Provincia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Latitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Longitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Datum':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cota_Terreno_Sobre_Nivel_Mar':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Poblacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Tipo_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Numero_Portal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Situacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Codigo_Estacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato != fichero_nombre_dividido[0]:
            d['OK_KO'] = 'KO'
            V.append('El valor debe ser igual ala primera parte del nombre del fichero xml')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Tipo_Sistema':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("GSM|DCS|UMTS|LTE", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a GSM ó DCS ó UMTS ó LTE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Tipo_Estacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ER1|ER2|ER3|ER4|ER5", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ER1ER2|ER3|ER4|ER5')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Interiores':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Exteriores':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Potencia_Radiada':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("PIRE", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a PIRE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Potencia_Maxima_Total':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Unidad_Potencia_Maxima_Total':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("W", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a W')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Localizacion_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("EXTERIOR|INTERIOR", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a EXTERIOR ó INTERIOR')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("D|N", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a D ó N')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Polarizacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("V|H|M|L|CR|CL", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a V|H|M|L|CR|CL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Altura_Antena_Sobre_Terreno':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Inclinacion_Haz_Sobre_Horizontal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Tipo_Ganancia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ISO", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ISO')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Ganancia_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Vertical_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Acimut_Maxima_Radiacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Nivel_Lobulos_Secundarios':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Forma_Volumen':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("PARALELEPIPEDO", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a PARALELEPIPEDO')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Distancia_Referencia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Coeficiente_Reflexion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match('1|2.56|4', vdato):
            d['OK_KO'] = 'KO'
            V.append('Valor debe ser igual a 1 ó 2.56 ó 4')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_IdPunto':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if float(vdato.replace(',', '.')) < 1:
            d['OK_KO'] = 'KO'
            V.append('Deben ser 5 o más puntos')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Distancia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if not ((float(vdato.replace(',', '.')) >= 0) and (float(vdato.replace(',', '.')) <= 100)):
            d['OK_KO'] = 'KO'
            V.append('Puntos de Medida debe estar entre 0 y 100 metros')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Acimut':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if not ((float(vdato.replace(',', '.')) >= 0) and (float(vdato.replace(',', '.')) <= 359)):
            d['OK_KO'] = 'KO'
            V.append('Puntos de Medida debe estar entre 0 y 359 grados')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Situacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Espacio_Sensible':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Nombre_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Numero_Portal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Codigo_Postal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Poblacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Termino_Municipal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Provincia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Tecnico_Responsable':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Fecha_Medicion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if procesos_comunes.add_months(datetime.datetime.strptime(vdato, '%Y-%m-%d').date(), 3) < datetime.date.today():
            d['OK_KO'] = 'KO'
            V.append('Fecha de medición caducada, es mayor a tres meses a fecha de hoy')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_IdEquipo':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Fecha_Ultima_Calibracion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if procesos_comunes.add_months(datetime.datetime.strptime(vdato, '%Y-%m-%d').date(), 24) < datetime.date.today():
            d['OK_KO'] = 'KO'
            V.append('La calibración tiene como máximo una duración de 2 años')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Umbral_Deteccion_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if float(vdato.replace(',', '.')) < 0.2:
            d['OK_KO'] = 'KO'
            V.append('Toda señal que se haya calculado por debajo de 0,2, no se pone el valor, se pone menor que umbral')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Longitud_Cable':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Marca_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Modelo_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Numero_Serie_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Marca_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Modelo_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Numero_Serie_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdPunto':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdEquipo':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Hora_Inicio_Medicion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Referencia_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Decision_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Medido_Promediado_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Calculado_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Diferencia_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Nombre':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Extension':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Codificacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Contenido':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d