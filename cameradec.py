import numpy as np
import sys
import tensorflow as tf
import time
import cv2
size = (150, 150)
cam = cv2.VideoCapture(2)
  
# reading the input using the camera
input("click enter to take a picture for classification: ")
result, img = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    cv2.imwrite("picture.jpg", img)
model = tf.keras.models.load_model(sys.argv[1])
img = cv2.imread("picture.jpg")
print(img.shape)
classification = model.predict(
            #[np.array(img).reshape(1, 150, 150, 3)]
            cv2.resize(img, (150, 150)).reshape(1, 150, 150, 3)
)
decision = classification.argmax()
if decision == 0:
    print("You can come in!")
else:
    print("Please wear a mask!")