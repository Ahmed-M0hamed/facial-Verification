import cv2 
import uuid 
import os 

cap = cv2.VideoCapture(0) 
while cap.isOpened() : 
    _ , frame = cap.read()
    
    if cv2.waitKey(1) & 0XFF == ord('a'):
        cv2.imwrite(os.path.join(os.getcwd() , 'data' , 'anchors' , f'{str(uuid.uuid1())}.jpg') , frame)
    if cv2.waitKey(1) & 0XFF == ord('p'):
        cv2.imwrite(os.path.join(os.getcwd() , 'data' , 'positive' , f'{str(uuid.uuid1())}.jpg') , frame)
    cv2.imshow('Image Collection', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        

