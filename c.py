#!/usr/bin/env python3
import os,sys,time,re;
import json
from datetime import datetime
import random
import subprocess
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)
os.system('color')
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CRED = '\033[91m'
CEND = '\033[0m'


IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
IMG_FILE_NAME_WEBP = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.webp'])
TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



try:
    print("")
    AAA = "https://img1.hotstarext.com/image/upload/f_auto,t_web_vl_3x/sources/r1/cms/prod/372/1420372-v-c4dc9b7e307f"
    img = requests.get(AAA,headers=headers)
    with open('images/' + IMG_FILE_NAME, 'wb') as imgf:
        imgf.write(img.content)
    print('\033[93m'+"[+] IMAGE RESIZE AND CONVERT........" +'\033[0m')
    time.sleep(2)
    print("")
    img = Image.open('images/' + IMG_FILE_NAME)
    # img.show()
    img_resized = img.resize((113, 169), Image.Resampling.LANCZOS)
    image = img_resized.convert('RGB')
    image.save('edit_images/'+ IMG_FILE_NAME_WEBP, format='webp')
    
except Exception as e:   
        print("SCANNIMG ERROR........")  
        print(e)


