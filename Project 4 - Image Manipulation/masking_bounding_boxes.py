import glob
import os
import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.patches as patches


def get_data():
    """Simple wrapper function to get data"""
    with open('data/ground_truth.json') as f:
        ground_truth = json.load(f)
    return ground_truth


def create_mask(path, color_threshold):
    """
    Create a binary mask of an image using a color threshold
    Args:
        path [str]: path to image file
        color_threshold [array]: 1x3 array of RGB value
    Returns:
        img [array]: RGB image array
        mask [array]: binary array
    """
    img = np.array(Image.open(path).convert('RGB'))
    R, G, B = img[..., 0], img[..., 1], img[..., 2]
    rt, gt, bt = color_threshold
    mask = (R > rt) & (G > gt) & (B > bt)
    return img, mask

def draw_bb(ax, cl, bb, colormap, class_labels):
    y1, x1, y2, x2 = bb
    rec = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, facecolor='none',
                            edgecolor=colormap[cl], label='Ground Truth')
    ax.add_patch(rec)
    ax.text(x1, y1, class_labels[cl], color='white', fontsize=8,
            bbox=dict(facecolor=colormap[cl], edgecolor=colormap[cl], pad=0, alpha=0.7))

def mask_and_display(img, mask, save_path, save=False, show=False):
    """
    Display 3 plots next to each other: image, mask and masked image
    and save the masked image
    Args:
        img [array]: HxWxC image array
        mask [array]: HxW mask array
        save_path [str]: path to save the masked image
    """
    gtdic = {}
    for gt in ground_truth:
        gtdic[gt['filename']] = gt

    # Color mapping of classes
    colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}
    class_labels = {2: 'Pedestrian', 1: 'Vehicle', 4: 'Prediction'}

    masked_image = img * np.stack([mask] * 3, axis=2)
    fig, ax = plt.subplots(1, 3, figsize=(15, 10))
    ax[0].imshow(img)
    ax[0].set_title('Original RGB Image')
    ax[1].imshow(mask)
    ax[1].set_title('The binary mask')
    ax[2].imshow(masked_image)
    ax[2].set_title('The masked RGB Image')

    # Draw bounding boxes
    filename = os.path.basename(save_path)
    if filename in gtdic:
        bboxes = gtdic[filename]['boxes']
        classes = gtdic[filename]['classes']
        for cl, bb in zip(classes, bboxes):
            [draw_bb(ax[i], cl, bb, colormap, class_labels) for i in range(0,3)]
            

    # Save the masked image
    if save:
        plt.savefig(save_path)
    if show:
        plt.show()


if __name__ == '__main__':
    directory = './data/images/*.png'
    color_threshold = [128, 128, 128]
    output_directory = './data/output'
    ground_truth = get_data()

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
