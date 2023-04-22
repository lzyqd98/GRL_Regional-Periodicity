# GRL_Regional-Periodicity
This repository is an open source for the GRL paper: Regional Features of the1 20-30 Day Periodic Behavior in the Southern Hemisphere Circulation


This repository includes three codes associated with several numpy data to reproduce figure 1 to figure 4 
including some of the supplementary figures. Details are shown below:

1. figure1.np is to plot the rain rate spectra features. 
Associated with the lon_asmre, lat_asmre which are the lon lat grids in in the AMSR-E. 
Rain_spectra 1-4.npy are the power spectra of surface rain rate averaged between 40S and 50S and 1:0-90E, 2:90E-180, 3:180-90W, 4:90W-0. 
Rain_spectra_0.npy is the spectra of the zonal-mean and 40S-50S mean. 
Rain_spectra.npy is only the zonal mean.

2. figure2-4.np is to plot all the filtered variance of different variables. 
lon_ERA and lat_ERA provides the horizontal resolution for the ERA data. 
intra_EKE.npy, intra_LWA_Z.npy, intra_LWA.npy, intra_VT.npy are the 37 year DJF averaged standard deviation filtered within 10-45 day frequency band. 
syn_EKE.npy, syn_LWA_Z.npy, syn_LWA.npy, syn_VT.npy are the 37 year DJF averaged standard deviation filtered within 2-7 day frequency band. 
freq1.np contains the frequency domain.

3. figrue3.np is to plot the cross-section power spectra of different variables.
Using the same freq1 and lon and lat, we will use LWA_spectra_45S and 55S.npy to plot the cross section
