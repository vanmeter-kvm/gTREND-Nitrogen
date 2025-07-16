
#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#3.5 Convert to 250m 
###################################################################################
'''
Input Datasets:
(1). 1000m-annual human waste raster 1930-2017

Processes:
(1). Resample to a 250m resolution, matching the other components of gTREND-Nitrogen

Output Datasets:
(1) 250m-annual human waste raster 1930-2017
'''
import processing
os.chdir("./Data/")
def warp_250m_tif(year, input_path, output_path, resolution):
    processing.run("gdal:warpreproject",{ 'DATA_TYPE' : 0, 'EXTRA' : '', \
    'INPUT' : input_path.format(year), \
    'MULTITHREADING' : False, 'NODATA' : None, 'OPTIONS' : '', \
    'OUTPUT' : output_path.format(year), \
    'RESAMPLING' : 0, 'SOURCE_CRS' : None, \
    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None, 'TARGET_RESOLUTION' : resolution })

year_l=range(1930,2018)

for year in year_l:
    input_path="./POP/human_waste_n/pop_N_{}.tif"
    output_path= './POP/250m_human_waste_n/pop_N_{}_250m.tif'
    resolution =250
    warp_250m_tif(year)