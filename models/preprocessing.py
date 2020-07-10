import idx2numpy
import numpy as np

def convert_idx_to_array(data):
    return idx2numpy.convert_from_file(data)

def convert_labels(num,labels):
    return [i==num for i in labels]

def flatten_img(img):
    return img.reshape(img.shape[0], img.shape[1]*img.shape[2])




