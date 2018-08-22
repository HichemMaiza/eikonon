import numpy as np

from keras.preprocessing.image import ImageDataGenerator 

X_train, Y_train = np.load("X.npy"), np.load("Y.npy") 


datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True) 

batches = 0
for x_batch, y_batch in datagen.flow(X_train, Y_train, batch_size = 1, save_to_dir = './augmented_data') :
    batches += 1
    if batches >= 5*len(X_train) / 1:
        break 
    