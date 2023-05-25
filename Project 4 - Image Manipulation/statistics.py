import glob
import logging

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image, ImageStat

from utils import check_results

# Configure registration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def calculate_mean_std(image_list):
    """
    calculate mean and std of image list
    args:
    - image_list [list[str]]: list of image paths
    returns:
    - mean [array]: 1x3 array of float, channel wise mean
    - std [array]: 1x3 array of float, channel wise std
    """
    logger.info("Calculating mean and standard deviation...")
    means = []
    stds = []
    logger.info(f"Processing images")
    for path in image_list:
        img = Image.open(path).convert('RGB')
        stat = ImageStat.Stat(img)
        means.append(np.array(stat.mean))
        stds.append(np.array(stat.var)**0.5)
    
    total_mean = np.mean(means, axis=0)
    total_std = np.mean(stds, axis=0)
    
    logger.info("Mean and standard deviation calculation completed.")
    return total_mean, total_std


def channel_histogram(image_list):
    """
    calculate channel wise pixel value
    args:
    - image_list [list[str]]: list of image paths
    """
    logger.info("Generating channel-wise histograms...")
    red = []
    green = []
    blue = []
    logger.debug(f"Processing images")
    for path in image_list:
        img = np.array(Image.open(path).convert('RGB'))
        R, G, B = img[..., 0], img[..., 1], img[..., 2]
        red.extend(R.flatten().tolist())
        green.extend(G.flatten().tolist())
        blue.extend(B.flatten().tolist())
    
    plt.figure()
    sns.kdeplot(red, color='r')
    sns.kdeplot(green, color='g')
    sns.kdeplot(blue, color='b')
    plt.show()
    
    logger.info("Channel-wise histograms generation completed.")


if __name__ == "__main__":
    logger.info("Starting the program...")
    image_list = glob.glob('./data/images/*')

    # Calculate mean and standard deviation
    mean, std = calculate_mean_std(image_list)
    logger.info(f"Mean: {mean}")
    logger.info(f"Standard Deviation: {std}")

    # Generate channel-wise histograms
    # channel_histogram(image_list[:2])

    # Check results
    check_results(mean, std)

    logger.info("Program completed.")
