
#gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)
##As part of the gTREND-Nitrogen data package, we also provide a script on the project homepage that can be used to aggregate the gridded data to watershed or other administrative boundaries.

import pandas as pd
import geopandas as gpd
from rasterstats import zonal_stats


def extract_wshd_stats(wshd_path, gtrend_path,var):
    wshd=gpd.read_file(wshd_path)
    if wshd.crs.to_epsg() != 5070:
        wshd = wshd.to_crs(epsg=5070)
        
    df_wshd=wshd.drop(columns=["geometry"])
    n=zonal_stats(wshd, gtrend_path, stats="mean")
    n = pd.DataFrame(n)
    df_wshd[var]=n["mean"].values
    return(df_wshd)

#boundary path
wshd_path=

#gTREND-N raster path
gtrend_path=

#define column name
var=

#export a dataframe stores the aggregated N values
df_wshd=extract_wshd_stats(wshd_path, gtrend_path,var)
