# -*- coding: utf-8 -*-

#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#1.1 Prepare and generate land use binary imagery
###################################################################################

'''
Input Datasets:
(1). 30m NLCD land use images from 1938 to 2005
(2). 250m Sohl land use images for the years 2006, 2008, 2011, 2013, and 2016
(3). CONUS county shapefile

Processes:
(1). Resample 30m NLCD Land Use Rasters to 250m Resolution [QGIS Python API]
Use the QGIS-Python Nearest Neighbor function (Python API) to resample the 30m NLCD land use rasters to a 250m resolution, matching the spatial resolution of the Sohl data.

(2). Classify the Resampled NLCD and Sohl 250m Grid Cells [QGIS Python API]
Classify each grid cell as either:
-Agricultural vs. Non-Agricultural
-Developed vs. Non-Developed

(3). Clip Binary Land Use Rasters [QGIS Python API]
Clip the binary land use rasters from Step (2) using the CONUS county shapefile to ensure consistent geometry across datasets.

Outputs:
(1). 250m Grid-Scale Agricultural Binary Images (1938–2017):
Binary images where 1 indicates agricultural pixels and 0 indicates non-agricultural pixels.

(2). 250m Grid-Scale Developed Binary Images (1938–2017):
Binary images where 1 indicates developed pixels and 0 indicates non-developed pixels.
'''
from qgis.core import *
from PyQt5.QtCore import *
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
import processing 
import pandas as pd 
os.chdir("./Data/")


#%% (1). Resample 30m NLCD Land Use Rasters to 250m Resolution [QGIS Python API]
    
def warp_function(nlcd_path,output_path):
    processing.run("gdal:warpreproject", { 'DATA_TYPE' : 0, 'EXTRA' : '', \
     'INPUT' : nlcd_path, \
         'MULTITHREADING' : False, 'NODATA' : 999999999, 'OPTIONS' : '', \
             'OUTPUT' : output_path, 'RESAMPLING' : 0, 'SOURCE_CRS' : None,\
                 'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None, 'TARGET_RESOLUTION' : 250 })


path_i="./NLCD/NLCD_landcover_2019_release_all_files_20210604/"
path_o="./NLCD/NLCD_landcover_250m/"
year_l=[2006, 2008, 2011, 2013, 2016]

for year in year_l: 
    nlcd_path=path_i+"nlcd_{}_land_cover_l48_20210604/".format(year)+"nlcd_{}_land_cover_l48_20210604.img".format(year)
    output_path=path_o+"nlcd_{}_land_cover_l48_20210604_250m.tif".format(year)
    warp_function(nlcd_path,output_path)
    
#%% (2). Classify the Resampled NLCD and Sohl 250m Grid Cells [QGIS Python API]
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

path="./NLCD/NLCD_landcover_250m/"
save_path="./NLCD/NLCD_landcover_250m_binary/"
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

path="./SOHL/SOHL_landcover_250m/"
save_path="./SOHL/SOHL_landcover_250m_binary/"
for year in range(1938,2006):
    if year<1938:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(1938)
    else:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(year)
    binary_raster_path=save_path+"sohl_binary_ag{}.tif".format(year)
    generate_binary_raster(clipped_raster_path,condition_ag,binary_raster_path)
    
for year in range(1938,2006):
    if year<1938:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(1938)
    else:
        sohl_path=path+"CONUS_Backcasting_y{}.tif".format(year)
    binary_raster_path=save_path+"sohl_binary_developed{}.tif".format(year)
    generate_binary_raster(nlcd_path,condition_dev,binary_raster_path)    
#%% (3).  Clip Binary Land Use Rasters [QGIS Python API]
def clip_raster_to_trend(input_path,shapefile_path, output_path):
    processing.run("gdal:cliprasterbymasklayer", { 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : \
     True, 'DATA_TYPE' : 0, 'EXTRA' : '',\
         'INPUT' :input_path, 'KEEP_RESOLUTION' : True, \
             'MASK' : shapefile_path,\
                 'MULTITHREADING' : False, 'NODATA' : None, 'OPTIONS' : '', 'OUTPUT' :output_path,\
                     'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 'TARGET_EXTENT' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None })

path_save='./LULC/'
p1="./NLCD/NLCD_landcover_250m_binary/"
county='./COUNTY/US_county.gpkg'
for year in year_l: 
    input_path=p1+"nlcd_{}_land_cover_l48_20210604_250m_binary_ag.tif".format(year)
    output_path=path_save+"Agriculture/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_ag.tif".format(year)
    clip_raster_to_trend(input_path,county, output_path)  

    input_path=p1+"nlcd_binary_developed/nlcd_{}_land_cover_l48_20210604_250m_binary_developed.tif".format(year)
    output_path=path_save+"Developed/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.tif".format(year)
    clip_raster_to_trend(input_path,county, output_path)  
    
p2="./SOHL/SOHL_landcover_250m_binary/"
for year in range(1930,2006): 
    input_path=p2+"sohl_binary_ag/sohl_binary_ag{}.tif".format(year)
    output_path=path_save+"Agriculture/SOHL/sohl_binary_ag_clipped{}.tif"
    clip_raster_to_trend(input_path,county, output_path)  

    input_path=p2+"sohl_binary_developed/sohl_binary_developed{}.tif".format(year)
    output_path=path_save+"Developed/SOHL/sohl_binary_developed_clipped{}.tif"
    clip_raster_to_trend(input_path,county, output_path)    
  
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
