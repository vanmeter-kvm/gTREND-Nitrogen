# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:04:50 2022

@author: Shuyu
"""
import geopandas as gpd
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

import scipy
p='./Data/COUNTY/US_county.gpkg'
 
chang=gpd.read_file(p)
chang=chang.set_index("GEOID")
l=chang.columns.to_list()
year_l=[2010,2000,1990,1980,1970,1960,1950,1940,1930]

def getzonalcolumns(year):
    com=["crop{}me".format(year),  "fix{}mea".format(year), "beef{}me".format(year),\
         "broiler{}".format(year[0:3]), "dairy{}m".format(year), "Equine{}".format(year), "hogs{}me".format(year), "layer{}m".format(year),\
             "other{}m".format(year), "sheep{}m".format(year), "trukey{}".format(year),"fertag{}".format(year), "fertdev{}".format(year[0:3]),\
                 "pop{}mea".format(year), "atm{}mea".format(year), "sur{}mea".format(year)]
    return(com)
     
trend_p="./Data/TREND-N/"

def readgroundtruth(index):
    if index==0:
        gd=pd.read_csv(trend_p+"CropUptake_Agriculture.csv")
    elif index==1:
        gd=pd.read_csv(trend_p+"Fix_Agriculture.csv")
    elif index==2:    
        gd=pd.read_csv(trend_p+"Lvst_BeefCattle.csv")
    elif index==3:
        gd=pd.read_csv(trend_p+"Lvst_Broilers.csv")
    elif index==4:
        gd=pd.read_csv(trend_p+"Lvst_DairyCattle.csv")
    elif index==5:
        gd=pd.read_csv(trend_p+"Lvst_Equine.csv")
    elif index==6:
        gd=pd.read_csv(trend_p+"Lvst_Hogs.csv")
    elif index==7:
        gd=pd.read_csv(trend_p+"Lvst_LayersPullets.csv")
    elif index==8:
        gd=pd.read_csv(trend_p+"Lvst_OtherCattle.csv")
    elif index==9:
        gd=pd.read_csv(trend_p+"Lvst_SheepGoat.csv")
    elif index==10:
        gd=pd.read_csv(trend_p+"Lvst_Turkeys.csv")
    elif index==11:
        gd=pd.read_csv(trend_p+"Fertilizer_Agriculture.csv")
    elif index==12:
        gd=pd.read_csv(trend_p+"Fertilizer_Domestic.csv")
    elif index==13:
        gd=pd.read_csv(trend_p+"Human.csv")

    elif index==14:
        gd=pd.read_csv(trend_p+"Atmospheric_Oxidized.csv")
    else:
        gd=pd.read_csv(trend_p+"NSurplus.csv")
        
    gd=gd.set_index('GEOID')
    #lst = [e[1:] for e in trendpop.index.to_list()]
    lst=map(int,gd.index.to_list())
    gd.index= ["%05d" %i for i in lst ] 
    return(gd)
    

cmap = plt.get_cmap("copper", len(year_l))  
fig, axs = plt.subplots(4,4, figsize=(12, 12), facecolor='w', edgecolor='k',linewidth=2)
fig.subplots_adjust(hspace =0.2, wspace=0.2)

axs = axs.flatten()
for i in range(16):
    gd=readgroundtruth(i)
    chang=chang.reindex(gd.index.to_list())
 
    gdmax=readgroundtruth(i)
    
    
    a=gdmax["y{}".format(1930)].values
    com=getzonalcolumns("1930")
    a1=chang[com[i]].values 
    for j in range(len(year_l)):
        year=str(year_l[j])
        com=getzonalcolumns(year)
        lim=gdmax["y{}".format(2010)].max()

        axs[i].plot(gd["y{}".format(year)],chang[com[i]],'.', color=cmap(j),alpha=1,markersize=15,markeredgecolor='k',markeredgewidth=0.25 )
        


        axs[i].plot([0,lim],[0,lim],'k--',linewidth=2)
        axs[i].set_xlim([0,lim])
        axs[i].set_ylim([0,lim])
        axs[i].tick_params(axis='both', which='major', labelsize=11)
        for axis in ['top','bottom','left','right']:
            axs[i].spines[axis].set_linewidth(2)
        
        b=gd["y{}".format(year)].values
        b1=chang[com[i]].values
        if year!="1930":
            a=np.concatenate((a, b), axis=None)
            a1=np.concatenate((a1, b1), axis=None)
            
    slope, intercept, r2, p, se = scipy.stats.linregress(a,a1.reshape(len(chang[com[i]])*len(year_l),))   
    print(r2)
axs[i].legend(loc="upper right")       


        
        
        
        
        
        
        
        
        
        
        
        
        
        