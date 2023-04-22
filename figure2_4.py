#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:56:29 2023

@author: Zhaoyu liu
"""

### This code is to plot figure2 3,4, S1, LWA, LWA_Z, Vt and EKE ###
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

#### Read the filtered variance you hpe to analsye ##
LWA_high_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/syn_EKE.npy')
LWA_low_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/intra_EKE.npy')  

LWA_high_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/syn_LWA_Z.npy')
LWA_low_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/intra_LWA_Z.npy') 

LWA_high_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/syn_LWA.npy')
LWA_low_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/intra_LWA.npy') 

LWA_high_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/syn_VT.npy')
LWA_low_std_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/intra_VT.npy') 

lat = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/lat_ERA.npy')
lon = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/lon_ERA.npy')


levs = np.linspace(0,6,15)         ## Scale for LWA ##
levs = np.linspace(0,19760274,15)  ## Scale for LWA_Z ##
levs = np.linspace(0,10, 10)       ## Scale for eddy heat flux ##
levs = np.linspace(0,48,10)        ## Scale for EKE

fig = plt.figure()
plt.clf()
#### Synoptic variation subplot #####
ax = fig.add_subplot(2,1,1, projection=ccrs.PlateCarree(central_longitude=180))

h1 = plt.contourf(lon,lat[82:], LWA_high_std_m[22:,:], levs, transform=ccrs.PlateCarree(), cmap='rainbow' ,extend ='max') 
h2 = plt.contour(lon,lat[82:], LWA_high_std_m[22:,:], levs, transform=ccrs.PlateCarree(), colors='k',linewidths=0.5)  
# plt.xlabel('longitude',fontsize=12)
plt.ylabel('latitude',fontsize=12)
ax.set_extent([-180, 180, -70, -30], ccrs.PlateCarree())

plt.title("(a) Synoptic Variability (2-7d) of EKE (DJF)", pad=5, fontdict={'family':'Times New Roman', 'size':14})
ax.coastlines()
#ax.gridlines(linestyle="--", alpha=0.7)

ax.set_xticks([0,60,120,180,240,300,358.5], crs=ccrs.PlateCarree())
ax.set_yticks([-70,-60,-50,-40,-30], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label='FALSE')
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)  


##### subseasonal to seasonal subplot #####
bx = fig.add_subplot(2,1,2, projection=ccrs.PlateCarree(central_longitude=180))

h3 = plt.contourf(lon,lat[82:], LWA_low_std_m[22:,:], levs, transform=ccrs.PlateCarree(), cmap='rainbow' ,extend ='max') 
h4 = plt.contour(lon,lat[82:], LWA_low_std_m[22:,:], levs, transform=ccrs.PlateCarree(), colors='k',linewidths=0.5)   
plt.xlabel('longitude',fontsize=12)
plt.ylabel('latitude',fontsize=12)
bx.set_extent([-180, 180, -70, -30], ccrs.PlateCarree())
 
plt.title("(b) Intraseasonal Variability (10-45d) of EKE (DJF)", pad=5, fontdict={'family':'Times New Roman', 'size':14})
bx.coastlines()
#bx.gridlines(linestyle="--", alpha=0.7)

bx.set_xticks([0,60,120,180,240,300,358.5], crs=ccrs.PlateCarree())
bx.set_yticks([-70,-60,-50,-40,-30], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label='FALSE')
lat_formatter = LatitudeFormatter()
bx.xaxis.set_major_formatter(lon_formatter)
bx.yaxis.set_major_formatter(lat_formatter)  

plt.hlines(0,358.5,-46.5,colors='r',linestyles='solid', linewidth=0.5)
######## Adjust the subplot #########
plt.subplots_adjust(hspace=-0.5, right=0.85)

######## Draw colorbar #######
cbar = fig.add_axes([0.9,0.25,0.015,0.5])
#cb = plt.colorbar(h1, cax=cbar, ticks=[0, 0.3e7, 0.6e7, 0.9e7, 1.2e7,1.5e7,1.8e7])  ## For LWA_Z
#cb = plt.colorbar(h1, cax=cbar, ticks=[0, 1, 2, 3, 4, 5, 6])  ## For LWA
#cb = plt.colorbar(h1, cax=cbar, ticks=[0, 2, 4, 6, 8, 10])  ## For VT
cb = plt.colorbar(h1, cax=cbar, ticks=[0, 8, 16, 24, 32, 40, 48])  ## For EKE
