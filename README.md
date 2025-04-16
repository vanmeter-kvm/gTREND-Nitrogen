# gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)

This repository contains the codes associated with the manuscript titled **"gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)"**, currently in revision with *Scientific Data*. Proper citation and DOI forthcoming.

The gTREND-Nitrogen dataset provides a comprehensive, long-term (1930-2017) nitrogen (N) mass balance for the contiguous United States at a spatial resolution of 250 meters. This dataset integrates county-scale estimates of N fluxes with gridded land use and population data to estimate grid-scale surface fluxes of N, including fertilizer, atmospheric deposition, manure inputs, biological fixation, crop uptake, and population-based human waste.

<img src="./Structure.svg" style="zoom:60%;" />

## Primary Data Sources 

* **TREND-Nitrogen V3**: County-scale nitrogen fluxes for the contiguous U.S. (1930–2017). Available in `Data/TREND-N` ([Byrnes et al. 2022](https://figshare.com/articles/dataset/Trajectories_Nutrient_Dataset_for_Nitrogen_TREND-Nitrogen_/20915989)).
* **U.S. County Shapefile**: Boundary shapefile stored in `Data/COUNTY`.
* **Land Cover Data**:
  - 30m National Land Cover Database (NLCD) (2006, 2008, 2011, 2013, 2016) – download from [MRLC](https://www.mrlc.gov/data).
  - 250m historical (1938–1992) and modern (1992–2005) land use and land cover data - download from [Sohl et al. 2018a](https://www.sciencebase.gov/catalog/item/59d3c73de4b05fe04cc3d1d1) and [Sohl et al. 2018b](https://www.sciencebase.gov/catalog/item/5b96c2f9e4b0702d0e826f6d). 
* **Population Data**: 1km decadal population distributions (1930-2010) - download from ([Yu & Jawitz 2018](https://www.nature.com/articles/sdata201867).

We only provide TREND-N V3 and county shapefile in this repository. Other raw data and intermediate products available upon request.

## Methodology

### Prerequisite

This repository contains code written in both Python `(.py)` and MATLAB `(.m)`. 

Regular Python files: Run with standard Python interpreter. Files prefixed with `QGIS-`: Must be executed through QGIS Python console to leverage QGIS toolbox. 

Required Python packages for standard python files are: `geopandas`, `pandas`, `math`, `os`, `shutile`, `numpy`, `matplotlib`. 

### Scripts

* **Downscale TREND-N V3 according to land use and population distribution**

  -`Scripts/1Downscale/1Develop_LU/`

  * `1QGIS-LU.py`: Resample NLCD to 250m, calculate county agricultural/developed land use ratios, generate binary rasters (ag/non-ag, developed/non-developed)。

  -`Scripts/1Downscale/2Downscale_AgDev/`

  * `1Data_Preprocessing.py`: Convert .txt to .csv for further analysis
  * `2Calculate_Nvalue_LU.py`: Calculate：（1）Nag,county (kg/ha-agland) for agricultural N fluxes； （2）Ndev,county (kg/ha-devland) for non-ag fertilizer
  * `3Check_Inf_Values.py`:  Validate TREND-N V3 vs land use 
  * `4Generate_NVALUE_Shapefile.py`: Generate county-scale vector maps 
  * `5QGIS-Generate_NVALUE_Raster.py`: Rasterize those shapefiles to a 250-m grid scale. 
  * `6QGIS-Generate_Nvalue_raster_with_binary.py`: Spatial allocation: （1） Agricultural N → ag land cells only；（2）Developed N → developed land cells only

  -`/Scripts/1Downscale/3Downscale_Humanwaste/`

  * `1QGIS-POP_WARP.py`: Convert .adf to .tif
  * `2QGIS-POP_CLIP.py`: Clip population raster to county shapefile 
  * `3Matlab-POPInterpolation.m`: Decadal population was linearly interpolated to obtain annual estimates of population. 
  * `4Matlab-POP_CONVERT_TO_KGHA.m`: convert population pop/km2 to kg-N/ha
  * `5QGIS-WARP_TO_250M.py`: Resample 1km to 250m
  * `6Matlab- POP_FIX_GEOMETRY.m`: Geometry correction

* **Technical validation**

  -`/Scripts/2Validation/`

  * `Figure6.py` : Compare county-scale TREND-Nitrogen v3.0 and the gridded gTREND-N, re-aggregated to the county scale

* **Extract basin-averaged N fluxes based on gTREND-N **

  -`/Scripts/3Application/`

  * `EXTRACT_gTREND.py`

  

  





 

