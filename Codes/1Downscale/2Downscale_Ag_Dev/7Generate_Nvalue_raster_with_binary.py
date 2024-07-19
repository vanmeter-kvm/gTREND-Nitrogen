# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter

###################################################################################################################
# Multiply binary land use image with rasterized normalized N fluxes 
###################################################################################################################
"""


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
component=["CropUptake_Cropland","CropUptake_Pasture", "Fix_Cropland","Fix_Pasture", "Fertilizer_Agriculture",\
             "Lvst_DairyCattle","Lvst_BeefCattle","Lvst_Broilers", "Lvst_Equine","Lvst_Hogs","Lvst_LayersPullets",\
                "Lvst_OtherCattle","Lvst_SheepGoat","Lvst_Turkeys" ]
bi_path_sohl="D:/ShuyuChang/Downscale_P/LULC/Agriculture/SOHL/"
bi_path_nlcd="D:/ShuyuChang/Downscale_P/LULC/Agriculture/NLCD/"
n_path='G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/N Surplus Dataset Publication Files/N_LU_rasterization/'
save='G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/N Surplus Dataset Publication Files (2022-05-26)/N Surplus Dataset Publication Files/N_LU_final_product/'

for c in component_l:
    for i in range(1933,2017):
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