
#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#3.2 Clip Raster based on the county boundary
###################################################################################

'''
Input dataset:
(1). Decadal population .tif

Processes:
(1). Clip Binary Land Use Rasters [QGIS Python API]
Clip the population rasters using the CONUS county shapefile to ensure consistent geometry across datasets.

Output:
(1). Decadal population .tif
'''

import processing
def clip_raster_to_trend_250m(year, mask_path, input_path, output_path):
    processing.run("gdal:cliprasterbymasklayer", { 'ALPHA_BAND' : False,\
    'CROP_TO_CUTLINE' : True, 'DATA_TYPE' : 0, 'EXTRA' : '',\
    'INPUT' : input_path.format(year),\
    'KEEP_RESOLUTION' : True, 'MASK' : mask_path,\
    'MULTITHREADING' : False, 'NODATA' : 999999999,'OPTIONS' : '',\
    'OUTPUT' :output_path.format(year),\
    'SET_RESOLUTION' : False, 'SOURCE_CRS' : None,\
    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None })

os.chdir("./Data/")
year_l=[1930,1940,1950,1970,1980,1990,2000,2010]
input_path ='./POP/Jawitz_decadal_tiff/pop_m3_{}_5070.tif'
output_path ="./POP/Clip_to_trend_extent/pop_m3_{}_5070_clipped.tif"
mask_path = "./COUNTY/US_county.gpkg"

for year in year_l:
    clip_raster_to_trend_250m(year, mask_path, input_path, output_path)