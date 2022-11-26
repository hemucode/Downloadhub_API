import json
from Google import Create_Service
import subprocess
import time
import random

TAG = random.choice(["Download in Downloadhub","Movie download filmyzilla","Movie Download in filmywap","movie download vegamovies","Movie download telegram","Movie download telegram link","Movie Download in telegram","download movie in telegram linK","movie download hdhub4u","full Movie download filmymeet","full Movie download link","Movie download filmy4wap","Movie Download in Hindi filmyzilla"])

try:
    CLIENT_SECRET_FILE = 'client_secrets.json'
    API_NAME = 'blogger'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/blogger']
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    POST_FILE = 'post.json'
    with open(POST_FILE) as POST_DATA:
        POST = json.load(POST_DATA)

    DATA_FILE = 'data.json'
    with open(DATA_FILE) as MAIN_DATA:
        DATA = json.load(MAIN_DATA)


    LABELS = "movies,"+POST['MOVIES_NAME'].lower()+" 300mb download",POST['MOVIES_NAME'].lower()+" 480p download",POST['MOVIES_NAME'].lower()+" 720p download"
    TITLE = DATA['MOVIES_TITLE'] + " " + TAG

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
    print("POST COMPLITED!")
    

    SEANN_NO_OF_URL = DATA['SEANN_NO_OF_URL']
    DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL +1   
    DATA['STATUS'] = 1
    json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
    time.sleep(2)
    subprocess.Popen('python scanner.py', shell=True)



except Exception as e:   
    print("ERROR FROM FILE NAME upload.py: ") 
    print('pip install --upgrade google-api-python-client') 
    print(e)
    exit()
	