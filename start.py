#!/usr/bin/env python3
import requests,os,json,subprocess;
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

COMMENT = 0
DATA_FILE = 'data.json'
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)


def UPLOAD_FILE():
    COMMENT_TEIL = "....."
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R1 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/data.json')
    with open("data.json", 'wb') as A1:
        A1.write(R1.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R2 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/scanner.py')
    with open("scanner.py", 'wb') as A2:
        A2.write(R2.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R3 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/edit.py')
    with open("edit.py", 'wb') as A3:
        A3.write(R3.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R4 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/blogger.py')
    with open("blogger.py", 'wb') as A4:
        A4.write(R4.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R5 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/start.py')
    with open("blogger.py", 'wb') as A5:
        A5.write(R5.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R6 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/client_secrets.json')
    with open("client_secrets.json", 'wb') as A6:
        A6.write(R6.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R7 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/client_secrets.json')
    with open("client_secrets.json", 'wb') as A7:
        A7.write(R7.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R8 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/Google.py')
    with open("Google.py", 'wb') as A8:
        A8.write(R8.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."
    R9 = requests.get('https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/replace.py')
    with open("replace.py", 'wb') as A9:
        A9.write(R9.content)
    time.sleep(1)
    print(COMMENT + COMMENT_TEIL)
    COMMENT_TEIL = COMMENT_TEIL + "..."


try:
    #Requests FROM NEW Sitemap URL 
    SITEMAP_URL = "https://raw.githubusercontent.com/hemucode/Downloadhub_API/main/data.json"
    NEWS_DATA = requests.get(SITEMAP_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
    NEWS_SOUP = BeautifulSoup(NEWS_DATA, "html.parser")
    #print(NEWS_SOUP)
    SITE_JSON=json.loads(NEWS_SOUP.text)
    # print(SITE_JSON['VARSION'])

    if DATA['VARSION'] != SITE_JSON['VARSION']:
        print("APPLICATION ARE NOT UPDATE:  OPTIONS : [u]UPDATE or [n]NOT UPDATE")
        OPTIONS = input("WATI YOUR ANS: ")
        if OPTIONS:
            if OPTIONS == "u":
                COMMENT = "[+] UPDATE"
                UPLOAD_FILE()
                print("")
                print("UPDATE COMPLITED!")
                subprocess.Popen('python scanner.py', shell=True)
            
        else:
            subprocess.Popen('python scanner.py', shell=True)
               
except Exception as e:   
        print("UPDATE ERROR........")  
        print(e)


        

