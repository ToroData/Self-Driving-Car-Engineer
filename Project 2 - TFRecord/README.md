# Waymo Open Dataset to TensorFlow Object Detection API TFRecord Converter


<div align="center">
    <img src="https://thedatascientist.digital/img/logo.png" alt="Logo" width="25%">
</div>


This project aims to familiarize you with the TFRecord format by converting data from the Waymo Open Dataset into the TFRecord format used by the TensorFlow Object Detection API. As a Machine Learning Engineer, you will frequently encounter the need to convert datasets from one format to another, and this exercise provides an excellent opportunity to practice such tasks.

## Objective

The objective of this exercise is to convert the Waymo Open Dataset data into the TFRecord format used by the TensorFlow Object Detection API. By completing this exercise, you will gain familiarity with the TFRecord format and the process of converting data from one format to another.

## Details

The Waymo Open Dataset consists of TFRecord files containing data from car trips. Each TFRecord file contains images from different cameras and LIDAR data. In this exercise, we focus on implementing the create_tf_example function to generate cleaned TFRecord files to keep the dataset size manageable.

To parse the raw TFRecord files, we utilize the Waymo Open Dataset GitHub repository. It is recommended to refer to the Waymo Open Dataset tutorial to gain a better understanding of the data format before proceeding with this exercise.

## Tips

To better comprehend the dataset structure, consult the Waymo Open Dataset documentation.

In future stages, we will leverage the TensorFlow Object Detection API to train object detection models. The API tutorial provides an example of the create_tf_example function, which can be found here.

Please note that running the code requires using the example .tfrecord file provided in the  directory.

## Setup Instructions

To execute the code and perform the Waymo Open Dataset to TensorFlow Object Detection API TFRecord conversion, follow these steps:



1. Install the required dependencies: TensorFlow 1.15.0, Pillow, and Waymo Open Dataset. You can install them using the following commands:

    ```{Bash}
    pip install tensorflow==1.15.0
    pip install Pillow
    pip install waymo-open-dataset==1.2.0

    ```
2. Clone the Waymo Open Dataset repository from GitHub by running the following command:

    ```{Bash}
    git clone https://github.com/waymo-research/waymo-open-dataset.git

    ```

3. Follow the instructions in the Waymo Open Dataset tutorial to download the dataset and obtain the necessary access credentials.

4. Once you have the dataset downloaded and the access credentials set up, navigate to the waymo-open-dataset directory and locate the convert.py script.

5. Open a terminal or command prompt in the same directory as the convert.py script.

6. Execute the following command to run the script and convert the Waymo Open Dataset TFRecord file into the TensorFlow Object Detection API TFRecord format:
    ```{Bash}
    python convert.py -p path/to/waymo.tfrecord

    ```
Replace path/to/waymo.tfrecord with the actual path to your Waymo Open Dataset TFRecord file.

    Note: Ensure that you have read and write permissions in the specified directories.

7. The script will process the TFRecord file and generate a new TFRecord file compatible with the TensorFlow Object Detection API. The output file will be saved in the output directory.

By following these instructions, you will successfully convert the Waymo Open Dataset into the TFRecord format required by the TensorFlow Object Detection API. This will allow you to further utilize the dataset for training object detection models.

## Conclusion

The Autonomous Driving System Showcase repository encapsulates our expertise, groundbreaking achievements, and the remarkable capabilities of our self-driving car system. We invite you to delve into the code, explore the various modules, and witness the future of autonomous driving. Get ready to be amazed!