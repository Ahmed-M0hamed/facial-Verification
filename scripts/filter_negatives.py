import cv2
from numpy import imag 
import os 

images_path = os.path.join(os.getcwd(),'data', 'negative')

for file in os.listdir(images_path) : 
    if os.path.exists(os.path.join(images_path , file)) : 
        image = cv2.imread(os.path.join(images_path , file)) 
        # print(image.dtype)
        if (image.shape[0] < 300) & ( image.shape[1] < 450) : 
            
            os.remove(os.path.join(images_path , file))
    else : 
        os.remove(os.path.join(images_path , file))