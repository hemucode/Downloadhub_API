#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re

try:
    print("run")
    MOVIES_NAME = "batman"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    IMDB_URL = "https://www.needevery.in/2022/11/last-film-show-2022-hindi-movie.html"
    IMDB_DATA = requests.get(IMDB_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
    IMDB_SOUP = BeautifulSoup(IMDB_DATA, "html.parser")
    # IMDB_CONTENT = IMDB_SOUP.fin    d('div',class_="kCrYT").a['href']
    print(IMDB_SOUP)
    # for a in IMDB_SOUP.find_all('a', href=True):
    #     print ("Found the URL:", a['href'])


    # if IMDB_CONTENT:    
    #     for data in IMDB_CONTENT:
    #         ALL_CONTENT = (data.href())
    #         MOVIES_BODY = re.sub(r' +', ' ', ALL_CONTENT).replace('\n ','').replace('\n','').replace(r'\r','\t')
    #         print(MOVIES_BODY)



        


    # if NEWS_CONTENT:    
    #     CONTENT_1 = NEWS_CONTENT.find_all('div')[0].text
    #     CONTENT_2 = NEWS_CONTENT.find_all('div')[1].text
    #     CONTENT_3 = NEWS_CONTENT.find_all('div')[2].text
    #     print(CONTENT_1+CONTENT_1+CONTENT_3)


            # print(MOVIES_BODY)

    # POST_FILE = 'post.json'
    # with open(POST_FILE) as POST_DATA:
    #     POST = json.load(POST_DATA)

    # DATA_FILE = 'data.json'
    # with open(DATA_FILE) as MAIN_DATA:
    #     DATA = json.load(MAIN_DATA)
        
    # TAG = "movies"
    # TAG_1 = " download"
    # TAG_2 = " 300mb download"
    # TAG_3 = " 480p download"
    # TAG_4 = " 720p download"
    # TAG_5 = " 1024p download"


    # LABELS_1 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'])

    # LABELS_2 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'])

    # LABELS_3 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'])

    # LABELS_4 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'+","+POST['MOVIES_NAME'].lower()+' 720p download'])

    # LABELS_5 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'+","+POST['MOVIES_NAME'].lower()+' 720p download'+","+POST['MOVIES_NAME'].lower()+' 1080p download'])

    # NUMBER_OF_LABELS_1 = len(re.sub("[^a-zA-Z]", "", LABELS_1))
    # NUMBER_OF_LABELS_2 = len(re.sub("[^a-zA-Z]", "", LABELS_2))
    # NUMBER_OF_LABELS_3 = len(re.sub("[^a-zA-Z]", "", LABELS_3))
    # NUMBER_OF_LABELS_4 = len(re.sub("[^a-zA-Z]", "", LABELS_4))
    # NUMBER_OF_LABELS_5 = len(re.sub("[^a-zA-Z]", "", LABELS_5))

    # if NUMBER_OF_LABELS_1<=160:
    #     LABELS = LABELS_1
    # if NUMBER_OF_LABELS_2<=160:
    #     LABELS = LABELS_2
    # if NUMBER_OF_LABELS_3<=160:
    #     LABELS = LABELS_3
    # if NUMBER_OF_LABELS_4<=160:
    #     LABELS = LABELS_4
    # if NUMBER_OF_LABELS_5<=160:
    #     LABELS = LABELS_5


    # print(LABELS)
    # a = LABELS.split()



    # with open('C:/data.txt', 'r') as textfile:
    #     lines = list(textfile)
    # words_all = sum([len(line.split()) for line in lines])
    # print ('Total words:   ', words_all)

except Exception as e:   
    print("ERROR FROM FILE NAME upload.py: ") 
    print('pip install --upgrade google-api-python-client') 
    print(e)

	