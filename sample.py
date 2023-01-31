import numpy as np
import cv2
import os


from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

# Load data and preprocess it
faces = []
labels = []

for filename in os.listdir('./Image'):
    label = int(filename.split('.')[0].replace('subject',''))
    image = cv2.imread('./Image/' + filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces.append(image)
    labels.append(label)

faces = np.array(faces)
labels = np.array(labels)

# Normalize data
faces = faces / 255.0

# Reshape data to fit model input
faces = faces.reshape(-1, 48, 48, 1)

# Create the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(40, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(faces, labels, epochs=10)