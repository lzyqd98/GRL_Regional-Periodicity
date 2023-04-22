#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:35:01 2023

@author: Zhaoyu Liu
"""

### This code is to plot figure1, rain rate spectra analysis ###
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature



S_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra.npy')
lat = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/lat_asmre.npy')  
lon = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/lon_asmre.npy')  
frq1 = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/frq1.npy')
S1_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra_1.npy')
S2_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra_2.npy')
S3_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra_3.npy')
S4_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra_4.npy') 
S_m0 = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/rain_spectra_0.npy')  


lat_SH = lat[0:360]
       
fig = plt.figure()

ff, laa = np.meshgrid(frq1, lat_SH)
maxlevel = np.nanmax(S_m[116:221,:]*1e3)
minlevel = np.nanmin(S_m[116:221,:]*1e3)  
levs = np.linspace(minlevel, maxlevel, 11)

ax = fig.add_subplot(2,2,1)

plt.contourf(ff[116:221,:],laa[116:221,:], S_m[116:221,:]*1e3, levs, cmap='hot_r')
ax.set_xlim(0,0.25)
plt.xticks([0.04,0.1,0.2])
plt.yticks(size=9)
plt.xlabel('Frequency',fontsize=9)
plt.ylabel('Latitude',fontsize=9)
plt.vlines(0.03,lat[116],lat[160],colors='k',linestyles='solid', linewidth=1)
plt.vlines(0.03,lat[160],lat[200],colors='b',linestyles='solid', linewidth=2)
plt.vlines(0.03,lat[200],lat[220],colors='k',linestyles='solid', linewidth=1)
plt.vlines(0.05,lat[116],lat[220],colors='k',linestyles='solid', linewidth=1)
plt.vlines(0.05,lat[160],lat[200],colors='b',linestyles='solid', linewidth=2)
plt.vlines(0.05,lat[200],lat[220],colors='k',linestyles='solid', linewidth=1)
plt.hlines(lat[160],0,0.03,colors='k',linestyles='solid', linewidth=1)
plt.hlines(lat[160],0.03,0.05,colors='b',linestyles='solid', linewidth=2)
plt.hlines(lat[160],0.05, 0.25,colors='k',linestyles='solid', linewidth=1)
plt.hlines(lat[200],0,0.03,colors='k',linestyles='solid', linewidth=1)
plt.hlines(lat[200],0.03,0.05,colors='b',linestyles='solid', linewidth=2)
plt.hlines(lat[200],0.05,0.25,colors='k',linestyles='solid', linewidth=1)

cb=plt.colorbar()
cb.set_ticks([1,2,3])
cb.ax.tick_params(labelsize=9)
cb.set_label('Power Intensity',fontsize=9)
plt.title("(a) Zonal-Mean Precipitation", pad=5, fontdict={'family':'Times New Roman', 'size':10})

# plt.savefig("/Users/liu3315/Documents/Proposal/FINESST2023/Fig4.png",dpi=600)

bx = fig.add_subplot(2,2,2)
plt.plot(frq1, S_m0, '-k', linewidth=2)
bx.set_xlim(0,0.25)
bx.set_ylim(0,9e-4)
plt.yticks(())
plt.xticks([0,0.04,0.1,0.2], fontsize=9)
plt.title("(b) Zonal-Mean and 40S-50S mean Precipitation", pad=5, fontdict={'family':'Times New Roman', 'size':10})
plt.xlabel('Frequency',fontsize=9)
plt.ylabel('Power',fontsize=9)
plt.vlines(0.04,0,9e-3,colors='r',linestyles='dashed', linewidth=1)



# fig = plt.figure()

ff, laa = np.meshgrid(frq1, lat_SH)
maxlevel = np.nanmax(S_m[116:221,:]*1e3)
minlevel = np.nanmin(S_m[116:221,:]*1e3)  
levs = np.linspace(minlevel, maxlevel, 11)
cx = fig.add_subplot(2,1,2, projection=ccrs.PlateCarree(central_longitude=180))
## Add the topograhy ##
# ax.stock_img()
cx.coastlines()
cx.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '110m',facecolor='darkseagreen'))
cx.add_feature(cfeature.NaturalEarthFeature('physical', 'ocean', '110m',facecolor='blanchedalmond'))
plt.title("(c) Regional Precipitation Power Spectra (40S-50S)", fontdict={'family':'Times New Roman', 'size':10})
cx.set_extent([0,365, -75, -10], crs=ccrs.PlateCarree())

cx2 = fig.add_axes([0.53,0.23,0.12,0.07])
plt.plot(frq1, S3_m, '-k', linewidth=1)
cx2.set_xlim(0,0.25)
cx2.set_ylim(0,0.003)
cx2.yaxis.set_ticks_position('left')
plt.xticks([0.04], fontsize=7)
plt.yticks(())
plt.title("180-90W", fontdict={'family':'Times New Roman', 'size':9, 'color':'red'})
plt.vlines(0.04,0,3e-3,colors='r',linestyles='solid', linewidth=0.5)
plt.xlabel('Frequency', fontsize=7)
plt.ylabel('Power',fontsize=7)
# plt.xlabel('Frequency',fontsize=12)
# plt.ylabel('Power Spectral',fontsize=12)

cx3 = fig.add_axes([0.34,0.23,0.12,0.07])
plt.plot(frq1, S2_m, '-k', linewidth=1)
cx3.set_xlim(0,0.25)
cx3.set_ylim(0,0.003)
cx3.yaxis.set_ticks_position('left')
plt.xticks([0.04], fontsize=7)
plt.yticks(())
plt.title("90E-180", fontdict={'family':'Times New Roman', 'size':9, 'color':'black'})
plt.vlines(0.04,0,3e-3,colors='r',linestyles='solid', linewidth=0.5)
plt.xlabel('Frequency',fontsize=7)
plt.ylabel('Power',fontsize=7)


cx4 = fig.add_axes([0.16,0.23,0.12,0.07])
plt.plot(frq1, S1_m, '-k', linewidth=1)
cx4.set_xlim(0,0.25)
cx4.set_ylim(0,0.003)
cx4.yaxis.set_ticks_position('left')
plt.xticks([0.04], fontsize=7)
plt.yticks(())
plt.title("0-90E", fontdict={'family':'Times New Roman', 'size':9, 'color':'black'})
plt.vlines(0.04,0,3e-3,colors='r',linestyles='solid', linewidth=0.5)
plt.xlabel('Frequency',fontsize=7)
plt.ylabel('Power',fontsize=7)


cx5 = fig.add_axes([0.75,0.23,0.12,0.07])
plt.plot(frq1, S4_m, '-k', linewidth=1)
cx5.set_xlim(0,0.25)
cx5.set_ylim(0,0.003)
cx5.yaxis.set_ticks_position('left')
plt.xticks([0.04], fontsize=7)
plt.yticks(())
plt.title("90W-0", fontdict={'family':'Times New Roman', 'size':9, 'color':'black'})
plt.vlines(0.04,0,3e-3,colors='r',linestyles='solid', linewidth=0.5)
plt.xlabel('Frequency',fontsize=7)
plt.ylabel('Power',fontsize=7)
