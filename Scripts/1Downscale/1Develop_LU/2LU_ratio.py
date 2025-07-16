# -*- coding: utf-8 -*-

#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#1.2 Prepare and generate county land use ratio
###################################################################################

'''
Input Datasets:
(1). 250 Binary land use imagery 1938-2017


Processes:
(1). Apply Zonal Statistics to Binary Images to Calculate County-Scale Land Use Ratios [Python]
-County-scale agricultural land use ratio
-County-scale developed land use ratio

Outputs:
(1). County-Scale Land Use Ratio CSV (1938–2017):
-CSV files containing the agricultural land use ratio for each county.
-CSV files containing the developed land use ratio for each county.
'''
from rasterstats import zonal_stats
import geopandas as gpd
import pandas as pd 
os.chdir("./Data/")
county=gpd.read_file('./COUNTY/US_county.gpkg',)

def zonal_stats(years, img_path, county, column_name, save):
    for year in years:
        df_wshd=county.drop(columns="geometry")
        df_wshd=county.set_index("GEOID")
        n=zonal_stats(county, img_path.format(year), stats="mean")
        n = pd.DataFrame(n)
        df_wshd[colum_name]=n["mean"].
        df_wshd.to_csv(save.format(year))
        
zonal_stats(range(1930, 2006), path_save+"Agriculture/SOHL/sohl_binary_ag_clipped{}.tif" county, "AG_RATIO", "./landuse/sohl/ag/sohl_binary_ag_{}.csv")
zonal_stats(range(1930, 2006), path_save+"Developed/SOHL/sohl_binary_developed_clipped{}.tif" county, "DEV_RATIO", "./landuse/sohl/dev/sohl_binary_developed_{}.csv")
zonal_stats(yearl,path_save+"Agriculture/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_ag.tif".format(year), county, "AG_RATIO", "./landuse/nlcd/ag/nlcd_binary_ag_NLCD_{}_Land_Cover_L48_20190424.csv")
zonal_stats(years, path_save+"Developed/NLCD/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.tif", county, "DEV_RATIO", "/landuse/nlcd/dev/nlcd_{}_land_cover_l48_20210604_250m_clipped_binary_developed.csv")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
