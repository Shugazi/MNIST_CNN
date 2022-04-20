# loading the mnist dataset
from tensorflow.keras.datasets import mnist
from matplotlib import pyplot as plt
#  load the dataset
(trainX, trainY), (testX,testY) = mnist.load_data()
#  sumarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, y=%s' % (testX.shape, testY.shape))
