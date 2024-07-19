import processing

def warp_250m_tif(year):
    processing.run("gdal:warpreproject",{ 'DATA_TYPE' : 0, 'EXTRA' : '', \
    'INPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/human_waste_n/pop_N_{}.tif'.format(year), \
    'MULTITHREADING' : False, 'NODATA' : None, 'OPTIONS' : '', \
    'OUTPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/250m_human_waste_n/pop_N_{}_250m.tif'.format(year), \
    'RESAMPLING' : 0, 'SOURCE_CRS' : None, \
    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None, 'TARGET_RESOLUTION' : 250 })

year_l=[1967,1972,1973]

for year in year_l:
    warp_250m_tif(year)