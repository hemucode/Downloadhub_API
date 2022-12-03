#!/usr/bin/env python3
import os,sys,time,re;
import json
from datetime import datetime
import subprocess
import requests
from bs4 import BeautifulSoup

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


NUMBER = DATA['STATUS']


if NUMBER == 1:
    subprocess.Popen('python scanner.py', shell=True)
    exit()

if NUMBER == 3:
    subprocess.Popen('python replace.py', shell=True)
    exit()


def PRINT_MOVIES_DATA():
    print('')
    print(WARNING + "[+] MOVIES TITLE: "+CRED + DATA['MOVIES_TITLE'] + CEND)
    print('')
    CONTENT = DATA['MOVIES_DEATILS']
    with open(CONTENT) as CONTENT_DATA:
        NEWS_CONTENT = CONTENT_DATA.read()
        print(WARNING + "[+] MOVIES CONTENT: "+ OKCYAN + NEWS_CONTENT + CEND)
        print("")
        print("")

def MAIN_INPUT():
    MOVIES_NAME = input(WARNING +"[+] EDIT MOVIES NAME: "+ CEND)
    while not MOVIES_NAME:
        print("\n[+]"+FAIL+" Are You Skip Next Movies? OPTIONS : "+OKGREEN+"[n]Next"+CEND+" or "+OKBLUE+"[a]Add Url Number"+CEND)
        print("")
        OPTIONS = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
        if OPTIONS=="n":
            DATA['STATUS'] = 1
            SEANN_NO_OF_URL = DATA['SEANN_NO_OF_URL']
            DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL + 1
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            subprocess.Popen('python scanner.py', shell=True)
            exit()
        if OPTIONS=="a":
            print("")
            ADD_URL_NO_OPTIONS = int(input(WARNING +"[+] Add Url Number: "+ CEND))
            if ADD_URL_NO_OPTIONS:
                DATA['STATUS'] = 1
                DATA['SEANN_NO_OF_URL'] = ADD_URL_NO_OPTIONS
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                subprocess.Popen('python scanner.py', shell=True)
                exit()
        else:
            print("")
            MOVIES_NAME = input(WARNING +"[+] EDIT MOVIES NAME: "+ CEND)
                
    print("")

    MOVIES_NAME_MIX = input(WARNING +"[+] EDIT MOVIES NAME MIX: "+ CEND)
    while not MOVIES_NAME_MIX:
        print("\n[-] You must enter a MOVIES NAME  MIX at least!", file=sys.stderr)
        MOVIES_NAME_MIX = input("[+] EDIT  MOVIES NAME MIX: ")

    print("")

    MOVIES_STORY = input(WARNING +"[+] ADD MOVIES STORY: "+ CEND)
    while not MOVIES_STORY:
        print("\n[-] You must enter a MOVIES  STORY at least!", file=sys.stderr)
        MOVIES_STORY = input("[+] ADD MOVIES _STORY: ")

    POST['MOVIES_TITLE'] =  DATA['MOVIES_TITLE']
    POST['MOVIES_NAME'] = MOVIES_NAME
    POST['MOVIES_NAME_MIX'] = MOVIES_NAME_MIX
    POST['MOVIES_STORY'] = MOVIES_STORY
    json.dump(POST, open(POST_FILE, "w"), indent = 2)


def IMAGE_INPUT():
    print("")
    MOVIES_IMG = input(WARNING +"[+] ADD MOVIES IMG: "+ CEND)
    while not MOVIES_IMG:
        print("\n[-] You must enter a MOVIES IMG at least!", file=sys.stderr)
        MOVIES_IMG = input(WARNING +"[+] ADD MOVIES IMG: "+ CEND)
        if not MOVIES_IMG:
            subprocess.Popen('python edit.py', shell=True)
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

        else:
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
    if NUMBER == 2:
        PRINT_MOVIES_DATA()
        if TEMPLATE == 1 or TEMPLATE == 2 or TEMPLATE == 3 or TEMPLATE == 4:
            if TEMPLATE == 1 or TEMPLATE == 2 or TEMPLATE == 4:
                MAIN_INPUT()
                IMAGE_INPUT() 
                DATA['STATUS'] = 3  
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
                subprocess.Popen('python edit.py', shell=True)

            if TEMPLATE == 3:
                MAIN_INPUT()
                IMAGE_INPUT()
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                IMDB_INPUT()
                DATE_INPUT()
                DATA['STATUS'] = 3  
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                subprocess.Popen('python edit.py', shell=True)
        else:
            print("")
            DATA["TEMPLATE"] = int(input('\033[93m' +"UPLOAD TEMPLATE NUMBER: "+ '\033[0m'))
            print("")
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
            subprocess.Popen('python edit.py', shell=True)
   
except Exception as e:   
        print("ERROR: edit.py")  
        print(e)


