#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gp
import matplotlib.pyplot as plt

# read mtl tracts into gdf (?)
tracts = gp.read_file('Montreal_CensusTracts.shp')

tracts.crs # EPSG 3347
tracts = tracts.to_crs(4326)

tracts = tracts.drop(columns=['Population'])
tracts.head()

from geopandas import GeoDataFrame
from shapely.geometry import Point

# read csv file into list
sunsetz = open('kyraz_sunsetz_try3.csv','r')
data = sunsetz.readlines()
sunsetz.close()

parsed_data = []
ids = []
x = []
y = []
geom = []

for line in data:
    listline = line.strip().split(',')
    parsed_data.append(listline)



parsed_data.pop(0)
print(parsed_data)


# In[2]:


for i in parsed_data:
    ids.append(i[0])
    y_coord = float(i[1])
    y_coord = y_coord
    y.append(y_coord)
    x_coord = float(i[2])
    x.append(x_coord)
    geom.append(Point(x_coord, y_coord))

print(tracts.crs)


# In[4]:


fig, ax = plt.subplots(figsize=(15, 15))  
tracts.plot(ax=ax, alpha=0.25, edgecolor="black", color='#c4fff9')  # Plot Montreal map

# If CRS is already EPSG:4326, use original x, y. Otherwise, use x_transformed, y_transformed.
ax.scatter(y, x, label='spots', color='orange', marker='*', s=50, alpha=0.7)

ax.legend(loc='upper left')

#fig, ax = plt.subplots(figsize=(10, 10))

text = ('''pictured:
Mt. Royal Cimitiere
Lac aux Castors
Cote de Neiges
Parc Jean-Michel
Ile de Soeurs
Parc Jean-Drapeau
Lachine Canal
Lafontaine
Parc-Ex
Le Boulevard
Riviere Prairies
Angrignon
Hochelaga-Mercier''')

#source = ('''      Kyra Meier 
#Feb. 20 / 2025 
#         for Prism''') 
#plt.text(0.91, 0.01, source, transform=ax.transAxes)
plt.text(0.01, 0.73, text, transform=ax.transAxes)

plt.title("Sunsetz 4 Us")
#plt.suptitle("The best spots to see the sunset in Montreal, quantitatively.", x=0.5,y=0.82)
plt.savefig("Kyra_Sunsetz.svg")


# In[ ]:




