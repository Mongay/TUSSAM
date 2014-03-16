# -*- coding: UTF-8 -*-

from lxml import etree
from suds.client import Client
import os

os.system("clear")


cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)

linea = raw_input("Linea de TUSSAM: ")
respuesta = cliente.service.GetStatusLinea(linea)

raiz = etree.fromstring(respuesta)
raiz2 = raiz[0][0]

targetNamespace = "{http://tempuri.org/}"

activos = raiz2.find(targetNamespace+"GetStatusLineaResult/"+targetNamespace+"activos")
num_activos = activos.text
frecuencias = raiz2.find(targetNamespace+"GetStatusLineaResult/"+targetNamespace+"frecuencias")
frecuencia = frecuencia.text
incidencias = raiz2.find(targetNamespace+"GetStatusLineaResult/"+targetNamespace+"incidencias")
incidencia = incidencias.text


print "Numero de choches activos: %s" % num_activos
print "La frecuencia es: %s" % frecuencia
print "Incidencias graves: %s" % incidencia 
