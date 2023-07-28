# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:35:33 2023

@author: z5327332
"""

import netCDF4 as nc
from wam_ipe_plotter import plot_wam_ipe, save_wam_ipe_fig
import sys 

indir = 'C:/Users/z5327332/Documents/Data/'
outdir = indir
# filename = 'wfs.t06z.ipe05.20230725_030500.nc'
filename = sys.argv[1]
dataset = nc.Dataset(indir + filename)
print(dataset)

dataset['tec'][:] # How you get the numpy array of the data
dataset['tec'].units # How you get the units of data


zdata = dataset['tec']
figsize=(12,6)
plot_wam_ipe(dataset,zdata, figsize)

zdata = dataset['tec']
figsize=(12,6)
infilename = 'tec plot1'
save_wam_ipe_fig(dataset, zdata, figsize, outdir + filename)
