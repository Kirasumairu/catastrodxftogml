#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
try:
	from osgeo import ogr, osr, gdal

except ImportError:
	sys.exit('ERROR: Paquetes GDAL/OGR no encontrados. Compruebe que están instalados correctamente')

try:
	from template_v4 import *

except ImportError:
	sys.exit('ERROR: No se encuentra el script plantilla "template_v4" en el directorio')


def crea_gml(dxf_origen_file, gml_salida_file, src):
	""" Transforma la información de la geometría de un archivo DXF al estándar de Catastro en formato GML v4.0.

	:dxf_origen_file:   Dirección del archivo en formato DXF con la geometría de origen
	:gml_salida_file:   Dirección del archivo en formato GML a sobreescribir con el resultado
	:src:               Sistema de Refencia de Coordendas del DXF. Según cógigos  EPSG
	"""
	driver = ogr.GetDriverByName('DXF')
	data_source = driver.Open(dxf_origen_file, 0)
	layer = data_source.GetLayer()

	if src not in SRC_DICT:
		print('ERROR: El código SRC ({}) indicado es incorrecto.'.format(src))
		print('Los SRC permitidos son 25828, 25829, 25830 o 25831')

		sys.exit()

	print('Archivo GML de salida: {}'.format(gml_salida_file))
	print('Código EPSG seleccionado: {}\n'.format(src))

	with open(gml_salida_file, 'w') as filegml:
		filegml.writelines(PLANTILLA_1)

		print('El archivo {} contiene {} geometría.'.format(dxf_origen_file, layer.GetFeatureCount()))

		for feature in layer:
			geom = feature.GetGeometryRef()

			area = geom.Area()
			print('El área del polígono es {:.4f} m2.'.format(area))

			filegml.writelines(str(area))

			geom = feature.GetGeometryRef()
			if geom is None:
					continue

			gtype = geom.GetGeometryName()

			if gtype == "POLYGON":
					perimetro = geom.GetGeometryRef(0)
			elif gtype in ("LINESTRING", "LINEARRING"):
					perimetro = geom
			else:
					print(f"Geometría no soportada: {gtype}")
					continue

			if perimetro is None:
					print("No se pudo obtener el perímetro")
					continue

			print(f"Este es el perimetro: {perimetro}")

			print('\nTotal de vértices del polígono: {}'.format(perimetro.GetPointCount()))
			print('Listado de coordenadas de los vértices:\nid,x,y')

			filegml.writelines(PLANTILLA_2.format(src=src))

			for i in range(0, perimetro.GetPointCount()):
				pt = perimetro.GetPoint(i)
				coordlist = [str(pt[0]), ' ', str(pt[1]), '\n']

				filegml.writelines(coordlist)

				print('{},{:.4f},{:.4f}'.format(i, pt[0], pt[1]))

		filegml.writelines(PLANTILLA_3)


if __name__ == '__main__':
	if len(sys.argv) < 4:
		sys.exit('ERROR: Falta alguno de los argumentos obligatorio: archivo dxf, archivo gml y/o código SRC.')

	dxf_origen_file = sys.argv[1]
	gml_salida_file = sys.argv[2]
	src = sys.argv[3]

	if os.path.isfile(dxf_origen_file):
		print('Archivo CAD de entrada: {}'.format(sys.argv[1]))

	else:
		sys.exit('ERROR: No existe el fichero DXF {}. Revise la ruta y el nombre de archivo.'.format(dxf_origen_file))

	if src not in SRC_DICT:
		sys.exit('ERROR: SRC indicado incorrecto. SRC permitidos: 25828, 25829, 25830 o 25831')

	crea_gml(dxf_origen_file, gml_salida_file, src)
