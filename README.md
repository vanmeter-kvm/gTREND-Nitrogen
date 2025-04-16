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

  * `1QGIS-LU.py`: Resample NLCD to 250m, calculate county agricultural and developed land use ratio, and generate binary rasters for ag/non-ag and developed/non-developed

  -`Scripts/1Downscale/2Downscale_AgDev/`

  * `1Data_Preprocessing.py`: Convert .txt to .csv for further analysis
  * `2Calculate_Nvalue_LU.py`: Calculate kg/ha-agland for agricultural N fluxes and calculate kg/ha-devland for non-ag fertilizer. 
  * `3Check_Inf_Values.py`: Check the descrepencies between TREND-N V3 and land use data
  * `4Generate_NVALUE_Shapefile.py`: Generate county-scale vector maps of ![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFUAAAAeCAMAAABqtKLHAAAAAXNSR0IArs4c6QAAALRQTFRFAAAAAAAAAAA6AABmADo6ADpmADqQAGZmAGa2OgAAOgA6OgBmOjoAOjo6OjqQOmZmOmaQOma2OpCQOpC2OpDbZgAAZgA6ZgBmZjoAZjo6ZjpmZmYAZmY6ZpC2ZpDbZrbbZrb/kDoAkGY6kJC2kJDbkLb/kNvbkNv/tmYAtmY6tmZmtpA6tpBmttv/tv//25A625Bm27Zm27aQ29uQ29u22////7Zm/7aQ/9uQ/9u2//+2///bOAEBNwAAAAF0Uk5TAEDm2GYAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAAZdEVYdFNvZnR3YXJlAE1pY3Jvc29mdCBPZmZpY2V/7TVxAAABxklEQVRIS+1UaVODMBDNomLxPkDxLHhBWxVaJabJ//9f7tswHe2gow5+685Q0hy7L2/fQ6lVrBhQNiHKmAdNtPbcHx8moQGyVUHRX1Jlti8EZBU2PWbV4ZRizlfip7coY5swTJuA3b7C5ZkqmVKz3WOvlNkquP9x77Ti9mHTM62QVRk8MBF/DbO3rB7QCgscMRF/jVL0/jFAq4LBRK3zlIJdUZhJaX3Xw5/fEFbnZxRcK3cDGbK2eZCZNMiUzQnrIzrkO4tGF44qxV82OW5M5MEPVe0djEk9UCbita2ifgIyfuqi3L9q8Ec0ae41b/cYF+73uUqGJApzOdfU3myYxKs9D8okj8sHfl+rSaTQjHc5ZLPkkpqertYdHhAfxJIsY8ae8KC1OiqMOpqDzUDAqfk2NvEE+0vJq+JpVBX42IOnrQ7L6y7Tc3U3TuMZ2yIo5pcMjLHYZKhmew1qzEATI6vPwtc7gViFr7eM0Y1Rudo877TnhDaeJmijy+nghQm2p8+qjugA0CJaH/LZtygY6giA+VIyqGij7RF683VUIB1YHn8j4ur7j57LOetUVPHjqItpR/8/HX/bIX/dH4fL2SGr+F8G3gG3ATkcCMacuwAAAABJRU5ErkJggg==)
  * `5QGIS-Generate_NVALUE_Raster.py`
  * `6QGIS-Generate_Nvalue_raster_with_binary.py`

  -`/Scripts/1Downscale/3Downscale_Humanwaste/`

  * `1QGIS-POP_WARP.py`
  * `2QGIS-POP_CLIP.py`
  * `3Matlab-POPInterpolation.m`
  * `4Matlab-POP_CONVERT_TO_KGHA.m`
  * `5QGIS-WARP_TO_250M.py`
  * `6Matlab- POP_FIX_GEOMETRY.m`

* **Technical validation**

* **Extract basin-averaged N fluxes based on gTREND-N **

  

  





 

