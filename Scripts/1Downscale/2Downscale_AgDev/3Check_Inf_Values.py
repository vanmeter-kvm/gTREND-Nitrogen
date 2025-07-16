# -*- coding: utf-8 -*-

#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
###################################################################################
#2.3 Check inf values due to our downscaling assumption 
###################################################################################


'''
Input dataset:
(1). Normalized county-scale N fluxes (including agricultural and developed components) CSVs 

Processes:
(1). Identify the years during which the normalized N mass balance components contain invalid values (-inf, inf, NaN) due to the downscaling assumption. 

Output:
(1). Flagged invalid normalzied values for specific components under specific years
'''

import pandas as pd
import numpy as np
import math
from shutil import copyfile
import os 
os.chdir("./Data/")
path="./TREND-N/Downscaled_csv/"

def get_inf_indx(path,file):
    file_path=path+file
    df=pd.read_csv(file_path,index_col=0)
    #find county which has inf number 
    county_inf= df.index[np.isinf(df).any(axis=1)]
    inf_list={}
    for county in county_inf:
        inf_list['{}'.format(county)]=[]
        for index, value in df.loc[county].items():
            if value==math.inf:
                inf_list['{}'.format(county)].append(int(index[1:]))

    inf_df=pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in inf_list.items() ]))
    inf_df.to_csv(path+file[:-4]+'_inf.csv') 
    print('finish!')


for file in os.listdir(path):
    if "inf" not in file and "finalized" not in file :
        get_inf_indx(path, file)



