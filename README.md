# gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)

This repository contains the codes associated with the manuscript titled **"gTREND-Nitrogen - Long-term nitrogen mass balance data for the contiguous United States (1930-2017)"**, currently in revision with *Scientific Data*. Proper citation and DOI forthcoming.

The gTREND-Nitrogen dataset provides a comprehensive, long-term (1930-2017) nitrogen (N) mass balance for the contiguous United States at a spatial resolution of 250 meters. This dataset integrates county-scale estimates of N fluxes with gridded land use and population data to estimate grid-scale surface fluxes of N, including fertilizer, atmospheric deposition, manure inputs, biological fixation, crop uptake, and population-based human waste.

<img src="./Structure.svg" style="zoom:60%;" />

## Primary Data Sources 

* **TREND-Nitrogen V3**: County-scale nitrogen fluxes for the contiguous U.S. (1930–2017). Available in `Data/TREND-N` ([Byrnes et al. 2022](https://figshare.com/articles/dataset/Trajectories_Nutrient_Dataset_for_Nitrogen_TREND-Nitrogen_/20915989)).
* **U.S. County Shapefile**: Boundary shapefile stored in `Data/COUNTY`.
* **Land Cover Data**:
  - 30m National Land Cover Database (NLCD) (2006, 2008, 2011, 2013, 2016) – download from [MRLC](https://www.mrlc.gov/data).
  - 250m historical (1938–1992) and modern (1992–2005) land use and land cover data - download from [Sohl et al 2018a](https://www.sciencebase.gov/catalog/item/59d3c73de4b05fe04cc3d1d1) and [Sohl et al 2018b](https://www.sciencebase.gov/catalog/item/5b96c2f9e4b0702d0e826f6d). 
* **Population Data**: 1km decadal population distributions (1930-2010) - download from ([Yu & Jawitz 2018](https://www.nature.com/articles/sdata201867).

We only provide TREND-N V3 and county shapefile in this repository. Other raw data and intermediate products available upon request.

## Methodology

### Prerequisite

This repository contains code written in both Python `(.py)` and MATLAB `(.m)`. 

Regular Python files: Run with standard Python interpreter. Files prefixed with `QGIS-`: Must be executed through QGIS Python console to leverage QGIS toolbox. 

Required Python packages for standard python files are: `geopandas`, `pandas`, `math`, `os`, `shutile`, `numpy`, `matplotlib`. 

### Scripts





 

