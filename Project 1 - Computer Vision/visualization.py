import argparse
import glob
import json
import os

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image

from utils import get_data


def viz(ground_truth: list[dict], predictions: list[dict], labels: bool) -> None:
    """
    Create a grid visualization of images with color coded bboxes
    
    Args:
        ground_truth [list[dict]]: ground truth data
        predictions [list[dict]]: prediction data
        labels [bool]: flag to show labels (default: True)
    """
    paths = glob.glob('./data/images/*')
    print(labels)
    # mapping to access data faster
    gtdic = {}
    for gt in ground_truth:
        gtdic[gt['filename']] = gt

    pdic = {}
    for pred in predictions:
        pdic[pred['filename']] = pred

    # color mapping of classes
    colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}
    class_labels = {2: 'Pedestrian', 1: 'Vehicle', 4: 'Prediction'}

    f, ax = plt.subplots(4, 5, figsize=(20, 10))
    for i in range(20):
        x = i % 4
        y = i % 5

        filename = os.path.basename(paths[i])
        img = Image.open(paths[i])
        ax[x, y].imshow(img)

        # Ground Truth
        if filename in gtdic:
            bboxes = gtdic[filename]['boxes']
            classes = gtdic[filename]['classes']
            for cl, bb in zip(classes, bboxes):
                y1, x1, y2, x2 = bb
                rec = Rectangle((x1, y1), x2 - x1, y2 - y1, facecolor='none',
                                edgecolor=colormap[cl], label='Ground Truth')
                ax[x, y].add_patch(rec)
                if labels:
                    ax[x, y].text(x1, y1, class_labels[cl],
                                color='white', fontsize=8,
                                bbox=dict(facecolor=colormap[cl], edgecolor=colormap[cl], pad=0, alpha=0.7))

        # Predictions
        if filename in pdic:
            pred_bboxes = pdic[filename]['boxes']
            pred_classes = pdic[filename]['classes']
            for cl, bb in zip(pred_classes, pred_bboxes):
                y1, x1, y2, x2 = bb
                rec = Rectangle((x1, y1), x2 - x1, y2 - y1, facecolor='none',
                                edgecolor='yellow', label='Prediction')
                ax[x, y].add_patch(rec)
                
                if labels:
                    ax[x, y].text(x1, y1, class_labels[cl],
                                color='black', fontsize=8,
                                bbox=dict(facecolor='yellow', edgecolor='yellow', pad=0, alpha=0.7))


        ax[x, y].axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize ground truth and predictions')
    parser.add_argument('--labels', type=str, default='True',
                        help='Flag to show labels (True or False)')
    args = parser.parse_args()
    
    labels: bool = args.labels.lower() == 'true'
    
    ground_truth, predictions = get_data()
    viz(ground_truth, predictions, labels)
