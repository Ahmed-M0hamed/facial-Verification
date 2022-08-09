from functools import total_ordering
from cv2 import transform
import torch 
from torch import nn 
import cv2 
import os 
from torchvision.transforms import Resize ,ToTensor
from torchvision.io import read_image
import random
import numpy as np 
from pytorch_model import Model  , embedding , L1Dist

model = Model()
model = torch.load(os.path.join(os.getcwd() , 'pytorch_model.pt'))
model.eval()

cap = cv2.VideoCapture(0 ) 

# the preprocess function for the images 
def preprocess(img_path ) : 
    img = read_image(img_path ) 
    resize = Resize((100 , 100))
    img = resize(img) 
    img = img / 255. 
    return img 


    
# we will select 5 random anchor images 
# we will pass each of them with the captured image to the model to predict 
# we will take the mean and compare it to threshold 
def predict(model , frame , detection_threshold   ) : 
    
    images_paths = os.listdir(os.path.join(os.getcwd() , 'data' , 'anchors'))
    random_indexs = [random.randrange(1, len(images_paths), 1) for i in range(5)]
    anchors  = [os.path.join(os.getcwd() , 'data' , 'anchors' , img_path) for i , img_path  in enumerate(images_paths) for ii in random_indexs if i == ii  ]
    preds = []
    transform = ToTensor() 
    frame_img = transform(frame)
    resize = Resize((100 , 100))
    frame_img = resize(frame_img )
    frame_img  = frame_img.reshape((3 , 100 , 100))
    frame_img = frame_img / 255. 
    for anchor in anchors  : 
        anchor = preprocess(anchor) 
        with torch.inference_mode() : 
            pred  = model(anchor.unsqueeze(0) , frame_img.unsqueeze(0))
            preds.append(pred)
    detection = np.sum(np.array(preds) > detection_threshold)
    score = detection  / 5 
    return preds , score 

    
while cap.isOpened() : 
    _ , frame = cap.read() 
    cv2.imshow('Verification', frame)
    if cv2.waitKey(1) & 0XFF == ord('v') : 
        preds , score =  predict(model , frame , .8 )
        verified  = score > .8 
        print(verified)
        
    if cv2.waitKey(1) & 0XFF == ord('q') : 
        break 
cap.release()
cv2.destroyAllWindows()