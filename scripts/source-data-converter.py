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