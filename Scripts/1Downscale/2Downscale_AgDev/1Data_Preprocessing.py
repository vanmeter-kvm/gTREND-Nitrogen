# -*- coding: utf-8 -*-
#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#2.1 Preprocess county-scale data
###################################################################################

'''
Input dataset:
(1). county-scale TREND-Nitrogen V3

Processes:
(1). Convert county-scale N mass balance components in .txt to .csv

Output:
(1). county-scale N mass balance components in .csv format 
'''

import pandas as pd
import os 
os.chdir("./Data/")
n_path="./TREND-N/"

for file in os.listdir(n_path):
    if ".txt" in file:
        df=pd.read_csv(n_path+file,sep=",",index_col=2)
        df.to_csv(n_path+file[:-4]+".csv")