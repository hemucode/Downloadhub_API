#!/usr/bin/env python3
import glob
import os,sys
import time
from datetime import datetime
from PIL import Image

try:
    IMG_FILE_NAME_WEBP = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.webp'])
    print("IMAGE RESIZE AND CONVERT........")
    print("")
    File_NAME= input("IMAGE NAME: ")
    while not File_NAME:
        print("\n[-] You must enter a IMAGE NAME at least!")
        File_NAME = input("EDIT  MOVIES IMAGE NAME: ")
    img = Image.open(File_NAME)
    # img.show()
    img_resized = img.resize((113, 169), Image.Resampling.LANCZOS)
    image = img_resized.convert('RGB')
    image.save('../edit_images/'+ IMG_FILE_NAME_WEBP, format='webp')
    time.sleep(2)
    
except Exception as e:   
    print("ERROR FROM FILE") 
    print(e)

	