# -*- coding: utf-8 -*-
"""
gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
@Shuyu Y. Chang, Danyka K. Byrnes, Nandita B. Basu, Kimberly J. Van Meter


###################################################################################
# County-scale TREND-Nitrogen data preprocessing 
###################################################################################
"""

#Input dataset:
# county-scale TREND-Nitrogen V3

#Processes:
#(1). Convert county-scale N mass balance components in .txt to .csv


#Output:
#(1). county-scale N mass balance components in .csv format 

import pandas as pd
import os 

n_path="D:/ShuyuChang/Downscale_N/N Surplus Dataset Publication Files (2023-10-18)/N Surplus Dataset Publication Files (2023-10-18)/"


for file in os.listdir(n_path):
    if ".txt" in file:
        df=pd.read_csv(n_path+file,sep=",",index_col=2)
        df.to_csv(n_path+file[:-4]+".csv")