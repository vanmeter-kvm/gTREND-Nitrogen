# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter

###################################################################################################################
# Generate county shapfiles which has normalzied county-scale values for the 15 agricultural and developed components
###################################################################################################################
"""
#Input dataset:
#(1). Finalzied normalized county-scale N fluxes (including agricultural and developed components) CSVs 

#Processes:
#(1). Attch the finalzied normalized county-scale N fluxes values to the CONUS county shapefile 

#Output:
#(1). CONUS county shapefile with finalzied normalized county-scale N fluxes values for 1930-2017

import pandas as pd
import geopandas as gpd
import os 
import numpy as np



def Nvalue_shapefile(Nvalue_path,Nvalue_shapefile_path):
    #read county shapefile
    path_county='G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/P Surplus Dataset Publication Files (2022-07-05)/CountyShapefile_2017/CountyShapefile_2017/'
    county_bd=gpd.read_file(path_county,index_col=4)
    
    #read N value csv and reidnex the csv by county-shapefile index
    Nvalue=pd.read_csv(Nvalue_path,index_col=0)
#    Nvalue=Nvalue.replace([np.inf, -np.inf], np.nan)
#    Nvalue.fillna(0)
    Nvalue.index= ["%05d" %i for i in Nvalue.index.to_list()] 
    Nvalue=Nvalue.reindex(county_bd['GEOID'].to_list())
    
    #add N value colmns to attribute table of county-shapefile
    for i in range(0,len(Nvalue.columns)):
        county_bd[Nvalue.columns[i]]=Nvalue[Nvalue.columns[i]].to_list()
    county_bd.to_file(Nvalue_shapefile_path)

#sohl ag component
path_sohl='D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/Downscaled_csv/'
save_path="D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/N_LU_Shapefile/"

for file in os.listdir(path_sohl):
    if "finalized" in file :
        print(file)
        Nvalue_shapefile(path_sohl+file,save_path+'/'+file[:-4]+'.shp')


    
