# -*- coding: utf-8 -*-

#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
##############################################################################################################
#2.6 Multiply binary land use image with rasterized normalized N fluxes 
##############################################################################################################

'''
Input dataset:
(1). 250m grid-scale raster for the 14 agricultural components and 1 developed component for each year from 1930 to 2017
(2). 250m binary land use raster

Processes:
(1). Raster multiplication: To appropriately assign agricultural N fluxes only to grid cells with agricultural land use, the county-scale flux values were multiplied by the 0 or 1 values in the binary land use grid; similarly, developed N fluxes were assigned only to grid cells with developed land use
 [QGIS Python API]

Output:
(1). Downscaled N fluxes
'''

from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
os.chdir("./Data/")

def generate_binary_raster(binary_raster_path,N_input_path,condition,output_raster_path):
    entries = []
    rlayer1 = QgsRasterLayer(binary_raster_path, "binary")
    QgsProject.instance().addMapLayer(rlayer1, True)
    binary=QgsRasterCalculatorEntry()
    binary.ref = 'binary@1'
    binary.raster=rlayer1 
    binary.bandNumber = 1
    entries.append( binary )
    rlayer2 = QgsRasterLayer(N_input_path, "ninput")
    QgsProject.instance().addMapLayer(rlayer2, True)
    ninput=QgsRasterCalculatorEntry()
    ninput.ref = 'ninput@1'
    ninput.raster=rlayer2 
    ninput.bandNumber = 1
    entries.append( ninput )
    calc = QgsRasterCalculator(condition, \
    output_raster_path, 'GTiff', \
    rlayer2 .extent(), rlayer2 .width(), rlayer2.height() , entries )
    calc.processCalculation()
condition='"binary@1"*"ninput@1"'
component=["CropUptake_Cropland","CropUptake_Pasture", "Fix_Cropland","Fix_Pasture", "Fertilizer_Agriculture",
           "Lvst_DairyCattle","Lvst_BeefCattle","Lvst_Broilers","Lvst_Equine","Lvst_Hogs","Lvst_LayersPullets","Lvst_OtherCattle","Lvst_SheepGoat","Lvst_Turkeys"]
    
bi_path_sohl="./SOHL/SOHL_landcover_250m_binary_clipped/"
bi_path_nlcd="./NLCD/NLCD_landcover_250m_binary_clipped/"
n_path='./TREND-N/N_LU_rasterization/'
save='./gTREND-N/'

for c in component_l:
    for i in range(1930,2017):
        if i<=1938:
            binary_raster_path=bi_path_sohl+'sohl_binary_ag_'+str(1938)+'.tif'
        elif i>1938 and i<2006:
            binary_raster_path=bi_path_sohl+'sohl_binary_ag_'+str(i)+'.tif'
        elif i>=2006 and i< 2008:
            binary_raster_path=bi_path_nlcd+'nlcd_'+str(2006)+'_land_cover_l48_20210604_250m_binary_ag.tif'
        elif i>=2008 and i< 2011:   
            binary_raster_path=bi_path_nlcd+'nlcd_'+str(2008)+'_land_cover_l48_20210604_250m_binary_ag.tif'
        elif i>=2011 and i< 2013:   
            binary_raster_path=bi_path_nlcd+'nlcd_'+str(2011)+'_land_cover_l48_20210604_250m_binary_ag.tif'
        elif i>=2013 and i< 2016: 
            binary_raster_path=bi_path_nlcd+'nlcd_'+str(2013)+'_land_cover_l48_20210604_250m_binary_ag.tif'
        elif i>=2016:         
            binary_raster_path=bi_path_nlcd+'nlcd_'+str(2016)+'_land_cover_l48_20210604_250m_binary_ag.tif'
    
    
        N_input_path=n_path+c+"/"+c+'_rasterized_'+str(i)+'.tif'
        print(N_input_path)
        print(binary_raster_path)
        save_path=save+c+"/"+c+'_rasterized_'+str(i)+'.tif'
        generate_binary_raster(binary_raster_path,N_input_path,condition,save_path)