import xml.etree.ElementTree as ET
import csv
from datetime import date
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import sys
import os

# inicializamos dateframe

Cod_Municipio = pd.DataFrame()

# datos de direccion  XML


rootDir = 'D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo/23207/GALB6100E_GALR6100E_ER1_M_ARCA_112601_1.xml'
Ficheros_Respaldo = 'D:/EMR_Auditorias_Python/Ficheros_Respaldo'


def Accesos_web(rootDir, Ficheros_Respaldo):
    # DECLARACION DE VARIABLES
    Cod_Municipio = pd.DataFrame()
    Nombre_Municipio = ''

    # OBTIENE FICHERO XML

    tree = ET.parse(rootDir)

    root = tree.getroot()

    for each in root.findall('.//Datos_Emplazamiento'):
        dato_Cod_INE_Termino_Municipal = each.find('.//Cod_INE_Termino_Municipal')

        dato_Cod_INE_Provincia = each.find('.//Cod_INE_Provincia')

        dato_Referencia_Catastral = each.find('.//Referencia_Catastral')

        dato_Latitud = each.find('.//Latitud')

        dato_Longitud = each.find('.//Longitud')

    for each in root.findall('.//Calle'):
        dato_Poblacion = each.find('.//Poblacion')

        dato_Tipo_Via = each.find('.//Tipo_Via')

        dato_Nombre_Via = each.find('.//Nombre_Via')

        dato_Numero_Portal = each.find('.//Numero_Portal')

    # IMPORTAMOS CSV INE

    Cod_Municipio = pd.read_csv(os.path.join(Ficheros_Respaldo, 'Cod_Municipio_Prov.csv'), sep=';', encoding='latin1')

    # FILTRAMOS DATEFRAME CON CODIGOS INE EN BASE A DATOS XML
    Cod_Municipio = Cod_Municipio[Cod_Municipio['Cod_Municipio_Ine'] == dato_Cod_INE_Termino_Municipal.text]

    Cod_Municipio = Cod_Municipio[Cod_Municipio['Cod_Provincia_INE'] == int(dato_Cod_INE_Provincia.text)]

    # SI DATEDRAME VACIO   NO SE PUEDE SACAR LOS DATOS CATASTRO

    if Cod_Municipio.empty:
        # GENERAR CSV RECHAZO COD PROVINCIA MUNICIPIO
        print("ERROR")

    # sacamos cod provincia y cod muninicipio catastro

    for Cod_Municipio_Catastro in Cod_Municipio['Cod_Municipio_Catastro']:
        Codigo_Municipio_Catastro = Cod_Municipio_Catastro

    for Cod_Provincia_Catastro in Cod_Municipio['Cod_Provincia_Catastro']:
        Codigo_Provincia_Catastro = Cod_Provincia_Catastro

    driver = webdriver.Firefox(executable_path=os.path.join(Ficheros_Respaldo, 'geckodriver.exe'))

    try:
        driver.get(
            "https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCConCiud.aspx?UrbRus=U&RefC=" + dato_Referencia_Catastral.text + "&esBice=&RCBice1=&RCBice2=&DenoBice=&from=OVCBusqueda&pest=rc&RCCompleta=" + dato_Referencia_Catastral.text + "&final=&del=" + str(
                Codigo_Provincia_Catastro) + "&mun=" + str(Codigo_Municipio_Catastro))
        # leemos datos devueltos por catastro

        select = driver.find_element_by_xpath(
            "/html/body/form/fieldset/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/span/label")
        # obtenemos los datos
        Datos_Direccion_Catastro = select.text

        print(" referencia catastral ok")

        # comprobamos si son correctos los datos de catastro contra los de xml
    except:
        # codigo catastro erroneo, crear reparo
        print("ERROR codigo catastro")
        pass

    # Opens a new tab
    driver.execute_script("window.open()")

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[1])

    # Navigate to new URL in new tab
    driver.get("https://geoportal.minetur.gob.es/VCTEL/vcne.do")

    # sacamos provincia
    try:
        for N_Provincia in Cod_Municipio['Nombre Provincia']:
            Nombre_Provincia = N_Provincia
        # BUSCAMOS PROVICIA

        select = Select(driver.find_element_by_id('lstProvincias'))
        select.select_by_visible_text(Nombre_Provincia)

        # sacamos municipio

        for N_M_Catastro in Cod_Municipio['Nombre Municipio_Catastro']:
            Nombre_Municipio_Catastro = N_M_Catastro

        # BUSCAMOS MUNICIPIO

        select = Select(driver.find_element_by_id('listmuni'))
        select.select_by_visible_text(Nombre_Municipio_Catastro)
        print("OK municipio  coincide con combo infoantenas")
    except:
        print("ERROR datos de municipio no coincide con combo infoantenas")
        pass

    try:
        # BUSCAMOS CALLE
        select = driver.find_element_by_id('nom_calle')

        select.send_keys(dato_Nombre_Via.text)
        select.send_keys(Keys.RETURN)

        print("Busqueda de la calle oK ")
    except:
        print("ERROR al realizar la busqueda de la calle")
        pass

    try:
        # METEMS ZOOM A MAPA
        time.sleep(2)
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()
        driver.find_element_by_id('OpenLayers.Control.PanZoomBar_59_zoomin_innerImage').click()

        # leer texto OpenLayers.Control.MousePosition_18
        select = driver.find_element_by_id('OpenLayers.Control.MousePosition_18')
        Coordenadas = select.text
        # limpiamos y convertimos en array
        Coordenadas = Coordenadas.replace('ETRS89:', '')
        Coordenadas = Coordenadas.replace(' ', '')
        Coordenadas = Coordenadas.replace('N', '')
        Coordenadas = Coordenadas.replace('O', '')
        # con array coordenadoas crear funcion que reste coordenadas web y xml y segun resultado click en flecha de forma recursiva
        # xpath mapa: //*[@id="OpenLayers.Layer.Vector.RootContainer_33_svgRoot"]

    except:
        print("error problemas al manipular el mapa")
        pass

    # Run other commands in the new tab here
    # Opens a new tab
    driver.execute_script("window.open()")

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[2])

    # Navigate to new URL in new tab
    driver.get("https://www.ign.es/iberpix2/visor/")
    # Run other commands in the new tab here
    time.sleep(10)

    try:

        select = driver.find_element_by_xpath("/html/body/ign-map/div/menu-routecal/div/div[1]/div/input")
        select.send_keys(
            dato_Tipo_Via.text + " " + dato_Nombre_Via.text + " " + dato_Numero_Portal.text + ", " + Nombre_Municipio_Catastro + ", " + Nombre_Provincia)
        time.sleep(4)

        # falta arreglar que pulse en la primera opcion
        # select.sendKeys(Keys.DOWN).sendKeys(Keys.ENTER)

        print("busqueda de calle ok")

    except:
        print("Error al hacer la busqueda en iberpix")
        pass
    """
    #verson de buscueda por coordenadas, problema para meer coordenanda en combo
    try:
        
        select=driver.find_element_by_xpath('/html/body/ign-map/menu-toolbar/div/div[1]/paper-menu-button[1]/div/paper-button/span').click()
        select=driver.find_element_by_xpath('//*[@id="buttonShowPanelSearch"]').click()
        select=driver.find_element_by_xpath('/html/body/ign-map/search-component2/div/panel-component/div/iron-collapse/div/paper-tabs/div/div/paper-tab[2]/div').click()
        #metemos las coordenadas
        select=driver.find_element_by_id('searchLonGradesGeo2')

        #print(select.text)

        #select.send_keys("1")
        
        select=driver.find_element_by_xpath('//*[@id="buttonSearchByGeoCoord"]').click()


        print("busqueda de calle ok")

    except:
        print("Error al hacer la busqueda en iberpix")
        pass
    """

    # Esta comentado por que habre ventana pero se queda pensando el programa , no termina.
    # falta cerrar ventana emergente y meter datos
    # Opens a new tab
    driver.execute_script("window.open()")

    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[3])

    # Navigate to new URL in new tab
    driver.get("https://mapas.fomento.gob.es/VisorSIU/")

    time.sleep(2)
    try:
        select = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/button').click()
        select = driver.find_element_by_xpath('//*[@id="esri_dijit_Search_0_input"]')
        select.send_keys(
            dato_Tipo_Via.text + " " + dato_Nombre_Via.text + " " + dato_Numero_Portal.text + ", " + Nombre_Municipio_Catastro + ", " + Nombre_Provincia)
        select.submit()
        print("OK busqueda de calle")
        # no se puede obtener el tipo de suelo que es por que hay que pulsar en el punto

    except:
        print("ERROR al hacer la busqueda en web de fomento")
        pass


# Llamada a la funcion
Accesos_web(rootDir, Ficheros_Respaldo)
