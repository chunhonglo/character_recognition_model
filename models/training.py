from sklearn.linear_model import LogisticRegression
from preprocessing import *
import pickle


train_img = convert_idx_to_array('../data/train_images')
train_labels = convert_idx_to_array('../data/train_labels')
test_img = convert_idx_to_array('../data/test_images')
test_labels = convert_idx_to_array('../data/test_labels')

train_labels = convert_labels(5,train_labels)
test_labels = convert_labels(5,test_labels)

train_img = flatten_img(train_img)
test_img = flatten_img(test_img)

logreg = LogisticRegression()
logreg.fit(train_img, train_labels)

filename = 'logistic_regression_model.sav'
pickle.dump(logreg, open(filename, 'wb'))


