import json
from Google import Create_Service
import subprocess
import random
import re

TAG = random.choice(["Download MP4moviez and Telegram to Watch Online","Download in Downloadhub 1080p 720p 480p","download filmyzilla 1080p 720p 480p","Download in filmywap 1080p 720p 480p","download vegamovies1080p 720p 480p","download telegram 1080p 720p 480p ","download telegram link","Download in telegram 1080p 720p 480p","download in telegram link 1080p 720p 480p","download hdhub4u 1080p 720p 480p","full download filmymeet 1080p 720p 480p","full download link 1080p 720p 480p","download filmy4wap 1080p 720p 480p","Download in Hindi filmyzilla 1080p 720p 480p","Watch Online 1080p 720p 480p","Download in Downloadhub 480p 720p  1080p","download filmyzilla 480p 720p  1080p","Download in filmywap 480p 720p  1080p","download vegamovies 480p 720p 1080p","download telegram 480p 720p 1080p","download telegram link 720p 480p 720p 1080p","Download in telegram 480p 720p 1080p","download in telegram link 480p 720p 1080p","download hdhub4u  480p 720p 1080p","full download filmymeet 480p 720p 1080p","full download link 480p 720p 1080p","download filmy4wap 480p 720p 1080p","Download in Hindi filmyzilla 480p 720p 1080p"," download in telugu movierulz"," download in telugu movierulz 480p 720p 1080p","download in Tamil kuttymovies 480p 720p 1080p"])

POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)

DATA_FILE = 'data.json'
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)

if POST['MOVIES_CONTENT'] == "CONTENTURLNOTFOUND":
    print("CONTENT NOT FOUND WAIT....")
    DATA['STATUS'] = 3  
    json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
    subprocess.Popen('python replace.py', shell=True)
    exit()
else:
    try:
        CLIENT_SECRET_FILE = 'client_secrets.json'
        API_NAME = 'blogger'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/blogger']
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        LABELS_1 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'])

        LABELS_2 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'])

        LABELS_3 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'])

        LABELS_4 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'+","+POST['MOVIES_NAME'].lower()+' 720p download'])

        LABELS_5 = ",".join(['movies'+","+POST['MOVIES_NAME'].lower()+' download'+","+POST['MOVIES_NAME'].lower()+' 300mb download'+","+POST['MOVIES_NAME'].lower()+' 480p download'+","+POST['MOVIES_NAME'].lower()+' 720p download'+","+POST['MOVIES_NAME'].lower()+' 1080p download'])

        NUMBER_OF_LABELS_1 = len(re.sub("[^a-zA-Z]", "", LABELS_1))
        NUMBER_OF_LABELS_2 = len(re.sub("[^a-zA-Z]", "", LABELS_2))
        NUMBER_OF_LABELS_3 = len(re.sub("[^a-zA-Z]", "", LABELS_3))
        NUMBER_OF_LABELS_4 = len(re.sub("[^a-zA-Z]", "", LABELS_4))
        NUMBER_OF_LABELS_5 = len(re.sub("[^a-zA-Z]", "", LABELS_5))

        if NUMBER_OF_LABELS_1<=120:
            LABELS = LABELS_1
        if NUMBER_OF_LABELS_2<=120:
            LABELS = LABELS_2
        if NUMBER_OF_LABELS_3<=120:
            LABELS = LABELS_3
        if NUMBER_OF_LABELS_4<=120:
            LABELS = LABELS_4
        if NUMBER_OF_LABELS_5<=120:
            LABELS = LABELS_5

        TITLE_ROW = (DATA['MOVIES_TITLE'])
        MOVIES_TITLE_ROW = re.sub(r' +', ' ', TITLE_ROW).replace('\n ','').replace(' 2000 ',' (2000) ').replace(' 2001 ',' (2001) ').replace(' 2002 ',' (2002) ').replace(' 2003 ',' (2003) ').replace(' 2004 ',' (2004) ').replace(' 2005 ',' (2005) ').replace(' 2006 ',' (2006) ').replace(' 2007 ',' (2007) ').replace(' 2008 ',' (2008) ').replace(' 2009 ',' (2009) ').replace(' 2010 ',' (2010) ').replace(' 2011 ',' (2011) ').replace(' 2012 ',' (2012) ').replace(' 2012 ',' (2012) ').replace(' 2013 ',' (2013) ').replace(' 2015 ',' (2015) ').replace(' 2016 ',' (2016) ').replace(' 2017 ',' (2017) ').replace(' 2018 ',' (2018) ').replace(' 2019 ',' (2019) ').replace(' 2020 ',' (2020) ').replace(' 2021 ',' (2021) ').replace(' 2022 ',' (2022) ').replace(' 2023 ',' (2023) ').replace(' 2024 ',' (2024) ').replace(' 2025 ',' (2025) ').replace('HDRip ESubs HEVC','').replace('HDRip','').replace('ESubs','').replace('HEVC','').replace('UNCUT','').replace('WEB-DL','').replace('BluRay','').replace('Web-DL','').replace(' (HQ-Dub) ',' ').replace('MSubs','')
        
        MOVIES_TITLE = re.sub(r' +', ' ', MOVIES_TITLE_ROW)

        TITLE = MOVIES_TITLE + " " + TAG

        CONTENT = POST['MOVIES_CONTENT']
        with open(CONTENT) as CONTENT_DATA:
            NEWS_CONTENT = CONTENT_DATA.read()

        movies_body = {
                "title": TITLE,
                "content": NEWS_CONTENT,
                "labels"  : LABELS,
            }
            
        res = service.posts().insert(blogId='5813569594685204437', body=movies_body, isDraft=True).execute()

        # print(res)
        print("")
        print("[+][+][+][+][+] POST COMPLITED! [+][+][+][+][+][+]")

        if DATA['AUTO'] == 1:
            SEANN_NO_OF_URL = DATA['SEANN_NO_OF_URL']
            DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL +1   
            DATA['STATUS'] = 1
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
            subprocess.Popen('python scanner.py', shell=True)
            POST['MOVIES_NAME'] = ""
            POST['MOVIES_NAME_MIX'] = ""
            POST['MOVIES_STORY'] = ""
            POST['MOVIES_IMDB'] = ""
            POST['MOVIES_DATE'] = ""
            POST['MOVIES_IMG'] = ""
            POST['MOVIES_CONTENT'] = ""
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            exit()

        if DATA['AUTO'] == 0:
            DATA['STATUS'] = 1
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
            subprocess.Popen('python input.py', shell=True)
            POST['MOVIES_NAME'] = ""
            POST['MOVIES_NAME_MIX'] = ""
            POST['MOVIES_STORY'] = ""
            POST['MOVIES_IMDB'] = ""
            POST['MOVIES_DATE'] = ""
            POST['MOVIES_IMG'] = ""
            POST['MOVIES_CONTENT'] = ""
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            exit()
        
    except Exception as e:   
        print("ERROR FROM FILE NAME upload.py: ") 
        print('pip install --upgrade google-api-python-client') 
        print(e)

        