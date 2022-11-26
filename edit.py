#!/usr/bin/env python3
import os,sys;
import json
from datetime import datetime
import re
import subprocess

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
    IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
    TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])
    DATA_FILE = 'data.json'
    with open(DATA_FILE) as MAIN_DATA:
        DATA = json.load(MAIN_DATA)

    POST_FILE = 'post.json'
    with open(POST_FILE) as POST_DATA:
        POST = json.load(POST_DATA)

    NUMBER = DATA['STATUS']

    if NUMBER ==3:
        subprocess.Popen('python blogger.py', shell=True)

    if NUMBER ==2:
        print(WARNING + "MOVIES TITLE: "+CRED + DATA['MOVIES_TITLE'] + CEND)
        print('')
        CONTENT = DATA['MOVIES_DEATILS']
        with open(CONTENT) as CONTENT_DATA:
            NEWS_CONTENT = CONTENT_DATA.read()
            print(WARNING + "MOVIES CONTENT: "+ OKCYAN + NEWS_CONTENT + CEND)
            print("")
            print("")

        if DATA["TEMPLATE"] ==1:
            MOVIES_NAME = input(WARNING +"EDIT MOVIES NAME: "+ CEND)
            while not MOVIES_NAME:
                print("\n[+]"+FAIL+" Are You Skip Next Movies? OPTIONS : "+OKGREEN+"[n]Next"+CEND+" or "+OKBLUE+"[a]Add Url Number"+CEND)
                print("")
                OPTIONS = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
                if OPTIONS=="n":
                    DATA['STATUS'] = 1
                    SEANN_NO_OF_URL = DATA['SEANN_NO_OF_URL']
                    DATA['SEANN_NO_OF_URL'] = SEANN_NO_OF_URL + 1
                    print("SCANNING NEXT URL.....")
                    json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                    subprocess.Popen('python scanner.py', shell=True)
                    exit()
                if OPTIONS=="a":
                    print("")
                    ADD_URL_NO_OPTIONS = int(input(WARNING +"Add Url Number: "+ CEND))
                    if ADD_URL_NO_OPTIONS:
                        DATA['STATUS'] = 1
                        DATA['SEANN_NO_OF_URL'] = ADD_URL_NO_OPTIONS
                        json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
                        subprocess.Popen('python scanner.py', shell=True)
                        exit()
                else:
                    print("")
                    MOVIES_NAME = input(WARNING +"EDIT MOVIES NAME: "+ CEND)

                 
            print("")

            MOVIES_NAME_MIX = input(WARNING +"EDIT MOVIES NAME MIX: "+ CEND)
            while not MOVIES_NAME_MIX:
                print("\n[-] You must enter a MOVIES NAME  MIX at least!", file=sys.stderr)
                MOVIES_NAME_MIX = input("EDIT  MOVIES NAME MIX: ")

            print("")

            MOVIES_STORY = input(WARNING +"ADD MOVIES STORY: "+ CEND)
            while not MOVIES_STORY:
                print("\n[-] You must enter a MOVIES  STORY at least!", file=sys.stderr)
                MOVIES_STORY = input("ADD MOVIES _STORY: ")

            print("")

            MOVIES_IMG = input(WARNING +"ADD MOVIES IMG: "+ CEND)
            while not MOVIES_IMG:
                print("\n[-] You must enter a MOVIES IMG at least!", file=sys.stderr)
                MOVIES_IMG = input("ADD MOVIES IMG: ")

            POST['MOVIES_NAME'] = MOVIES_NAME
            POST['MOVIES_NAME_MIX'] = MOVIES_NAME_MIX
            POST['MOVIES_STORY'] = MOVIES_STORY
            POST['MOVIES_IMG'] = MOVIES_IMG
            json.dump(POST, open(POST_FILE, "w"), indent = 2)

            TEMPLATE_1 = "<style type='text/css'> .button__link{ border-style: solid; border-top-width: 0; border-right-width: 0; border-left-width: 0; border-bottom-width: 0; border-color: #0274be; background-color: red; color: #ffffff; font-family: inherit; font-weight: inherit; line-height: 1; border-radius: 2px; padding-top: 10px; padding-right: 40px; padding-bottom: 10px; padding-left: 40px; display: inline-block; text-align: center; word-break: break-word; box-sizing: border-box; font-size: inherit; } .button__link:hover{ background-color: #404040; } </style> <div class='contentAI'> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' border='0' data-original-height='836' data-original-width='1254' height='169' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1' width='113' /> </a> <noscript> <img decoding='async' width='113' height='169' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME+" movie download filmywap</figcaption> </div> <p><strong>Click the following "+MOVIES_NAME+" movie download filmywap button</strong>"+MOVIES_STORY+"</p> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>"+MOVIES_NAME+" movie download telegram link</span></strong> </a> </div> </div> <h3 style='margin-bottom: 20px; margin-top: 20px;'>"+MOVIES_NAME+" movie download telegram link</h3> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank' title='SERVER 1 (Standard Download)'><strong> <span style='color: white;'>SERVER 1 (Standard Download)</span></strong> </a> </div> </div> <h3 style='margin-bottom: 20px; margin-top: 20px;'>Button for "+MOVIES_NAME+" movie download in tamil kuttymovies</h3> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>SERVER 2 (Fast Download)</span></strong> </a> </div> </div> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p><strong>"+MOVIES_NAME+" movie download in tamil isaimini</strong> <strong>HI-subtitles</strong> in English for the Deaf or Hard-of-Hearing (<b><span style='color: #2b00fe;'>SDH</span></b>). These&nbsp;are the text format of the spoken part of a television, movie, or <b>TV</b> series. In most cases, <b>OTT</b> platforms provide audiences with one of three options to make their content more accessible and easier to understand</p> <div style='margin-bottom: 10px;'> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>SERVER 3 (SuperFast Download)</span></strong> </a> </div> </div> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <ul> <li>Subtitles</li> <li>Closed Captions</li> <li>SDH (Subtitles for the Deaf or Hard-of-Hearing)</li> </ul> <p>[<strong><span style='color: red;'>index of "+MOVIES_NAME+" movie download pagalworld</span></strong>] Hi subtitles provide better understanding of the video program you watch. Unlike non-HI subtitles it include not only dialogs spoken by characters but also the subtle sounds that pops up all around the program. Some of those sounds are namely gunshots, glass break, blast, grunting, barking, shouting.</p> <h3><strong>Types of subtitles</strong></h3> <ol> <li><strong>Subtitles</strong>: These are the subtitles for <b>"+MOVIES_NAME_MIX+"</b><strong> 2022 movie download site eliteanswers.in</strong> intended for the viewer who does not understand the original language of content. Not recommended for hearing impaired people.</li><br /> <li><strong><span style='color: #2b00fe;'>Closed Caption</span></strong>: These are the subtitles for <strong>"+MOVIES_NAME+" movie download tamilrockers</strong> intended for the viewer who is audibly challenged. Closed Captions are in same language as that of the content. Not recommended for foreigner audiences who doesn't understand that particular language</li><br /> <li><strong>SDH</strong>: These are the subtitles for <strong>"+MOVIES_NAME+" 2022 movie download</strong> intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreigner audiences who doesn't understand that particular language of content.</li> </ol> <p>Thanks for downloading <strong>"+MOVIES_NAME+" tamil movie download <span style='color: #2b00fe;'>moviesda</span></strong> SDH Subtitles from <strong><a href='http://needevery.in'>needevery.in</a></strong>. If you found this article helpful please support us by sharing these posts with your friends. We also try to update you with the newest content.</p> <p><span style='color: red;'><b>"+MOVIES_NAME_MIX+"</b></span> 2022 subtitles download, "+MOVIES_NAME+" English subtitles, "+MOVIES_NAME+" subtitles, "+MOVIES_NAME+" subtitles English, "+MOVIES_NAME+" movie subtitles, "+MOVIES_NAME+" srt, download "+MOVIES_NAME+" subtitles, subtitles for "+MOVIES_NAME+" , "+MOVIES_NAME+" eng sub,"+MOVIES_NAME+" Hindi subtitles download</p> </div> <script type='text/javascript'> domReady(() => { linkButton() }) function domReady (callback) { if (document.readyState === 'complete') { callback() } else { window.addEventListener('load', callback, false); } } function linkButton() { linkin = document.location.href mfd; document.querySelector('.button__link').href = linkin; } </script>"
            # print(TEMPLATE_1)
            with open("post/"+TEXT_FILE_NAME, "w") as file:
                file.write(TEMPLATE_1)
            POST['MOVIES_CONTENT'] = "post/"+TEXT_FILE_NAME
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            DATA['STATUS'] = 3  
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            subprocess.Popen('python blogger.py', shell=True)
               
    else:
        DATA['STATUS'] = 3  
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
        subprocess.Popen('python blogger.py', shell=True)

except Exception as e:   
        print("ERROR: edit.py")  
        print(e)
