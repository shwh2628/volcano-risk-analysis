"""Process for calculating and plotting vegetation indexes to analyze burn scar and vegetation loss and gain from events of burning

Includes cloud removal for accurrate analysis"""

def plot_rgb_cir_l8(image, date, bool=False):
    """ Creates a mapping function for plotting rgb and cir images from Landsat 8

    Parameters
    ----------
    image : raster
        Name of the file you want to plot

    date : string
        Date of image

    bool : boolean
        boolean to indicate if you want to save the output figure

    Example
    -------
    plot_rgb_cir_l8(landsat_pre, "03-02-2017")
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
    sns.set(font_scale=1.5)

    es.plot_rgb(image, rgb=[3, 2, 1],
                ax=ax1,
                stretch=True)
    ax1.set(title="Landsat 8 | 30 meter resolution \n"
            + "RGB Image " + date)

    es.plot_rgb(image, rgb=[4, 3, 2],
                ax=ax2,
                stretch=True)
    ax2.set(title="Landsat 8 | 30 meter resolution \n"
            + "CIR Image " + date)
    plt.show()
    if bool == True:
        fig.savefig("data/group/outputs/figs/landsat_rgb_cir_" + date + ".png")
        
        

def remove_clouds(array, qa_array, masked_values):
    """ Removes the clouds and cloud shadows from Landsat data
        The output values are a new array with clouds removed for more accurate calculations.

    Parameters
    ----------
    array : a 3-dimensional array of Landsat values that need to have clouds and cloud shadows removed
        The shape of array should be (i, j, k)

    qa_array : a 3-dimensional quality assurance array from Landsat QA file
        The last two dimensions of this array should match the last two dimensions of the input array
        The shape of qa_array should be (1, j, k)

    masked_values : list of the mask values to be used to mask the array

    Returns
    -------
    array_cloud_masked : array of same shape as the input array, with the cloud and cloud shadows masked

    Example
    -------
    landsat_pre_cl = remove_clouds(landsat_pre, landsat_pre_qa, masked_values)
    """
    cl_mask = np.zeros(qa_array.shape)

    for cval in masked_values:
        cl_mask[qa_array == cval] = 1

    cloud_mask = np.broadcast_to(cl_mask == 1, array.shape)
    array_cloud_masked = ma.masked_array(array,
                                         mask=cloud_mask)

    return(array_cloud_masked)



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

    Example
    -------
    landsat_dndvi_06, landsat_dnbr_06 = calc_dndvi_dnbr_l8(landsat_pre_masked, landsat_post_06_masked)
    """
    pre_ndvi = (pre_image[4] - pre_image[3]) / (pre_image[4] + pre_image[3])
    post_ndvi = (post_image[4] - post_image[3]) / \
        (post_image[4] + post_image[3])

    dndvi = post_ndvi - pre_ndvi

    pre_nbr = (pre_image[4] - pre_image[6]) / (pre_image[4] + pre_image[6])
    post_nbr = (post_image[4] - post_image[6]) / \
        (post_image[4] + post_image[6])

    dnbr = pre_nbr - post_nbr

    return dndvi, dnbr


def plot_dndvi_l8(dndvi1, date1, dndvi2, date2, bool=None):
    """ Creates function for plotting dNDVI images from Landsat 8

    Parameters
    ----------
    dndvi1 : raster
        Name of the first dndvi raster you want to plot

    date1 : string
        Date associated with the first plotted dNDVI data

    dndvi2 : raster
        Name of the second dndvi raster you want to plot

    date2 : string
        Date associated with the second plotted dNDVI data

    bool : boolean
        boolean to indicate if you want to save the output figure

    Example
    -------
    plot_dndvi_l8(landsat_dndvi_06, "06-25-2018 - 03-02-2017",
             landsat_dndvi_11, "11-16-2018 - 03-02-2017")
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
    sns.set(font_scale=1.5)

    dndvi1 = ax1.imshow(dndvi1, cmap='PiYG',
                        vmin=-1, vmax=1)
    ax1.set(title="Landsat 8 Derived dNDVI" + "\n" + date1)
    ax1.axis('off')

    dndvi2 = ax2.imshow(dndvi2, cmap='PiYG',
                        vmin=-1, vmax=1)
    ax2.set(title="Landsat 8 Derived dNDVI" + "\n" + date2)
    ax2.axis('off')

    fig.colorbar(dndvi1, fraction=.0168, ax=(ax1, ax2))
    plt.show()
    if bool is not None:
        fig.savefig("data/group/outputs/figs/landsat_dNDVI_" +
                    date1 + "_" + date2 + ".png")
        
def plot_hist_dndvi_l8(dndvi1, date1, dndvi2, date2, bool=None):
    """ Creates a mapping function for plotting dNDVI histograms for Landsat 8

    Parameters
    ----------
    dndvi1 : raster
        Name of the first dndvi raster you want to plot

    date1 : string
        Date associated with the first plotted dNDVI data

    dndvi2 : raster
        Name of the second dndvi raster you want to plot

    date2 : string
        Date associated with the second plotted dNDVI data

    bool : boolean
        boolean to indicate if you want to save the output figure

    Example
    -------
    plot_hist_dndvi_l8(landsat_dndvi_11, "March 2nd, 2017 and Novemeber 16th, 2018", 
                landsat_dndvi_06, "March 2nd, 2017 and June 25th, 2018")
    """
    fig,  (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    sns.set(font_scale=1.0)

    ax1.hist(dndvi1.ravel(), bins=[-.99, -.5, -.2,
                                   0, .2, .5, 1], color="purple")
    ax1.set(title="Landsat 8 Derived dNDVI Histogram \n" + date1)

    ax2.hist(dndvi2.ravel(), bins=[-.99, -.5, -.2,
                                   0, .2, .5, 1], color="purple")
    ax2.set(title="Landsat 8 Derived dNDVI Histogram \n" + date2)

    if bool is not None:
        fig.savefig("data/group/outputs/figs/landsat_hist_dNDVI_" +
                    date1 + date2 + ".png")
        
def plot_dnbr_l8(dnbr1, date1, dnbr2, date2, bool=None):
    """ Creates function for plotting dNDVI images from Landsat 8

    Parameters
    ----------
    dnbr1 : raster
        Name of the first dndvi raster you want to plot

    date1 : string
        Date associated with the first plotted dNBR data

    dnbr2 : raster
        Name of the second dndvi raster you want to plot

    date2 : string
        Date associated with the second plotted dNBR data

    bool : boolean
        boolean to indicate if you want to save the output figure

    Example
    -------
    plot_dnbr_l8(landsat_dnbr_06, "06-25-2018 - 03-02-2017",
             landsat_dnbr_11, "11-16-2018 - 03-02-2017")
    """
    dnbr_class1 = np.digitize(dnbr1, class_bins)
    dnbr_class1_ma = np.ma.masked_array(dnbr_class1, dnbr1.mask)

    dnbr_class2 = np.digitize(dnbr2, class_bins)
    dnbr_class2_ma = np.ma.masked_array(dnbr_class2, dnbr2.mask)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
    sns.set(font_scale=1.5)

    dnbr1 = ax1.imshow(dnbr_class1_ma, cmap=dnbr_cmap)
    values1 = np.unique(dnbr_class1_ma.ravel())
    es.draw_legend(dnbr1,
                   classes=values1,
                   titles=class_dnbr)
    ax1.set(title="Landsat 8 Derived dNBR" + "\n" + date1)
    ax1.axis('off')

    dnbr2 = ax2.imshow(dnbr_class2_ma, cmap=dnbr_cmap)
    values2 = np.unique(dnbr_class2_ma.ravel())
    es.draw_legend(dnbr2,
                   classes=values2,
                   titles=class_dnbr)
    ax2.set(title="Landsat 8 Derived dNBR" + "\n" + date2)
    ax2.axis('off')
    plt.tight_layout()
    plt.show()
    if bool is not None:
        fig.savefig("data/group/outputs/figs/landsat_dNBR_" +
                    date1 + "_" + date2 + ".png")
        
def plot_hist_dnbr_l8(dnbr1, date1, dnbr2, date2, bool=None):
    """ Creates a mapping function for plotting dNBR histograms for Landsat 8

    Parameters
    ----------
    dnbr1 : raster
        Name of the first dndvi raster you want to plot

    date1 : string
        Date associated with the first plotted dNBR data

    dnbr2 : raster
        Name of the second dndvi raster you want to plot

    date2 : string
        Date associated with the second plotted dNBR data

    bool : boolean
        boolean to indicate if you want to save the output figure

    Example
    -------
    plot_hist_dnbr_l8(landsat_dnbr_11, "March 2nd, 2017 and Novemeber 16th, 2018", 
                landsat_dnbr_06, "March 2nd, 2017 and June 25th, 2018")
    """
    fig,  (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    sns.set(font_scale=1.0)

    ax1.hist(dnbr1.ravel(), bins=[-.99, -.5, -.2,
                                  0, .2, .5, 1], color="purple")
    ax1.set(title="Landsat 8 Derived dNBR Histogram \n" + date1)

    ax2.hist(dnbr2.ravel(), bins=[-.99, -.5, -.2,
                                  0, .2, .5, 1], color="purple")
    ax2.set(title="Landsat 8 Derived dNBR Histogram \n" + date2)

    if bool is not None:
        fig.savefig("data/group/outputs/figs/landsat_hist_dNBR_" +
                    date1 + date2 + ".png")