# facial verification 
this facial verification app made with tensorflow and cv2 

## how the app work 
the model we will train need positive images and negative images and anchor images to compare each 
of the positive and negative with so we will collect these data 

- first anchors and positive 
we will use cv2 to access our webcam and capture some images so the webcam_images.py will do that 

```bash 
python scripts/webcam_images.py 
``` 

- the negative example 
you can use and images but we will scrap some from the web so the get_negatives.py script will do it 
```bash 
python scripts/get_negatives.py 
``` 

- filter the negatives 
you will need to filter some of the unsuitalble images in the negatives with the filter negatives.py script
``` bash 
python scripts/filter_images.py
``` 

- augment the data 
run the augment.py script to augment the data you collected 
``` bash 
python scripts/augment.py
``` 
- train the model 
the data is ready we will start to train the model 
you will open the facial-verification notebook and run the cell to train the model and save it 

- finally you will some inference 
you will use cv2 to do some inference with inference.py script 

``` bash 
python scripts/inference.py
``` 