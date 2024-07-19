import processing

def warp_5070_tif(year):
    processing.run("gdal:warpreproject",{ 'DATA_TYPE' : 0, 'EXTRA' : '', \
    'INPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/USA_HistoricalPopulationDataset/pop_m3_{}/w001001.adf'.format(year),\
    'MULTITHREADING' : False, 'NODATA' : 999999999, 'OPTIONS' : '', \
    'OUTPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/Jawitz_decadal_tiff/pop_m3_{}_5070.tif'.format(year),\
    'RESAMPLING' : 0,'SOURCE_CRS' : None, 'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'),\
    'TARGET_EXTENT' : None, 'TARGET_EXTENT_CRS' : None,\
    'TARGET_RESOLUTION' : 1000 })

year_l=[1930,1940,1950,1970,1980,1990,2000,2010]

for year in year_l:
    warp_5070_tif(year)