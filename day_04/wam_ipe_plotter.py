# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:37:52 2023

@author: z5327332
"""
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt


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


def save_wam_ipe_fig(filename):
    dataset = nc.Dataset(filename)
    figsize=(15,12)
    fig, axs = plot_wam_ipe(dataset, dataset['tec'], figsize)
    outfilename = filename + '.png'
    fig.savefig(outfilename)



# dataset = nc.Dataset(filename)
# print(dataset)

# dataset['tec'][:] # How you get the numpy array of the data
# dataset['tec'].units # How you get the units of data


# zdata = dataset['tec']
# figsize=(12,6)
# plot_wam_ipe(dataset,zdata, figsize)

# zdata = dataset['tec']
# figsize=(12,6)
# infilename = 'tec plot1'
# save_wam_ipe_fig(dataset, zdata, figsize, outdir + filename)