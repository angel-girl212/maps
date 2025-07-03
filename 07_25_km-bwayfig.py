#!/usr/bin/env python
# coding: utf-8

# In[36]:


# GLOBAL COOLING STRATEGIES
# Kyra Meier
# kmeier@thebentway.ca
# July 2, 2025

import geopandas as gp
import matplotlib.pyplot as plt
from shapely.geometry import box
from geopandas import GeoDataFrame
from shapely.geometry import Point

# read file into geodataframe
world = gp.read_file("319/World_Land.shp")

cities = []

masdar = (24.4273, 54.6136)
erbil = (36.19319, 44.0079)
melbourne = (-37.8204, 144.9753)
paris = (48.8588, 2.3521)
barcelona = (41.3857, 2.1755)
mexico = (19.4354, -99.1044)
kamloops = (50.6739, -120.3262)
houston = (29.7633, -95.3541)
berkeley = (37.8718, -122.2752)
seville = (37.3892, -5.9790)
# high line network

city_items = (masdar, erbil, melbourne, paris, barcelona, mexico, kamloops, houston, berkeley, seville)
text = "Featuring:\nMasdar City\nErbil\nMelbourne\nParis\nBarcelona\nMexico City\nKamloops\nHouston\nBerkeley\nSeville"
for item in city_items:
    cities.append(item)

x = []
y = []
    
for i in cities:
    
    lat = float(i[0])  # isolate latitude
    long = float(i[1])  # isolate longitude
    x.append(long)
    y.append(lat) # gis is such a joke bro

# setup
world.crs
world.head()
world = world.drop(columns=['featurecla'])

fig, ax = plt.subplots(figsize=(15, 15)) # set plot parameters in empty container

world.plot(ax=ax,alpha=0.25, edgecolor="black", color='#c3b7ff')

ax.scatter(x, y, label="shady inspirations", color='#650411ff', marker='*', s=150, zorder=5) 

ax.text(0.01, 0.4, text, transform=ax.transAxes)
ax.set_title("INTERVIEWEES: GLOBAL COOLING STRATEGIES", fontsize=16)
ax.legend(loc='upper left')
plt.savefig("Kmeier_0703.svg") # save the final map
plt.show()

