#!/usr/bin/env python3
import os,sys,time,re;
import json
from datetime import datetime
import subprocess
import requests
from bs4 import BeautifulSoup
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
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


DATA_FILE = 'data.json'
POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)
    
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)

DATA['AUTO'] == 0
json.dump(DATA, open(DATA_FILE, "w"), indent = 2)

NUMBER = 2
IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
IMG_FILE_NAME_WEBP = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.webp'])
TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])
print("")

def MAIN_INPUT():
    MOVIES_NAME = input(WARNING +"[+] EDIT MOVIES NAME: "+ CEND)
    while not MOVIES_NAME:
        print("")
        MOVIES_NAME = input(WARNING +"[+] EDIT MOVIES NAME: "+ CEND)
                
    print("")
    print("\n[+]"+FAIL+" Select Types of Movies? OPTIONS : "+OKGREEN+"[e]English"+CEND+" or "+OKBLUE+"[p]Punjabi"+CEND+" or "+OKGREEN+"[h]Hindi Dual Audio"+CEND+" or "+OKBLUE+"[a]All Season"+CEND+" or "+OKGREEN+"[b]Bangla movie"+CEND+" or "+OKGREEN+"[d]Hindi Dubbed"+CEND+" or "+OKBLUE+"[n]Normal Language"+CEND+" or "+OKGREEN+"[m]Malayalam"+CEND)
    print("")
    MOVIES_TYPES = input(WARNING +"[+] PRESS MOVIES TYPES: "+ CEND)
    while not MOVIES_TYPES:
        print("")
        MOVIES_TYPES = input(WARNING +"[+] PRESS MOVIES TYPES: "+ CEND)
    if MOVIES_TYPES == "e":
        MOVIES_TYPES_DATA = " English Movie"
    if MOVIES_TYPES == "p":
        MOVIES_TYPES_DATA = " Punjabi Movie"
    if MOVIES_TYPES == "h":
        MOVIES_TYPES_DATA = " Hindi Dual Audio Movie"
    if MOVIES_TYPES == "a":
        MOVIES_TYPES_DATA = " All Season"
    if MOVIES_TYPES == "b":
        MOVIES_TYPES_DATA = " Bengali/Bangla movie"
    if MOVIES_TYPES == "d":
        MOVIES_TYPES_DATA = " hindi dubbed movie"
    if MOVIES_TYPES == "n":
        MOVIES_TYPES_DATA = " movie"
    if MOVIES_TYPES == "m":
        MOVIES_TYPES_DATA = " Malayalam movie"
                
    print("")
    DATA['MOVIES_TITLE'] =  MOVIES_NAME + MOVIES_TYPES_DATA 
    json.dump(DATA, open(DATA_FILE, "w"), indent = 2)

    MOVIES_NAME_MIX = input(WARNING +"[+] EDIT MOVIES NAME MIX: "+ CEND)
    while not MOVIES_NAME_MIX:
        print("\n[-] You must enter a MOVIES NAME  MIX at least!", file=sys.stderr)
        MOVIES_NAME_MIX = input("[+] EDIT  MOVIES NAME MIX: ")

    print("")

    MOVIES_STORY = input(WARNING +"[+] ADD MOVIES STORY: "+ CEND)
    while not MOVIES_STORY:
        print("\n[-] You must enter a MOVIES  STORY at least!", file=sys.stderr)
        MOVIES_STORY = input("[+] ADD MOVIES _STORY: ")

    
    POST['MOVIES_NAME'] = MOVIES_NAME
    POST['MOVIES_NAME_MIX'] = MOVIES_NAME_MIX
    POST['MOVIES_STORY'] = MOVIES_STORY
    json.dump(POST, open(POST_FILE, "w"), indent = 2)


def IMAGE_INPUT():
    print("")
    MOVIES_IMG_URL = input(WARNING +"[+] MOVIES IMG URL: "+ CEND)
    while not MOVIES_IMG_URL:
        print("")
        MOVIES_IMG_URL = input(WARNING +"[+] MOVIES IMG URL: "+ CEND)

    DATA['IMAGES'] = 'images/' + IMG_FILE_NAME
    img = requests.get(MOVIES_IMG_URL,headers=headers)
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


    MOVIES_IMG = input(WARNING +"[+] ADD MOVIES IMG BY BLOGGER: "+ CEND)
    while not MOVIES_IMG:
        print("\n[-] You must enter a MOVIES IMG at least!", file=sys.stderr)
        print("")
        MOVIES_IMG = input(WARNING +"[+] ADD MOVIES IMG BY BLOGGER: "+ CEND)
        if not MOVIES_IMG:
            subprocess.Popen('python input.py', shell=True)
            exit()
    POST['MOVIES_IMG'] = MOVIES_IMG
    json.dump(POST, open(POST_FILE, "w"), indent = 2)


def IMDB_INPUT():
    print("")
    MOVIES_NAME = POST['MOVIES_NAME']
    MOVIES_IMDB = input(WARNING +"[+] ADD MOVIES IMDB URL: "+ CEND)
    POST['MOVIES_IMDB'] = MOVIES_IMDB
    json.dump(POST, open(POST_FILE, "w"), indent = 2)
    while not MOVIES_IMDB:
        print("\n[+]"+FAIL+" Are You Search Movies IMDB URL Google? OPTIONS : "+OKGREEN+"[y]YES"+CEND+" or "+OKBLUE+"[n]NO"+CEND+" or "+OKCYAN + "[m]MANUAL" + CEND)
        print("")
        OPTIONS_MOVIES_IMDB = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
        if OPTIONS_MOVIES_IMDB =="y":
            IMDB_URL = "https://www.google.com/search?q="+MOVIES_NAME+"+movie+imdb"
            IMDB_DATA = requests.get(IMDB_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
            IMDB_SOUP = BeautifulSoup(IMDB_DATA, "html.parser")
            IMDB_CONTENT = IMDB_SOUP.find('div',class_="kCrYT").a['href']
            print(WARNING +IMDB_CONTENT +CEND)
            print("")
            MOVIES_IMDB = input(WARNING +"ADD MOVIES IMDB URL: "+ CEND)
            POST['MOVIES_IMDB'] = MOVIES_IMDB
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            
        if OPTIONS_MOVIES_IMDB =="n":
            print("")
            print("\n[-] You must enter a EDIT MOVIES RELEASE DATE at least!", file=sys.stderr)
            MOVIES_IMDB = input(WARNING +"[+] ADD MOVIES IMDB URL: "+ CEND)
            POST['MOVIES_IMDB'] = MOVIES_IMDB
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
        
        if OPTIONS_MOVIES_IMDB =="m":
            MOVIES_IMDB ="https://www.imdb.com/find?q=" + MOVIES_NAME 
            POST['MOVIES_IMDB'] = MOVIES_IMDB
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
  
def DATE_INPUT():
    print("")
    MOVIES_NAME = POST['MOVIES_NAME']
    MOVIES_DATE = input(WARNING +"[+] EDIT MOVIES RELEASE DATE: "+ CEND)
    POST['MOVIES_DATE'] = MOVIES_DATE
    json.dump(POST, open(POST_FILE, "w"), indent = 2)
    while not MOVIES_DATE:
        print("\n[+]"+FAIL+" Are You Search Movies Release date on Google? OPTIONS : "+OKGREEN+"[y]YES"+CEND+" or "+OKBLUE+"[n]NO"+CEND)
        print("")
        OPTIONS_MOVIES_DATE = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
        if OPTIONS_MOVIES_DATE =="y":
            SITEMAP_URL = "https://www.google.com/search?q="+MOVIES_NAME+"+movie+release+date"
            NEWS_DATA = requests.get(SITEMAP_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
            NEWS_SOUP = BeautifulSoup(NEWS_DATA, "html.parser")
            NEWS_CONTENT = NEWS_SOUP.find_all('div',class_ = "BNeawe")
            if NEWS_CONTENT:   
                for data in NEWS_CONTENT:
                    ALL_CONTENT = (data.get_text())
                    MOVIES_BODY = re.sub(r' +', ' ', ALL_CONTENT).replace('\n ','').replace('\n','')
                    print(WARNING + MOVIES_BODY + CEND)
                    print("")

        MOVIES_DATE = input(WARNING +"[+] EDIT MOVIES RELEASE DATE: "+ CEND)
        POST['MOVIES_DATE'] = MOVIES_DATE
        json.dump(POST, open(POST_FILE, "w"), indent = 2)    

        if OPTIONS_MOVIES_DATE =="n":
            print("")
            print("\n[-] You must enter a EDIT MOVIES RELEASE DATE at least!", file=sys.stderr)
            MOVIES_DATE = input(WARNING +"EDIT MOVIES RELEASE DATE: "+ CEND)
            POST['MOVIES_DATE'] = MOVIES_DATE
            json.dump(POST, open(POST_FILE, "w"), indent = 2)



try:
    TEMPLATE = DATA["TEMPLATE"]
    if TEMPLATE:
        if TEMPLATE == 1 or TEMPLATE == 2 or TEMPLATE == 3 or TEMPLATE == 4 or TEMPLATE == 5:
            if TEMPLATE == 1 or TEMPLATE == 2 or TEMPLATE == 4:
                MAIN_INPUT()
                IMAGE_INPUT() 
                DATA['STATUS'] = 3  
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
                subprocess.Popen('python replace.py', shell=True)

            if TEMPLATE == 3 or TEMPLATE == 5:
                MAIN_INPUT()
                IMAGE_INPUT()
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                IMDB_INPUT()
                DATE_INPUT()
                DATA['STATUS'] = 3  
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                subprocess.Popen('python replace.py', shell=True)
        else:
            print("")
            DATA["TEMPLATE"] = int(input('\033[93m' +"UPLOAD TEMPLATE NUMBER: "+ '\033[0m'))
            print("")
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
            subprocess.Popen('python input.py', shell=True)  
    else:
        print("")
        DATA["TEMPLATE"] = int(input('\033[93m' +"UPLOAD TEMPLATE NUMBER: "+ '\033[0m'))
        print("")
        json.dump(POST, open(POST_FILE, "w"), indent = 2)
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
        subprocess.Popen('python input.py', shell=True)
   
except Exception as e:   
        print("ERROR: edit.py")  
        print(e)



