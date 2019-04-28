#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Get the data as polygons in GeoJSON format
 https://data.melbourne.vic.gov.au/api/geospatial/crvt-b4kt?method=export&format=GeoJSON
Convert data to centroids
 https://gis.stackexchange.com/questions/302430/polygon-to-point-in-geopandas
 pip install geopandas
"""

import geopandas as gpd
sourceGeometryUrl = "https://data.melbourne.vic.gov.au/api/geospatial/crvt-b4kt?method=export&format=GeoJSON"
geoms = gpd.read_file(sourceGeometryUrl)
print(geoms.head())
# copy GeoDataFrame
points = geoms.copy()
# change geometry 
points['geometry'] = points['geometry'].centroid
print(points.head())

#buffered Polygons
buff = geoms.copy()
buff['geometry'] = buff['geometry'].buffer(0.00001) #1 degree = ~111km, so buffer ~1.1m
print(buff.head())

#envelope Polygons
elop = buff.copy()
elop['geometry'] = elop['geometry'].envelope
print(elop.head)

#for each point, buffer by 5meters and extract a snippet of aerial photos.
for index, row in buff.iterrows():
   poly_bounds = row['geometry'].bounds
   print("Polygon bounds is {0}".format(poly_bounds,))