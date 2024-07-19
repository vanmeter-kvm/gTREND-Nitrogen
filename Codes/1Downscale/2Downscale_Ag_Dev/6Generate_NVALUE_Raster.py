# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter

###################################################################################################################
# Rasterize CONUS county shapefile with finalzied normalized county-scale N fluxes values for 1930-2017
###################################################################################################################
"""

#Input dataset:
#(1). CONUS county shapfiles which have normalized agricultural and developed N fluxes values from 1930 to 2017

#Processes:
#(1). Rasterize the shapefile to 250m grids based on the N fluxes values for each year for each component 

#Output:
#(1). 250m grid-scale raster for the 14 agricultural components and 1 develoepd component for each year from 1930 to 2017

import processing
import os
import pandas as pd


def rasterize_Nvalue(Nvalue_shapefile, rasterize_field, save_path,h,w):
    processing.run("gdal:rasterize",{ 'BURN' : None, 'DATA_TYPE' : 5,\
    'EXTENT' : '-2356113.742900000,2258200.176900000,269573.558600000,3172567.920600000 [EPSG:5070]',\
    'EXTRA' : '', 'FIELD' : rasterize_field, 'HEIGHT' : h, 'INIT' : None, 
    'INPUT' : Nvalue_shapefile, 'INVERT' : False,  'NODATA' : 999999999, 
    'OPTIONS' : '', 'OUTPUT' : save_path, 'UNITS' : 1, 'WIDTH' : w })
    
#sohl ag
sohl_shapefile_path="D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/N_LU_Shapefile/"
save_path='D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/N_LU_rasterization/'

component=["CropUptake_Cropland","CropUptake_Pasture", "Fix_Cropland","Fix_Pasture", "Fertilizer_Agriculture",\
             "Lvst_DairyCattle","Lvst_BeefCattle","Lvst_Broilers", "Lvst_Equine","Lvst_Hogs","Lvst_LayersPullets",\
                "Lvst_OtherCattle","Lvst_SheepGoat","Lvst_Turkeys","Fertilizer_Domestic" ]
    
    
for file in os.listdir(sohl_shapefile_path):
    for j in range(15):
        if ".shp" in file and component[j] in file:
            print(file)
            shpfile=sohl_shapefile_path+file
            for i in range(1930,2018):
                print(i)
                save_raster_path=save_path+file[:-14]+"/"+file[:-14]+"_rasterized_"+str(i)+".tif"
                print(save_raster_path)
                rasterize_Nvalue(shpfile,'y'+str(i),save_raster_path,250,250)
            
        
        
        
        
        
        
        
        
        
        
        
    
    

