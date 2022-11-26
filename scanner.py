#!/usr/bin/env python3
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
import re
import subprocess


try:
    IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
    TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as MAIN_DATA:
        DATA = json.load(MAIN_DATA)
    NUMBER = DATA['STATUS']

    if NUMBER ==1:   
        #Requests FROM NEW Sitemap URL 
        SITEMAP_URL = DATA['SITEMAP']
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        NEWS_DATA = requests.get(SITEMAP_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
        NEWS_SOUP = BeautifulSoup(NEWS_DATA, "xml")
        # print(NEWS_SOUP)

        SEANN_NO_OF_URL = DATA['SEANN_NO_OF_URL']
        NEW_URL = NEWS_SOUP.findAll('loc')[SEANN_NO_OF_URL].text
        # print(NEW_URL)

        if NEW_URL:
            # DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL +1
            MOVIES_DATA = requests.get(NEW_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
            MOVIES_SOUP = BeautifulSoup(MOVIES_DATA, "xml")
            MOVIES_TITLE = MOVIES_SOUP.findAll('span', class_="material-text")[0].text
            MOVIES_TITLE_PURE = re.sub(r' +', ' ', MOVIES_TITLE).replace('\n ','').replace('\n','')
            # print(MOVIES_TITLE_PURE)

            NEWS_CONTENT = MOVIES_SOUP.find('main',class_="page-body")


            if NEWS_CONTENT:    
                with open("content/" + TEXT_FILE_NAME, "a") as out_file:
                    CONTENT_1 = NEWS_CONTENT.find_all('p')[0]
                    CONTENT_2 = NEWS_CONTENT.find_all('p')[2]
                    CONTENT_3 = NEWS_CONTENT.find_all('p')[3]
                    data = ''
                    for data in CONTENT_1,CONTENT_2,CONTENT_3:
                        ALL_CONTENT = (data.get_text())
                        # print(ALL_CONTENT)
                        MOVIES_BODY = re.sub(r' +', ' ', ALL_CONTENT).replace('\n ','').replace('\n','')
                        out_file.writelines(data for data in MOVIES_BODY)
                        # print(MOVIES_BODY)
            
            NEWS_IMG = NEWS_CONTENT.find_all('p')[1]
            # print(NEWS_IMG)
            if NEWS_IMG :
                DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
                img = requests.get(NEWS_IMG.img['src'],headers=headers)
                with open('images/' + IMG_FILE_NAME, 'wb') as imgf:
                    imgf.write(img.content)            
            else:
                print("IMAGES NOT FOUND!")
                DATA['IMAGES'] = ""
                
            DATA['STATUS'] = 2  
            DATA['MOVIES_DEATILS'] = "content/" + TEXT_FILE_NAME
            DATA['MOVIES_TITLE'] =  MOVIES_TITLE_PURE
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)

        else:
            DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL +1
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
        
        if NEWS_IMG and NEWS_CONTENT and MOVIES_TITLE:
            OPEN2 = 'python edit.py'
            subprocess.Popen(OPEN2, shell=True)
    else:

        subprocess.Popen('python edit.py', shell=True)

except Exception as e:   
        print("ERROR: scanner.py")  
        print(e)
