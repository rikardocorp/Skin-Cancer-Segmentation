# Skin-Cancer-Segmentation
Classification and Segmentation with Mark-RCNN of Skin Cancer by ISIC dataset 

## Setup

1) Download the dataset from https://isic-archive.com/ 
    - You can download it with : python3 download_dataset.py

2) python3 create_dataset.py : to get the numpy format of the image and the mask

3) python3 main.py : to create the model 
    - You also have to download the Coco Model, that you can find here: 
    https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5

4) python3 test.py : to test the model

## Results

Original image

<img src="https://github.com/0x5eba/Skin-Cancer-Segmentation/blob/master/Nei/git.png" width="200" height="200">

Classify and Segment image

<img src="https://github.com/0x5eba/Skin-Cancer-Segmentation/blob/master/Nei/gitres.png" width="400" height="400">
