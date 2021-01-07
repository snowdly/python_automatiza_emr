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



r = obtiene_polarizacion('AQU4518R25v06')
print (r["Polarizacion"])

#for a in r["Polarizacion"]:
#    print(a)
