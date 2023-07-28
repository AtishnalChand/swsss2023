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
filenames = sys.argv[1:]
for filename in filenames:
    save_wam_ipe_fig(filename)

