import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import json

from Mask.config import Config
import Mask.utils as utils
import Mask.model as modellib
import Mask.visualize as visualize
from Mask.model import log

np.set_printoptions(threshold=np.inf)
dir_path = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = dir_path + "/models/"
# Example : "models/moles20180227T1422/mask_rcnn_moles_0030.h5"
MODEL_PATH = input(
    "Insert the path of your trained model [" + dir_path + "/]: ")

if os.path.isfile(MODEL_PATH) == False:
    raise Exception(MODEL_PATH + " Does not exists")



class CocoConfig(Config):
    NAME = "moles"
    NUM_CLASSES = 1 + 2
    IMAGE_MIN_DIM = 128
    IMAGE_MAX_DIM = 128
    DETECTION_MAX_INSTANCES = 3

class InferenceConfig(CocoConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()


model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
model.load_weights(MODEL_PATH, by_name=True)

class_names = ["BG", "malignant", "benign"]

for i in range(13786):
    num = str(i).zfill(5)
    img = cv2.imread(f"Data/Images/ISIC_00{num}.jpg")
    img = cv2.resize(img, (128, 128))

    data = json.load(open(f"Data/Descriptions/ISIC_00{num}"))

    print(data["meta"]["clinical"]["benign_malignant"])
    print(i)
    
    r = model.detect([img])[0]
    visualize.display_instances(img, r['rois'], r['masks'], r['class_ids'],
                                class_names, r['scores'])
