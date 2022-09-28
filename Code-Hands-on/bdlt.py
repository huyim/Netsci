import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

uzh_colors_de = {'blau': '#0028a5', 'blau_80': '#3353b7', 'blau_60': '#667ec9', 'blau_40': '#99a9db', 'blau_20': '#ccd4ed',
               'ockerrot': '#dc6027', 'ockerrot_80': '#e38052', 'ockerrot_60': '#eaa07d', 'ockerrot_40': '#f1bfa9', 'ockerrot_20': '#f8dfd4',
               'lindengruen': '#91c34a', 'lindengruen_80': '#aad470', 'lindengruen_60': '#bfdf94', 'lindengruen_40': '#d5e9b7', 'lindengruen_20': '#eaf4db',
               'warmgelb': '#fede00', 'warmgelb_80': '#fbe651', 'warmgelb_60': '#fcec7c', 'warmgelb_40': '#fdf3a8', 'warmgelb_20': '#fef9d3',
               'grau': '#a3adb7', 'grau_80': '#b5bdc5', 'grau_60': '#c8ced4', 'grau_40': '#dadee2', 'grau_20': '#edeff1',
               'tuerkis': '#0b82a0', 'tuerkis_80': '#3c9fb6', 'tuerkis_60': '#6bb7c7', 'tuerkis_40': '#9ed0d9', 'tuerkis_20': '#cfe8ec',
               'flaschengruen': '#2a7f62', 'flaschengruen_80': '#569d85', 'flaschengruen_60': '#80b6a4', 'flaschengruen_40': '#abcec2', 'flaschengruen_20': '#d5e7e1'}



uzh_colors = {'blue': '#0028a5', 'blue_80': '#3353b7', 'blue_60': '#667ec9', 'blue_40': '#99a9db', 'blue_20': '#ccd4ed',
               'red': '#dc6027', 'red_80': '#e38052', 'red_60': '#eaa07d', 'red_40': '#f1bfa9', 'red_20': '#f8dfd4',
               'green': '#91c34a', 'green_80': '#aad470', 'green_60': '#bfdf94', 'green_40': '#d5e9b7', 'green_20': '#eaf4db',
               'yellow': '#fede00', 'yellow_80': '#fbe651', 'yellow_60': '#fcec7c', 'yellow_40': '#fdf3a8', 'yellow_20': '#fef9d3',
               'grey': '#a3adb7', 'grey_80': '#b5bdc5', 'grey_60': '#c8ced4', 'grey_40': '#dadee2', 'grey_20': '#edeff1',
               'turquoise': '#0b82a0', 'turquoise_80': '#3c9fb6', 'turquoise_60': '#6bb7c7', 'turquoise_40': '#9ed0d9', 'turquoise_20': '#cfe8ec',
               'green2': '#2a7f62', 'green2_80': '#569d85', 'green2_60': '#80b6a4', 'green2_40': '#abcec2', 'green2_20': '#d5e7e1'}


uzh_color_list = ['#0028a5', '#dc6027', '#91c34a', '#fede00', '#a3adb7', '#0b82a0', '#2a7f62', # FULL
                 '#667ec9', '#eaa07d', '#bfdf94', '#fcec7c', '#c8ced4', '#6bb7c7', '#80b6a4', # 60%
                 '#3353b7', '#e38052', '#aad470', '#fbe651', '#b5bdc5', '#3c9fb6', '#569d85', # 80%
                 '#99a9db', '#f1bfa9', '#d5e9b7', '#fdf3a8', '#dadee2', '#9ed0d9', '#abcec2', # 40%
                 '#ccd4ed', '#f8dfd4', '#eaf4db', '#fef9d3', '#edeff1', '#cfe8ec', '#d5e7e1'] # 20%



def init_bdlt_style(portrait = False, figsize = (9, 5.625), scale=1.6):

    plt.rc('text', usetex=False)

    if type(figsize) in [int, float]:
        figsize = (figsize, figsize/scale)
    
    if portrait:
        mpl.rcParams['figure.figsize'] = (min(figsize), max(figsize))
    else: 
        mpl.rcParams['figure.figsize'] = (max(figsize), min(figsize))
        
    mpl.rcParams['font.family'] = 'sans-serif'

    mpl.rcParams['font.sans-serif'] = [ 'TheSans LP5 Plain', "TheSans" ]
    mpl.rcParams['font.size'] = 12

    mpl.rcParams['axes.titlesize'] = 20
    mpl.rcParams['axes.labelsize'] = 18
    mpl.rcParams['axes.linewidth'] = 1.2 #set the value globally

    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=uzh_color_list) 
    
    mpl.rcParams['lines.markersize'] = 8
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['legend.fontsize'] = 16


    
    
    