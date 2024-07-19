# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter

###################################################################################
# Normalize county-scale values
###################################################################################

"""

###################################################################################
# Normalize county-scale agrciultural N flux values by agricultural area
###################################################################################
#Input dataset:
#(1). 14 TREND-Nitrogen V3 county-scale agricultural component CSV:
#       CropUptake_Cropland,CropUptake_Pasture, Fix_Cropland,Fix_Pasture, Fertilizer_Agriculture,
#       Lvst_DairyCattle, Lvst_BeefCattle, Lvst_Broilers, Lvst_Equine, Lvst_Hogs, Lvst_LayersPullets,
#       Lvst_OtherCattle,Lvst_SheepGoat, Lvst_Turkeys"
#(2). County-Scale Agricultural Land Use Ratio CSV :
    
#Processes:
#(1). Normalize the county-scale nitrogen (N) flux values for each agricultural component by the agricultural area.
#(2). If a county has zero agricultural land, set the normalized agricultural N fluxes for that county to zero, based on the assumption that downscaling is based on agricultural land use.

#Output:
#(1). normalized county-scale agrciultural N flux for the 14 agricultural N components with zeroes filled for counties with no agricultural land
#       component+_Agriculture_LU_finalized.csv
#(2). normalized county-scale agrciultural N flux for the 14 agricultural N components
#       component+_Agriculture_LU.csv



import pandas as pd 
import geopandas as gpd
import os 
import numpy as np

def N_value_kghaLU_sohl(LU_path,N_path,LU_name,LU_ratio,save_path,flag):
    n_value=pd.read_csv(N_path,index_col=0)
    path_county='D:/Downscale/landuse/sohl/ag/sohl_binary_ag_1938.csv'
    county_bd=pd.read_csv(path_county)
    n_value=n_value.reindex(county_bd['GEOID'].to_list())
    
    n_value_lu=pd.DataFrame(index=n_value.index)
    for yr in range(1930,2018):
        print(yr)
        if yr<2006:
            LU=pd.read_csv(LU_path+'sohl_binary_'+LU_name+'_'+str(yr)+'.csv',index_col=5)
        elif yr>=2006 and yr< 2008:
            LU=pd.read_csv(LU_nlcd_path+'nlcd_binary_'+LU_name+'_'+str(2006)+'.csv',index_col=5)
        elif yr>=2008 and yr< 2011:   
            LU=pd.read_csv(LU_nlcd_path+'nlcd_binary_'+LU_name+'_'+str(2008)+'.csv',index_col=5)
        elif yr>=2011 and yr< 2013:   
            LU=pd.read_csv(LU_nlcd_path+'nlcd_binary_'+LU_name+'_'+str(2011)+'.csv',index_col=5)
        elif yr>=2013 and yr< 2016: 
            LU=pd.read_csv(LU_nlcd_path+'nlcd_binary_'+LU_name+'_'+str(2013)+'.csv',index_col=5)
        elif yr>=2016: 
            LU=pd.read_csv(LU_nlcd_path+'nlcd_binary_'+LU_name+'_'+str(2016)+'.csv',index_col=5)
            
        n_value_lu["y"+str(yr)]=n_value["y"+str(yr)]/LU[LU_ratio]
    if flag==1:
        #due to the assumption that downscaling is based on agricultural land use, if ag land use in a county is zero, the normalized ag N fluxes for this county should be set as zero 
        n_value_lu=n_value_lu.replace([np.inf, -np.inf, np.nan], 0) 

    n_value_lu.to_csv(save_path)

path="D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/"
LU_path='D:/Downscale/landuse/sohl/ag/'
LU_nlcd_path='D:/Downscale/landuse/nlcd/ag/'

component_l=["CropUptake_Cropland","CropUptake_Pasture", "Fix_Cropland","Fix_Pasture", "Fertilizer_Agriculture",\
             "Lvst_DairyCattle","Lvst_BeefCattle","Lvst_Broilers", "Lvst_Equine","Lvst_Hogs","Lvst_LayersPullets",\
                "Lvst_OtherCattle","Lvst_SheepGoat","Lvst_Turkeys" ]
for component in component_l:
    for flag in [1,0]:
        N_path=path+component+".csv"
        LU_name='ag'
        LU_ratio='AG_RATIO'    
        if flag==1:
            save_path=path+"Downscaled_csv/"+component+"_Agriculture_LU_finalized.csv" 
           
        else:
            save_path=path+"Downscaled_csv/"+component+"_Agriculture_LU.csv" 
            
        N_value_kghaLU_sohl(LU_path,N_path,LU_name,LU_ratio,save_path,flag)
        
        
        
#%%
###################################################################################
# Normalize county-scale developed N flux values by developed area
###################################################################################

#Input dataset:
#(1). 14 TREND-Nitrogen V3 county-scale developed component CSV:
#       Fertilizer_Domestic
#(2). County-Scale Developed Land Use Ratio CSV :
    
#Processes:
#(1). Normalize the county-scale nitrogen (N) flux values for each agricultural component by the developed area.
#(2). If a county has zero developed land, set the normalized developed N fluxes for that county to zero, based on the assumption that downscaling is based on developed land use.

#Output:
#(1). normalized county-scale developed N flux for the 1 developed N components with zeroes filled for counties with no developed land
#       component+_Domestic_LU_finalized.csv
#(2). normalized county-scale developed N flux for the 14 agricultural N components
#       component+_Domestic_LU.csv        
        
        
path="D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/"
LU_path='D:/Downscale/landuse/sohl/developed/'
LU_nlcd_path='D:/Downscale/landuse/nlcd/developed/'   
        
        
component_l=['Fertilizer_Domestic']
for component in component_l:

    N_path=path+component+".csv"
    LU_name='dev'
    LU_ratio='DEV_RATIO'  
    if flag==1:
        save_path=path+"Downscaled_csv/"+component+"_Domestic_LU_finalized.csv"
    else:
        save_path=path+"Downscaled_csv/"+component+"_Domestic_LU.csv"
    N_value_kghaLU_sohl(LU_path,N_path,LU_name,LU_ratio,save_path)     
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        

