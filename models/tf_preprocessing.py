import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as mplt
import idx2numpy
import pickle

def convert_idx_to_array(data):
    return idx2numpy.convert_from_file(data)

def convert_labels(num,labels):
    return [i==num for i in labels]

def flatten_img(img):
    return img.reshape(img.shape[0], img.shape[1]*img.shape[2])

train_img = convert_idx_to_array('../data/train_images')
train_labels = convert_idx_to_array('../data/train_labels') 
test_img = convert_idx_to_array('../data/test_images')
test_labels = convert_idx_to_array('../data/test_labels')
