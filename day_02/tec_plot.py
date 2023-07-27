# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:37:47 2023

@author: nitya
"""

from wam_ipe_plotter import plot_tec, save_figure
import sys

command_arguments = sys.argv[1:]

for dataset_name in command_arguments:
    
    save_figure(dataset_name)

