# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter


###################################################################################
#Prepare and Generate land use trajectoreis: agricultural and developed land use
###################################################################################
"""

#Input dataset:
#(1). 30m NLCD land use images from 1938 to 2005
#(2). 250m Sohl land use imges for the years 2006, 2008, 2011, 2013, 2016
#(2). CONUS cpunty shapefile 

#Processes:
#(1). Resample 30m NLCD Land Use Rasters to 250m Resolution:
#       Use the QGIS-Python Nearest Neighbor Function API to resample the 30m NLCD land use rasters to 250m resolution, matching the spatial resolution of the Sohl data.
#(2). Classify the resampled NLCD and Sohl 250m grid cells into:
#       Agricultural vs. Non-Agricultural Pixels
#       Developed vs. Non-Developed Pixels
#(3). Clip Binary Land Use Rasters:
#       Clip the binary land use rasters obtained from step 2 using the CONUS shapefile to ensure that land use images from different sources have the same geometry.
#(4). Apply zonal stats to binary images to Calculate county-scale land use ratios
#       County-scale agircultural land use ratio
#       County-scale developed land use ratio

#Output:
#(1). 250m Grid-Scale Agricultural Binary Images for 1930-2017:
#       Binary images where 1 indicates agricultural pixels and 0 indicates non-agricultural pixels.
#(2). 250m Grid-Scale Developed Binary Images for 1930-2017:
#       Binary images where 1 indicates developed pixels and 0 indicates non-developed pixels.
#(3). County-Scale Agricultural Land Use Ratio CSV for 1930-2017 :
#       CSV file containing the agricultural land use ratio for each county.
#(4). County-Scale Developed Land Use Ratio CSV for 1930-2017:
#       CSV file containing the developed land use ratio for each county.

from qgis.core import *
from PyQt5.QtCore import *
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
import processing 
import geopandas as gpd
import pandas as pd 
#%% (1). Resample 30m NLCD Land Use Rasters to 250m Resolution:
    
def warp_function(nlcd_path,output_path):
    processing.run("gdal:warpreproject", { 'DATA_TYPE' : 0, 'EXTRA' : '', \
     'INPUT' : nlcd_path, \
         'MULTITHREADING' : False, 'NODATA' : 999999999, 'OPTIONS' : '', \
             'OUTPUT' : output_path, 'RESAMPLING' : 0, 'SOURCE_CRS' : None,\
                 'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None, 'TARGET_RESOLUTION' : 250 })


path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/NLCD_landuse/NLCD_landcover_2019_release_all_files_20210604/"
year_l=[2006, 2008, 2011, 2013, 2016]


for year in year_l: 
    nlcd_path=path+"nlcd_{}_land_cover_l48_20210604/".format(year)+"nlcd_{}_land_cover_l48_20210604.img".format(year)
    output_path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/NLCD_landuse/NLCD_landcover_250m/"+"nlcd_{}_land_cover_l48_20210604_250m.tif".format(year)
    warp_function(nlcd_path,output_path)
    
#%% (2). Classify the resampled NLCD and Sohl 250m grid cells into:Agricultural vs. Non-Agricultural Pixels & Developed vs. Non-Developed Pixels
   

def generate_binary_raster(clipped_raster_path,condition,binary_raster_path):
    entries = []
    rlayer2 = QgsRasterLayer(clipped_raster_path)
    #QgsProject.instance().addMapLayer(rlayer2, True)
    
    landuse=QgsRasterCalculatorEntry()
    landuse.ref = 'landuse@1'
    landuse.raster=rlayer2 
    landuse.bandNumber = 1
    entries.append(landuse)
    calc = QgsRasterCalculator(condition, \
    binary_raster_path, 'GTiff', \
    rlayer2.extent(), rlayer2.width(), rlayer2.height(), entries )
    calc.processCalculation()

#NLCD Land use 
condition_ag='( "landuse@1" = 81 OR "landuse@1" = 82 ) * 1 + ( "landuse@1" < 81 OR "landuse@1" > 82 ) * 0'
condition_dev='( "landuse@1" = 21 OR "landuse@1" = 22 OR "landuse@1" = 23 OR "landuse@1" = 24 ) * 1 + ( "landuse@1" < 21 OR "landuse@1" > 24 ) * 0'

path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/NLCD_landuse/NLCD_landcover_250m/"
save_path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/NLCD_landuse/NLCD_landcover_250m_binary/"
for year in year_l:
    nlcd_path=path+"nlcd_{}_land_cover_l48_20210604_250m.tif".format(year)
    binary_raster_path=save_path+"nlcd_binary_ag/nlcd_{}_land_cover_l48_20210604_250m_binary_ag.tif".format(year)
    generate_binary_raster(nlcd_path,condition_ag,binary_raster_path)
for year in year_l: 
    nlcd_path=path+"nlcd_{}_land_cover_l48_20210604_250m.tif".format(year)
    binary_raster_path=save_path+"nlcd_binary_developed/nlcd_{}_land_cover_l48_20210604_250m_binary_developed.tif".format(year)
    generate_binary_raster(nlcd_path,condition_dev,binary_raster_path)
    
    
#SOHL Land use  
condition_ag='( "landuse@1" = 13 OR "landuse@1" = 14 ) * 1 + ( "landuse@1" < 13 OR "landuse@1" > 14 ) * 0'
condition_dev='( "landuse@1" ==2 ) * 1 + ( "landuse@1" !=2) * 0'

path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Sohl_landuse/Sohl_landcover_250m/"
save_path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Sohl_landuse/Sohl_landcover_250m_binary/"
for year in range(1938,2006):
    if year<1938:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(1938)
    else:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(year)
    binary_raster_path=save_path+"sohl_binary_ag/sohl_binary_ag{}.tif".format(year)
    generate_binary_raster(clipped_raster_path,condition_ag,binary_raster_path)
    
for year in range(1938,2006):
    if year<1938:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(1938)
    else:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(year)
    binary_raster_path=save_path+"sohl_binary_developed/sohl_binary_developed{}.tif".format(year)
    generate_binary_raster(nlcd_path,condition_dev,binary_raster_path)    
    
#%% (3).  Clip Binary Land Use Rasters
    

def clip_raster_to_trend(input_path,output_path):
    processing.run("gdal:cliprasterbymasklayer", { 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : \
     True, 'DATA_TYPE' : 0, 'EXTRA' : '',\
         'INPUT' :input_path, 'KEEP_RESOLUTION' : True, \
             'MASK' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/US Counties Fixed Geom v2/US Counties Fixed Geom v2/US_CountyShapefile_2017_fixed_v2.shp',\
                 'MULTITHREADING' : False, 'NODATA' : None, 'OPTIONS' : '', 'OUTPUT' :output_path,\
                     'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 'TARGET_EXTENT' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None })




path_save='D:/ShuyuChang/Downscale_P/LULC/'
p1="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/NLCD_landuse/NLCD_landcover_250m_binary/"
p2="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Sohl_landuse/Sohl_landcover_250m_binary/"
for year in year_l: 
    input_path=p1+"nlcd_binary_ag/nlcd_{}_land_cover_l48_20210604_250m_binary_ag.tif".format(year)
    output_path=path_save+"Agriculture/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_ag.tif".format(year)
    clip_raster_to_trend(input_path,output_path)  

    input_path=p1+"nlcd_binary_developed/nlcd_{}_land_cover_l48_20210604_250m_binary_developed.tif".format(year)
    output_path=path_save+"Developed/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.tif".format(year)
    clip_raster_to_trend(input_path,output_path)  
    
    
for year in range(1930,2006): 
    input_path=p2+"sohl_binary_ag/sohl_binary_ag{}.tif".format(year)
    output_path=path_save+"Agriculture/SOHL/sohl_binary_ag_clipped{}.tif"
    clip_raster_to_trend(input_path,output_path)  

    input_path=p2+"sohl_binary_developed/sohl_binary_developed{}.tif".format(year)
    output_path=path_save+"Developed/SOHL/sohl_binary_developed_clipped{}.tif"
    clip_raster_to_trend(input_path,output_path)    
  
        
#%% (4). Apply zonal stats to binary images to Calculate county-scale land use ratios
    
county=gpd.read_file('G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/US Counties Fixed Geom v2/US Counties Fixed Geom v2/US_CountyShapefile_2017_fixed_v2.shp',)


for year in range(1930,2006):
    df_wshd=county.drop(columns="geometry")
    df_wshd=county.set_index("GEOID")
    path_ag=path_save+"Agriculture/SOHL/sohl_binary_ag_clipped{}.tif".format(year)
    n=zonal_stats(county, path_ag, stats="mean")
    n = pd.DataFrame(n)
    df_wshd["AG_RATIO"]=n["mean"].
    df_wshd.to_csv(r"D:\Downscale\landuse\sohl\ag\sohl_binary_ag_{}.csv".format(year))
    
    df_wshd=county.drop(columns="geometry")
    df_wshd=county.set_index("GEOID")
    path_dev=path_save+"Developed/SOHL/sohl_binary_developed_clipped{}.tif".format(year)
    n=zonal_stats(county, path_dev, stats="mean")
    n = pd.DataFrame(n)
    df_wshd["DEV_RATIO"]=n["mean"].
    df_wshd.to_csv(r"D:\Downscale\landuse\sohl\dev\sohl_binary_developed_{}.csv".format(year))    
    
    
for year in year_l:
    df_wshd=county.drop(columns="geometry")
    df_wshd=county.set_index("GEOID")
    path_ag=path_save+"Agriculture/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_ag.tif".format(year)
    n=zonal_stats(county, path_ag, stats="mean")
    n = pd.DataFrame(n)
    df_wshd["AG_RATIO"]=n["mean"].
    df_wshd.to_csv(r"D:\Downscale\landuse\nlcd\ag\nlcd_binary_ag_NLCD_{}_Land_Cover_L48_20190424.csv".format(year))
    
    df_wshd=county.drop(columns="geometry")
    df_wshd=county.set_index("GEOID")
    path_dev=path_save+"Developed/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.tif".format(year)
    n=zonal_stats(county, path_dev, stats="mean")
    n = pd.DataFrame(n)
    df_wshd["DEV_RATIO"]=n["mean"].
    df_wshd.to_csv(r"D:\Downscale\landuse\nlcd\dev\nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.tif".format(year))    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
