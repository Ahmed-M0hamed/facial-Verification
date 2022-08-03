from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import os 
import uuid

urls = []
# urls the the sites you will scrap from 
target_sites  = ['https://unsplash.com/s/photos/human?orientation=landscape' , 'https://unsplash.com/s/photos/portrait?orientation=landscape' , 'https://unsplash.com/s/photos/person?orientation=landscape']
for site in target_sites : 
    htmldata = urlopen(site)
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    site_urls = [image['src'] for image in images] 
    urls += site_urls
    
# get the unique urls 
urls_set = set(urls) 
print(len(urls_set))

# save the images 
for url in urls_set :
    urllib.request.urlretrieve(url ,os.path.join(os.getcwd() , 'data' , 'negative' , f'{str(uuid.uuid1())}.jpg') ) 