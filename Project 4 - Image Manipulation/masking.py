import glob, os
import time
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def create_mask(path, color_threshold):
    """
    create a binary mask of an image using a color threshold
    args:
    - path [str]: path to image file
    - color_threshold [array]: 1x3 array of RGB value
    returns:
    - img [array]: RGB image array
    - mask [array]: binary array
    """
    img = np.array(Image.open(path).convert('RGB'))
    R, G, B = img[..., 0], img[..., 1], img[..., 2]
    rt, gt, bt = color_threshold
    mask = (R > rt) & (G > gt) & (B > bt)
    return img, mask


def mask_and_display(img, mask, save_path, save=False, show=False):
    """
    display 3 plots next to each other: image, mask and masked image
    and save the masked image
    args:
    - img [array]: HxWxC image array
    - mask [array]: HxW mask array
    - save_path [str]: path to save the masked image
    """
    masked_image = img * np.stack([mask]*3, axis=2)
    f, ax = plt.subplots(1, 3, figsize=(15, 10))
    ax[0].imshow(img)
    ax[0].set_title('Original RGB Image')
    ax[1].imshow(mask)
    ax[1].set_title('The binary mask')
    ax[2].imshow(masked_image)
    ax[2].set_title('The masked RGB Image')

    # Save the masked image
    if save:
        plt.savefig(save_path)
    if show:
        plt.show()


if __name__ == '__main__':
    directory = './data/images/*.png'
    color_threshold = [128, 128, 128]
    output_directory = './data/output'
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get the list of image files in the directory
    file_list = glob.glob(directory)

    # Iterate over the files and process each image
    for file_path in file_list:
        # Generate the mask and display the image
        img, mask = create_mask(file_path, color_threshold)

        # Generate the save path for the masked image
        file_name = os.path.basename(file_path)
        save_path = os.path.join(output_directory, file_name)

        # Mask and display the image, and save the masked image
        mask_and_display(img=img, mask=mask, save_path=save_path, save=False, show=True)