import processing

def clip_raster_to_trend_250m(year):
    processing.run("gdal:cliprasterbymasklayer", { 'ALPHA_BAND' : False,\
    'CROP_TO_CUTLINE' : True, 'DATA_TYPE' : 0, 'EXTRA' : '',\
    'INPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/Jawitz_decadal_tiff/pop_m3_{}_5070.tif'.format(year),\
    'KEEP_RESOLUTION' : True, 'MASK' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/US Counties Fixed Geom v2/US Counties Fixed Geom v2/US_CountyShapefile_2017_fixed_v2.shp',\
    'MULTITHREADING' : False, 'NODATA' : 999999999,'OPTIONS' : '',\
    'OUTPUT' : "G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/Clip_to_trend_extent/pop_m3_{}_5070_clipped.tif".format(year),\
    'SET_RESOLUTION' : False, 'SOURCE_CRS' : None,\
    'TARGET_CRS' : QgsCoordinateReferenceSystem('EPSG:5070'), 'TARGET_EXTENT' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None })

year_l=[1930,1940,1950,1970,1980,1990,2000,2010]

for year in year_l:
    clip_raster_to_trend_250m(year)