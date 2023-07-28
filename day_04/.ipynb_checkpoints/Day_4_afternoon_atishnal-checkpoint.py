# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:36:20 2023

@author: z5327332
"""

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

dataset = nc.Dataset('C:/Users/z5327332/Documents/Data/wfs.t06z.ipe05.20230725_030500.nc')
print(dataset)

dataset['tec'][:] # How you get the numpy array of the data
dataset['tec'].units # How you get the units of data

#print(dataset['tec'][:])
#print(dataset['tec'].units)

def plot_tec(dataset, figsize):
    """
    
    Returns the total electron content (TEC) in the ionosphere
    
    Parameters
    ----------
    dataset : Long, Lat and TEC: float
              
    figsize : (15, 15)
        
    Returns
    -------
    fig : Total electron content in the ionosphere
       
    axs : xaxis is Longitude, yaxis is Latitude
        

    """
    #creating figure
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    x, y = np.meshgrid(dataset['lon'], dataset['lat'])
    z = dataset['tec']
    plot1 = axs.pcolormesh(x, y, z)
    axs.set_title('TEC Plot', fontsize=15)
    axs.set_xlabel('Longitude', fontsize=12)
    axs.set_ylabel('Latitude', fontsize=12)
    # color bar settings
    cbar = fig.colorbar(plot1,ax =axs)
    cbar.ax.set_ylabel('TEC', fontsize = 30)
    cbar.ax.tick_params(labelsize = 20)
    return fig, axs


print(np.shape(tec))
figsize=(12,6)
plot_tec(dataset,figsize)

# import matplotlib.pyplot as plt 
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,16))
# ax.pcolormesh(tec)


#%%




dataset = nc.Dataset('C:/Users/z5327332/Documents/Data/wfs.t06z.ipe05.20230725_030500.nc')
print(dataset)

# dataset['tec'][:] # How you get the numpy array of the data
# dataset['tec'].units # How you get the units of data

#print(dataset['tec'][:])
#print(dataset['tec'].units)

def plot_wam_ipe(dataset, zdata, figsize):
    """
    
    Returns other arguments in dataset
    
    Parameters
    ----------
    dataset : Long, Lat and other argument: float
              
    figsize : (15, 15)
        
    Returns
    -------
    fig : 
       
    axs : xaxis is Longitude, yaxis is Latitude
        

    """
    #creating figure
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    x, y = np.meshgrid(dataset['lon'], dataset['lat'])
    plot1 = axs.pcolormesh(x, y, zdata)
    axs.set_title('TEC Plot', fontsize=15)
    axs.set_xlabel('Longitude', fontsize=12)
    axs.set_ylabel('Latitude', fontsize=12)
    # color bar settings
    cbar = fig.colorbar(plot1,ax =axs)
    cbar.ax.set_ylabel(zdata.units, fontsize = 30)
    cbar.ax.tick_params(labelsize = 20)
    return fig, axs

    

zdata = dataset['HmF2']
figsize=(12,6)
plot_wam_ipe(dataset,zdata, figsize)


    
#%%

def save_wam_ipe_fig(dataset,zdata, figsize, infilename):
    # dataset = nc.Dataset('C:/Users/z5327332/Documents/Data/wfs.t06z.ipe05.20230725_030500.nc')
    fig, axs = plot_wam_ipe(dataset, zdata, figsize)
    outfilename = infilename + '.png'
    fig.savefig(outfilename)

zdata = dataset['tec']
figsize=(12,6)
infilename = 'tec plot1'
save_wam_ipe_fig(dataset, zdata, figsize, infilename)
    
    
#print(dataset.keys)

#%%
 




#%%
