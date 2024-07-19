import processing
import random
def zonalstats(year):
    processing.run("qgis:zonalstatistics", { 'COLUMN_PREFIX' : '{}'.format(year), \
    'INPUT_VECTOR' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/US Counties Fixed Geom v2/US Counties Fixed Geom v2/US_CountyShapefile_2017_fixed_v2.shp', \
    'INPUT_RASTER' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/interpolated_anaul_pop/pop_{}.tif'.format(year), \
    'OUTPUT' : 'G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/Quality_control/{}_extracted_county_pop_chang.csv'.format(year), \
    'RASTER_BAND' : 1, 'STATISTICS' : [1] })



for i in range(10):
    year=random.randint(1930, 2010)
    print(year)
    zonalstats(year)