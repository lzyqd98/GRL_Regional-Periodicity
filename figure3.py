#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:38:59 2023

@author: Zhaoyu Liu
"""
#### This code is to plot figure 3, coross section of LWA spectra ####
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

S_m = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/LWA_spectra_55S.npy')
lon = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/lon_ERA.npy')
frq1 = np.load('/Users/liu3315/Documents/Research_BAM/Spring2023/Manuscript1/repository/frq1.npy')

loo, ff= np.meshgrid(lon, frq1)
maxlevel = S_m[:,:].max()
minlevel = S_m[:,:].min()  
levs = np.linspace(minlevel, maxlevel, 15)


fig = plt.figure(figsize=[20,5])
ax = fig.add_subplot(1,1,1)

plt.contourf(lon,frq1, S_m[:,:], levs, cmap='hot_r')
cb=plt.colorbar()
cb.set_label('Power Density',fontsize=12)

plt.contour(lon,frq1, S_m[:,:], levs, colors='k', linewidth='0.5')

ax.set_xlim(0,358.5)
ax.set_ylim(0,0.25)
ax.set_xticklabels(['0', '50E', '100E', '150E', '160W','110W','60W','10W'])
plt.xlabel('longitude',fontsize=12)
plt.ylabel('frequency',fontsize=12)

plt.hlines(1/30, 0, 360)
plt.hlines(1/20, 0, 360)

plt.title("Power Spectral of LWA on 55S (DJF)", pad=5, fontdict={'family':'Times New Roman', 'size':16})
