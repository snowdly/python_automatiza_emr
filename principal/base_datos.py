import mysql.connector
import re

# Datos de conección a la Base de datos
DBaseDatos = {
    "usuario": "admin_web_bqa",
    "password": "Password10_nae",
    "host": "85.25.194.35",
    "database": "web_bqa"
}


def prueba_conectividad():
    resultado = {
        "Conectividad": "OK",
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute('SELECT DISTINCT TRIM(MODELO) AS MODELO FROM datasheet;')
        results = curs.fetchall()
        curs.close()
        conn.close()
    except Exception as e:
        resultado["Conectividad"] = "KO"
        resultado["Error"] = "No ha sido posible conectarse a la BD del servidor " + DBaseDatos["host"]
    return resultado

def obtiene_antenas():
    resultado = {
        "Modelos_Antenas" : [],
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute('SELECT DISTINCT TRIM(MODELO) AS MODELO FROM datasheet;')
        results = curs.fetchall()
        curs.close()
        conn.close()
        resultado["Modelos_Antenas"] = [result[0] for result in results]
    except Exception as e:
        resultado["Modelos_Antenas"] = [""]
        resultado["Error"]="No se ha podido conectar a la Base de Datos para obtener datos de las Antenas"
    return resultado

def obtiene_polarizacion(modelo):
    resultado = {
        "Polarizacion": "",
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute("SELECT DISTINCT TRIM(Polarization) AS Polarization FROM  datasheet WHERE TRIM(MODELO) = '"+ modelo +"'")
        results = curs.fetchall()
        curs.close()
        conn.close()
        consulta = [result[0] for result in results]
        for a in consulta:
            resultado["Polarizacion"] = a

    except Exception as e:
        resultado["Polarizacion"] = ""
        resultado["Error"]="No se ha podido conectar a la Base de Datos para obtener los datos de Polarización"
    return resultado


def ganancia_antena(modelo):
    resultado = {
        "Ganancia": "",
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute("SELECT DISTINCT TRIM(Gain_dBi_Over_all_Tilts) AS Ganancia_Antena, MAX(FRECUENCIA_MAXIMA) AS Frecuencia_Maxima FROM  datasheet WHERE TRIM(MODELO) = '"+ modelo +"'")
        results = curs.fetchall()
        curs.close()
        conn.close()
        consulta = [result[0] for result in results]
        for a in consulta:
            resultado["Ganancia"] = a

    except Exception as e:
        resultado["Ganancia"] = ""
        resultado["Error"]="No se ha podido conectar a la Base de Datos para obtener los datos de Ganancia"
    return resultado


def acimut_maxima_radiacion(modelo):
    resultado = {
        "Acimut": "",
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute("SELECT DISTINCT TRIM(Azimuth_Beamwidth_deg_Average) AS Acimut_Maxima_Radiacion, MAX(FRECUENCIA_MAXIMA) AS Frecuencia_Maxima FROM  datasheet WHERE TRIM(MODELO) = '"+ modelo +"'")
        results = curs.fetchall()
        curs.close()
        conn.close()
        consulta = [result[0] for result in results]
        for a in consulta:
            resultado["Acimut"] = a

    except Exception as e:
        resultado["Acimut"] = ""
        resultado["Error"]="No se ha podido conectar a la Base de Datos para obtener los datos de Ganancia"
    return resultado


def nivel_lobulos_secundarios(modelo):
    resultado = {
        "Lobulo": "",
        "Error": ""
    }
    try:
        conn = mysql.connector.connect(user=DBaseDatos["usuario"], password=DBaseDatos["password"],
                                       host=DBaseDatos["host"],
                                       database=DBaseDatos["database"])
        curs = conn.cursor()
        curs.execute("SELECT DISTINCT TRIM(First_Upper_Sidelobe_level) AS Nivel_Lobulos_Secundarios, MAX(FRECUENCIA_MAXIMA) AS Frecuencia_Maxima FROM  datasheet WHERE TRIM(MODELO) = '"+ modelo +"'")
        results = curs.fetchall()
        curs.close()
        conn.close()
        consulta = [result[0] for result in results]
        for a in consulta:
            resultado["Lobulo"] = a

    except Exception as e:
        resultado["Lobulo"] = ""
        resultado["Error"]="No se ha podido conectar a la Base de Datos para obtener los datos de Ganancia"
    return resultado

#r = ganancia_antena('AQU4518R24v06')
#print (r)

#for a in r["Polarizacion"]:
#    print(a)
