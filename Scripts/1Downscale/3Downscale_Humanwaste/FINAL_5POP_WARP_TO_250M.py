'''
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#Convert to 250m
###################################################################################
'''

import processing

def warp_250m_tif(year, input_path, output_path, resolution):
    processing.run("gdal:warpreproject",{ 'DATA_TYPE' : 0, 'EXTRA' : '', \
    'INPUT' : input_path.format(year), \
    'MULTITHREADING' : False, 'NODATA' : None, 'OPTIONS' : '', \
    'OUTPUT' : output_path.format(year), \
    'RESAMPLING' : 0, 'SOURCE_CRS' : None, \
    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None, 'TARGET_RESOLUTION' : resolution })

year_l=range(1930,2018)

for year in year_l:
    input_path="./Data/POP/human_waste_n/pop_N_{}.tif"
    output_path= './Data/POP/250m_human_waste_n/pop_N_{}_250m.tif'
    resolution =250
    warp_250m_tif(year)