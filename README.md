# Environmental Impacts of Volcanic Eruption Over Time

## The purpose of this project is to analyze environmental impacts from the Kilauea eruption dating back from 1992 through to present day. I will look at land and vegetation change and pollution in the atmosphere.

### I will use data from Landsat and ASTER to analyze vegetation indexes based off of the reflectance of different wavelengths. These indices represent vegetation loss and can indicate burn scar from the lava flow. Vegetation loss can have a huge impact on surrounding communities with relation to agriculture and infrastructure loss. The script for **vegetation.py** includes functions for this part of the analysis.

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

### ASTER data is also used to analyze elevation change and  emissivity. This could also help with noting changes to the land.

### I will use MODIS data to study air quality - in particular Aerosol Optical Depth (AOD) which indicates the level at which particles in the air prevent light from traveling through. A level of .1 is considered 'clean' , whereas a level 3 indicates aerosols are so dense that it could obscure the sun.

## With vegetation and atmospheric impact models, I will be able to create a cohesive visualization of the impacts volcanoes have environmentally, which ultimately impacts the social lives of surrounding communities.

## One could further correlate the data to health trends of the community during times of eruption and bad air quality. Agriculture could also be negatively impacted with air quality and loss of vegetation and poor soil quality. Recognizing these trends is important part of analyzing volcanic eruptions and the environmental impacts that result in specific social and economic reactions.  
