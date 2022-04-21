# loading the mnist dataset
from tensorflow.keras.datasets import mnist
from matplotlib import pyplot as plt
#  load the dataset
(trainX, trainY), (testX,testY) = mnist.load_data()
#  summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, y=%s' % (testX.shape, testY.shape))

#  Plotting the images
for i in range(9):
    #defining subplot
    plt.subplot(330 + 1 + i)
    #plot raw pixel data
    plt.imshow(trainX[i], cmap=plt.get_cmap("gray"))
# show the figure
plt.show()
