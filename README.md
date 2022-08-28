# facial verification 
this facial verification app made for both  tensorflow and pytorch 

## how the app work 
the model we will train need positive images and negative images and anchor images so we will collect these data 


- first anchors and positive 
we will use cv2 to access our webcam and capture some images so the webcam_images.py will capture positive if you pressed  'p' in your keyboard and anchor if you pressed 'a'

```bash 
python scripts/webcam_images.py 
``` 

- the negative example 
you can use any random images but we will scrap some from the web so the get_negatives.py script will scrab some images and save them localy and you can change the url to the site you want to scrab 

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

----------------
tensorflow => you will open the tensorflow_model.ipynb notebook and run the cells to train the model and save it 

------------------
pytorch => you will open the pytorch_model.ipynb notebook and run the cells to train the model and save it 

- finally you will some inference 

---------------
you will use cv2 to do some inference 

tensorflow => you can run the tensorflow_inference script 
``` bash 
python scripts/tensorflow_inference.py 
``` 

----------------
pytorch =>  you can run the pytorch_inference script 
``` bash 
python scripts/pytorch_inference.py 
``` 