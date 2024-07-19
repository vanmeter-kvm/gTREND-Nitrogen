# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:56:51 2024

@author: sxc6234
"""

import pandas as pd
import geopands as gpd

def extract_wshd_stats(wshd_path, gtrend_path,):
    wshd=gpd.read_file(wshd_path)
    df_wshd=wshd.drop(subset="Geometry")
    n=zonal_stats(wshd, gtrend_path, stats="mean")
    n = pd.DataFrame(n)
    df_wshd[var]=n["mean"].values
    return(df_wshd)


wshd_path=
gtrend_path=
extract_wshd_stats(wshd_path, gtrend_path,)
