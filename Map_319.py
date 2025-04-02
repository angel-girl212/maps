#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Personal Deity Profile - Afro-Diasporic Tradition of St. Jacques Majeur
# Kyra Meier
# McGill University
# Relg 319

import geopandas as gp
import matplotlib.pyplot as plt
from shapely.geometry import box

# read file into geodataframe
world = gp.read_file("World_Land.shp")

# setup
world.crs
world.head()
world = world.drop(columns=['featurecla'])

# create bounding box and define coordinates
bbox_coords = [
    (-14.084473,6.337137,-9.909668,10.336536), # sierra leone
    (-0.769043,3.359889,14.985352,14.306969), # benin, togo, nigeria
    (-74.575195,17.623082,-71.542969,20.344627), # haiti
    (-85.297852,19.394068,-73.740234,23.966176), # cuba
    (-47.768555,-16.972741,-36.035156,-8.146243), # brazil
]

# create gdf for bounding boxes
bbox_polygons = [box(*coords) for coords in bbox_coords]
bbox_gdf = gp.GeoDataFrame(geometry=bbox_polygons, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(15, 15)) # set plot parameters in empty container

world.plot(ax=ax,alpha=0.25, edgecolor="black", cmap='gist_heat')

lat, lon = 29.422853, -90.226593 # new orleans
ax.scatter(lon, lat, color='#650411ff', marker='*', zorder=5) 
bbox_gdf.boundary.plot(ax=ax, edgecolor='#650411ff', linewidth=2)

ax.set_title("St. Jacques Majeur Diasporic Tradition", fontsize=16)
plt.savefig("KyraMeier_319.png") # save the final map
plt.show()

