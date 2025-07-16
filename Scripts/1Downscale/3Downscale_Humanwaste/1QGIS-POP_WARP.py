
#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#3.1 Convert population data to .tif in EPSG:5070
###################################################################################
'''
#Input dataset:
(1). Decadal population .adf
https://springernature.figshare.com/collections/Human_Population_Distribution_in_the_Conterminous_United_States_High_Resolution_Reconstruction_1790-2010/3890191

Processes:
(1). Convert .adf to .tif and change crs to "EPSG:5070" for consistence [QGIS Python API]

Output:
(1). Decadal population .tif
'''

import processing

def warp_5070_tif(year, input_path, output_path, resolution):
    processing.run("gdal:warpreproject",{ 'DATA_TYPE' : 0, 'EXTRA' : '', \
    'INPUT' : input_path.format(year)\
    'MULTITHREADING' : False, 'NODATA' : 999999999, 'OPTIONS' : '', \
    'OUTPUT' : output_path.format(year),\
    'RESAMPLING' : 0,'SOURCE_CRS' : None, 'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'),\
    'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None,\
    'TARGET_RESOLUTION' : resolution })


os.chdir("./Data/")
input_path = './POP/USA_HistoricalPopulationDataset/pop_m3_{}/w001001.adf'
output_path = './POP/Jawitz_decadal_tiff/pop_m3_{}_5070.tif'
resolution = 1000
year_l=[1930,1940,1950,1970,1980,1990,2000,2010]

for year in year_l:
    warp_5070_tif(year,input_path, output_path, resolution)