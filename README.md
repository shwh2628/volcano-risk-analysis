# Environmental Impacts of Volcanic Eruption Over Time

## The purpose of this project is to analyze environmental impacts from the Kilauea eruption dating back from 1992 through to present day. I will look at vegetation change and pollution in the atmosphere.

### I will use data from Landsat, ASTER, and MODIS (NDVI) to analyze vegetation indexes based off of the reflectance of different wavelengths. These indices represent vegetation loss and can indicate burn scar from the lava flow. Vegetation loss can have a huge impact on surrounding communities with relation to agriculture and infrastructure loss. The script for **vegetation.py** includes functions to simplify this part of the analysis, though not necessary. The notebooks calculate NDVI manually.

def calc_dndvi_dnbr_l8(pre_image, post_image):
  """ Creates a function for calculating the dNDVI and dNBR for Landsat 8

  Parameters
  ----------
  pre_image : raster
      Name of the pre image raster

  post_iamge : raster
      Name of the post image raster

  Returns
  ------
  dndvi : array of calculated dndvi values for the image
  dnbr : array of calculated dnbr values for the image



### I will use data from local sensors to analyze pollution. In the pollution notebook I analyze Particulate Matter and Sulfur Dioxide. Both of these pollutants reached dangerous levels during the eruption.

## With vegetation and atmospheric impact models, I will be able to create a cohesive visualization of the impacts volcanoes have environmentally, which ultimately impacts the social lives of surrounding communities.

## One could further correlate the pollution data to the health trends of the community during times of eruption. Agriculture revenue could also be negatively impacted with air quality and loss of vegetation and poor soil quality. Recognizing these trends is important part of analyzing volcanic eruptions and the environmental impacts that result in specific social and economic reactions.  

## To reproduce these notebooks, an up-to-date conda earth-analytics-python environment is needed.
## I used these imports to run the code :

import os
import geopandas as gpd
from osgeo import gdal
import numpy as np
import numpy.ma as ma
import glob
import matplotlib.pyplot as plt
import subprocess
import earthpy as et
import earthpy.spatial as es
import rasterio as rio
from rasterio.merge import merge
from rasterio.plot import show
from rasterio.plot import plotting_extent
