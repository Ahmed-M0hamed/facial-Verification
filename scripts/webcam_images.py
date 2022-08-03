import cv2 
import uuid 
import os 


cap = cv2.VideoCapture(0) 
while cap.isOpened() : 
    _ , frame = cap.read()
    # append to anchors dir if you press a 
    if cv2.waitKey(1) & 0XFF == ord('a'):
        cv2.imwrite(os.path.join(os.getcwd() , 'data' , 'anchors' , f'{str(uuid.uuid1())}.jpg') , frame)
    # append to positive dir if you press p
    if cv2.waitKey(1) & 0XFF == ord('p'):
        cv2.imwrite(os.path.join(os.getcwd() , 'data' , 'positive' , f'{str(uuid.uuid1())}.jpg') , frame)
    cv2.imshow('Image Collection', frame)
    # break the loop if you press q
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        

