#!/usr/bin/env python3
import os,sys,time,re;
import json
from datetime import datetime
import random
import subprocess
import requests
from bs4 import BeautifulSoup
import re
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



try:
    print("")
    MOVIES_NAME = POST['MOVIES_NAME']
    MOVIES_IMDB = input(WARNING +"ADD MOVIES IMDB URL: "+ CEND)
    POST['MOVIES_IMDB'] = MOVIES_IMDB
    json.dump(POST, open(POST_FILE, "w"), indent = 2)
    while not MOVIES_IMDB:
        print("\n[+]"+FAIL+" Are You Search Movies IMDB URL Google? OPTIONS : "+OKGREEN+"[y]YES"+CEND+" or "+OKBLUE+"[n]NO"+CEND+" or "+UNDERLINE + "[m]MANUAL" + CEND)
        print("")
        OPTIONS_MOVIES_IMDB = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
        if OPTIONS_MOVIES_IMDB =="y":
            IMDB_URL = "https://www.google.com/search?q="+MOVIES_NAME+"+movie+imdb"
            IMDB_DATA = requests.get(IMDB_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
            IMDB_SOUP = BeautifulSoup(IMDB_DATA, "html.parser")
            IMDB_CONTENT = IMDB_SOUP.find('div',class_="kCrYT").a['href']
            print(WARNING +IMDB_CONTENT +CEND)
            
        if OPTIONS_MOVIES_IMDB =="n":
            print("\n[-] You must enter a EDIT MOVIES RELEASE DATE at least!", file=sys.stderr)
            MOVIES_IMDB = input(WARNING +"ADD MOVIES IMDB URL: "+ CEND)
            POST['MOVIES_IMDB'] = MOVIES_IMDB
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
        
        if OPTIONS_MOVIES_IMDB =="m":
            POST['MOVIES_IMDB'] = "https://www.imdb.com/find?q=" + MOVIES_NAME
            json.dump(POST, open(POST_FILE, "w"), indent = 2)

        
        MOVIES_IMDB = input(WARNING +"ADD MOVIES IMDB URL: "+ CEND)
        POST['MOVIES_IMDB'] = MOVIES_IMDB
        json.dump(POST, open(POST_FILE, "w"), indent = 2)
        
except Exception as e:   
        print("SCANNIMG ERROR........")  
        print(e)


