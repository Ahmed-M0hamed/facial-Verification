import tensorflow as tf 
import cv2 
import os 
import random
import numpy as np 
from yaml import AnchorToken 

# load th emodel 
model = tf.keras.models.load_model(os.path.join(os.getcwd() , 'model_1')) 
cap = cv2.VideoCapture(0 ) 

# the preprocess function for the images 
def preprocess(img_path ) : 
    img = tf.io.read_file(img_path ) 
    img = tf.io.decode_jpeg(img) 
    img = tf.image.resize(img ,(100, 100)) 
    return img 


    
# we will select 5 random anchor images 
# we will pass each of them with the captured image to the model to predict 
# we will take the mean and compare it to threshold 
def predict(model , frame , detection_threshold   ) : 
    
    images_paths = os.listdir(os.path.join(os.getcwd() , 'data' , 'anchors'))
    random_indexs = [random.randrange(1, len(images_paths), 1) for i in range(5)]
    anchors  = [os.path.join(os.getcwd() , 'data' , 'anchors' , img_path) for i , img_path  in enumerate(images_paths) for ii in random_indexs if i == ii  ]
    preds = []
    frame_img = tf.image.resize(frame , (100 , 100))
    for anchor in anchors  : 
        anchor = preprocess(anchor) 
        pred  = model.predict(list(np.expand_dims([anchor, frame_img], axis=1)))
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