#!/usr/bin/env python3
import os,sys,time,re;
import json
from datetime import datetime
import random
import subprocess
import requests
from bs4 import BeautifulSoup
TAG_MOVIES = random.choice(["Download in Downloadhub","Movie download filmyzilla","Movie Download in filmywap","movie download vegamovies","Movie download telegram","Movie download telegram link","Movie Download in telegram","download movie in telegram linK","movie download hdhub4u","full Movie download filmymeet","full Movie download link","Movie download filmy4wap","Movie Download in Hindi filmyzilla"])
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
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)

POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)


try:
    IMG_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.JPG'])
    TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])

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

            TEMPLATE_1 = "<style type='text/css'> .button__link{ border-style: solid; border-top-width: 0; border-right-width: 0; border-left-width: 0; border-bottom-width: 0; border-color: #0274be; background-color: red; color: #ffffff; font-family: inherit; font-weight: inherit; line-height: 1; border-radius: 2px; padding-top: 10px; padding-right: 40px; padding-bottom: 10px; padding-left: 40px; display: inline-block; text-align: center; word-break: break-word; box-sizing: border-box; font-size: inherit; } .button__link:hover{ background-color: #404040; } </style> <div class='contentAI'> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' border='0' data-original-height='836' data-original-width='1254' height='169' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1' width='113' /> </a> <noscript> <img decoding='async' width='113' height='169' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME+" "+TAG_MOVIES+"</figcaption> </div> <p><strong>Click the following "+MOVIES_NAME+" movie download filmywap button</strong>"+MOVIES_STORY+"</p> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>"+MOVIES_NAME+" "+TAG_MOVIES+"</span></strong> </a> </div> </div> <h3 style='margin-bottom: 20px; margin-top: 20px;'>"+MOVIES_NAME+" movie download telegram link</h3> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank' title='SERVER 1 (Standard Download)'><strong> <span style='color: white;'>SERVER 1 (Standard Download)</span></strong> </a> </div> </div> <h3 style='margin-bottom: 20px; margin-top: 20px;'>Button for "+MOVIES_NAME+" movie download in tamil kuttymovies</h3> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>SERVER 2 (Fast Download)</span></strong> </a> </div> </div> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p><strong>"+MOVIES_NAME+" movie download in tamil isaimini</strong> <strong>HI-subtitles</strong> in English for the Deaf or Hard-of-Hearing (<b><span style='color: #2b00fe;'>SDH</span></b>). These&nbsp;are the text format of the spoken part of a television, movie, or <b>TV</b> series. In most cases, <b>OTT</b> platforms provide audiences with one of three options to make their content more accessible and easier to understand</p> <div style='margin-bottom: 10px;'> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span>SERVER 3 (SuperFast Download)</span></strong> </a> </div> </div> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <ul> <li>Subtitles</li> <li>Closed Captions</li> <li>SDH (Subtitles for the Deaf or Hard-of-Hearing)</li> </ul> <p>[<strong><span style='color: red;'>index of "+MOVIES_NAME+" movie download pagalworld</span></strong>] Hi subtitles provide better understanding of the video program you watch. Unlike non-HI subtitles it include not only dialogs spoken by characters but also the subtle sounds that pops up all around the program. Some of those sounds are namely gunshots, glass break, blast, grunting, barking, shouting.</p> <h3><strong>Types of subtitles</strong></h3> <ol> <li><strong>Subtitles</strong>: These are the subtitles for <b>"+MOVIES_NAME_MIX+"</b><strong> 2022 movie download site eliteanswers.in</strong> intended for the viewer who does not understand the original language of content. Not recommended for hearing impaired people.</li><br /> <li><strong><span style='color: #2b00fe;'>Closed Caption</span></strong>: These are the subtitles for <strong>"+MOVIES_NAME+" movie download tamilrockers</strong> intended for the viewer who is audibly challenged. Closed Captions are in same language as that of the content. Not recommended for foreigner audiences who doesn't understand that particular language</li><br /> <li><strong>SDH</strong>: These are the subtitles for <strong>"+MOVIES_NAME+" 2022 movie download</strong> intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreigner audiences who doesn't understand that particular language of content.</li> </ol> <p>Thanks for downloading <strong>"+MOVIES_NAME+" tamil movie download <span style='color: #2b00fe;'>moviesda</span></strong> SDH Subtitles from <strong><a href='http://needevery.in'>needevery.in</a></strong>. If you found this article helpful please support us by sharing these posts with your friends. We also try to update you with the newest content.</p> <p><span style='color: red;'><b>"+MOVIES_NAME_MIX+"</b></span> 2022 subtitles download, "+MOVIES_NAME+" English subtitles, "+MOVIES_NAME+" subtitles, "+MOVIES_NAME+" subtitles English, "+MOVIES_NAME+" movie subtitles, "+MOVIES_NAME+" srt, download "+MOVIES_NAME+" subtitles, subtitles for "+MOVIES_NAME+" , "+MOVIES_NAME+" eng sub,"+MOVIES_NAME+" Hindi subtitles download</p> </div> <script type='text/javascript'> domReady(() => { linkButton() }) function domReady (callback) { if (document.readyState === 'complete') { callback() } else { window.addEventListener('load', callback, false); } } function linkButton() { linkin = document.location.href mfd; document.querySelector('.button__link').href = linkin; } </script>"
            # print(TEMPLATE_1)
            with open("post/"+TEXT_FILE_NAME, "w") as file:
                file.write(TEMPLATE_1)
            POST['MOVIES_CONTENT'] = "post/"+TEXT_FILE_NAME
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            DATA['STATUS'] = 3  
            DATA['TEMPLATE'] = 2  
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            subprocess.Popen('python blogger.py', shell=True)


        if DATA["TEMPLATE"] ==2:
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
            print("")

            POST['MOVIES_NAME'] = MOVIES_NAME
            POST['MOVIES_NAME_MIX'] = MOVIES_NAME_MIX
            POST['MOVIES_STORY'] = MOVIES_STORY
            POST['MOVIES_IMG'] = MOVIES_IMG
            json.dump(POST, open(POST_FILE, "w"), indent = 2)

            TEMPLATE_1 ="<style type='text/css'> .button__link{ border-style: solid; border-top-width: 0; border-right-width: 0; border-left-width: 0; border-bottom-width: 0; border-color: #0274be; background:linear-gradient(135deg,rgb(76,16,145) 0%,rgb(125,9,36) 100%); color: #ffffff; font-family: inherit; font-weight: inherit; line-height: 1; border-radius: 2px; padding-top: 10px; padding-right: 40px; padding-bottom: 10px; padding-left: 40px; display: inline-block; text-align: center; word-break: break-word; box-sizing: border-box; font-size: inherit; margin-bottom: 5px; } .button__link:hover{ background-color: #404040; } </style> <div itemprop='text'> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img width='97' height='109' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download 2022, "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" 2022 full movie download in hindi mp4moviez' border='0' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1' /> </a><noscript><img decoding='async' width='97' height='109' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download 2022, "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" 2022 full movie download in hindi mp4moviez' title='"+MOVIES_NAME+" movie download filmyzilla 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME +" "+ TAG_MOVIES +"</figcaption> </div> <P>"+MOVIES_STORY+"</p> <h3>[Download] "+MOVIES_NAME +" "+ TAG_MOVIES +"</h3> <p>Are you strongly willing for&nbsp;<strong>"+MOVIES_NAME+" full hd movie download link</strong>&nbsp;and are searching on the internet for Varun Dhavan&nbsp;"+MOVIES_NAME+" movie download telegram link, then this particular post is dedicated for such audience. We are about to hold you full information about&nbsp;<strong>"+MOVIES_NAME+" movie movie download 720p</strong>&nbsp;and how to stream "+MOVIES_NAME+" online mp4moviez.</p> <p>"+MOVIES_NAME+" Download&nbsp;Filmyzilla HD, 4k, 300MB, 360p, 480p, 720p, 1080p, Filmywap, Vegamovies, Movierulz, iBomma, Filmy4wap, Free, but you must know about <strong>"+MOVIES_NAME_MIX+" movie download in tamil mp4moviez</strong>.</p> <h3>"+MOVIES_NAME+" Movie Download 300mb</h3> <p>"+MOVIES_NAME+" is going to compete with many other movies from different industries. Hench people will not only search for "+MOVIES_NAME+" full movie download but will also search for south &amp; Hollywood movies free download links and index. Shortly after the release <strong>"+MOVIES_NAME+" full movie</strong> will be available for <strong>download</strong> in <strong>HDCAM</strong>. It can also be downloaded from movie download telegram channels. Many infamous downloading sites like Filmyzilla HD, 4k, 300MB, 360p, 480p, 720p, 1080p, Filmywap, Vegamovies, Movierulz, iBomma, Filmy4wap will be making it available in <strong>theatre print</strong> and <strong>Hall Print</strong> for audience to watch "+MOVIES_NAME+" for free online</p> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <h4>"+MOVIES_NAME+" 2022 full movie download in hindi mp4moviez</h4> <p>How many reasons can be given why Filmyzilla is the best south/<strong>PAN India movie</strong> website to download movies.&nbsp;For starters, the site has a huge selection of movies available for download, including both latest in theatre and all time favorites.</p> <p>The site also offers high-quality downloads, so you can be sure that you're getting the best possible quality when you <strong>"+MOVIES_NAME+" Download Filmyzilla</strong>.&nbsp;Filmyzilla is a pirated website.&nbsp;That's why we oppose it, if you are so sorry to watch the movie, please go to the cinema hall and watch it.</p> <h3>Why Google search always show "+MOVIES_NAME+" movie download 480p?</h3> <p>You must have noticed this thing which is actually so weird, you can try it right away. Go to google search and search for "+MOVIES_NAME+". Then you will get a long list of keywords that are getting searched in large quantity that starts with <strong>"+MOVIES_NAME+" 2022 movie download</strong>. These are based on “<strong>People also search for</strong>” or “People also ask”. As users on google starts searching for a particular thing, google ranks it based on it's search volume, hence larger the search volume, higher is the rank. As soon as a awaited and popular movie gets announced or releases like "+MOVIES_NAME+", users search released queries like <strong>"+MOVIES_NAME+" cast</strong>, "+MOVIES_NAME+" release date, "+MOVIES_NAME+" review hindi, <strong>"+MOVIES_NAME+" advanced booking</strong>. User search queries are not limited to this, it also includes keywords like <strong>"+MOVIES_NAME+" movie download filmyzilla</strong>, "+MOVIES_NAME+" movie download 2022, <strong>"+MOVIES_NAME+" movie download kuttymovies</strong>, "+MOVIES_NAME+" movie download <strong>vegamovies</strong>, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download in hindi filmywap. Such keywords which are long in length are also referred as <strong>LONG TAIL KEYWORDS</strong>. Long tail keywords in digital marketing are so much important.</p> <div class='separator' style='clear: both;'> <a href='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' data-src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' style='display: block; padding: 1em 0px; text-align: center;'> <img decoding='async' width='658' height='548' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download 2022, "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" 2022 full movie download in hindi mp4moviez' border='0' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' data-src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1' /> </a><noscript>"       
            TEMPLATE_2 = "<img decoding='async'decoding='async' width='658' height='548' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download 2022, "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" 2022 full movie download in hindi mp4moviez' srcset='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG 658w, https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1JW6rvXykEgr4O4lY33Ri3vcZhk_Cd237kYeOQDIE8QLEiBCPRtoCvabB_3lSRy0iwc6IvkpYlJIWy8Rc0I_y3vVffaspqTPksqb8FKXE98zEYhC7iqXybbc0qNgEnCD3E1BV25QLFGIZ9qrIFHFj34ZjfHN9uM6_NJzCb2W4jPZcQrCgUFw5C01_/s1600/3124545.PNG' sizes='(max-width: 658px) 100vw, 658px' title='"+MOVIES_NAME+" movie download filmyzilla 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME +" "+ TAG_MOVIES +"</figcaption> </div> <h3>"+MOVIES_NAME+" movie download moviesda in hindi</h3> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p><strong>"+MOVIES_NAME+" movie download in Hindi filmyzilla hd</strong> (2022) <strong><a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>Hindi Dubbed</a></strong> in English for the Deaf or Hard-of-Hearing (SDH). These&nbsp;are the text format of the spoken part of a television, movie, or TV series. In most cases, OTT platforms provide audiences with one of three options to make their <em><a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>"+MOVIES_NAME+"</a></em> more accessible and easy to understand &gt;&gt;</p> <h3>"+MOVIES_NAME+" telegram download Link</h3> <p>As you can tell that if you are looking for&nbsp;<strong>"+MOVIES_NAME+" download link filmymeet on&nbsp;</strong>telegram, then it is very difficult to find it now and in many places, people are fooling people by giving the download link to Kriti Sanon "+MOVIES_NAME+" movie. If you are thinking that by&nbsp;<strong>searching "+MOVIES_NAME+" download movierulz</strong>&nbsp;on telegram, you will download the movie from there, then do not do this at all because it is wrong to do so and such channels are deleted on telegram so that you cannot download the movie.</p> <p>Latest released <strong>"+MOVIES_NAME+" movie download isaimini</strong> &amp; watch online <strong>720p</strong> versions are available in multiple resolutions like&nbsp;<strong>1080p</strong>,<strong>&nbsp;720p,</strong>&nbsp;<strong>480p</strong>. You can <strong>"+MOVIES_NAME+" movie download kuttymovies in&nbsp;BluRay</strong>,&nbsp;WEB-DL,&nbsp;HDRip,&nbsp;WEBRip&nbsp;&amp;&nbsp;mp4&nbsp;video formats. The movie is available in full hd on different online movie-watching <a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'><strong>websites</strong></a> for free in mkv.</p> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p class='has-text-align-center has-vivid-red-color has-text-color'><strong>Hit the below index of "+MOVIES_NAME+" 2022 hd movie button</strong></p> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='AI-POST-URL?a=superstar' rel='noreferrer noopener' target='_blank'><strong> <span target='_blank' rel='noreferrer noopener'>"+MOVIES_NAME+" movie download [mkv]</span></strong> </a> </div> </div> <h3>"+MOVIES_NAME+" movie download in Tamil Kuttymovies</h3> <p>Every visitors must be aware that if you try to download any online movie <strong>300mb</strong> then it has been declared illegal by the Government of India, you can download any movie.&nbsp;If caught downloading illegally, you can be jailed or fined for it.</p> <p>If you want to watch movies legally then you can watch it by visiting the nearest cinema hall or you can watch movies using an online subscription like Ullu app, Hulu, Disney+, Kooku app Netflix, Amazon Prime etc.</p> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <div> <div id='download' style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noreferrer noopener' target='_blank' title='"+MOVIES_NAME+" movie download filmyzilla'><strong> <span style='color: white;'>"+MOVIES_NAME +" "+ TAG_MOVIES +"</span></strong> </a> </div> </div> <div> <div> <div data-ad-id='2180' style='text-align:center; margin-top:px; margin-bottom:px; margin-left:px; margin-right:px;float:none;' class='afw afw-ga afw_ad afwadid-2180 '> <div style='font-size:10px;text-align:center;color:#cccccc;'>Advertisement</div> <script async='' src='//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'> </script> <ins class='adsbygoogle' style='background: none; display: inline-block; max-width: 800px; width: 100%; height: 280px; max-height: 200px;' data-ad-client='ca-pub-4069350686060090' data-ad-slot='4738988805' data-ad-format='auto' data-full-width-responsive='true' data-adsbygoogle-status='done'> <div id='aswift_10_host' style='border: none; height: 280px; width: 612px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;'></div> </ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> </div> <h5>Button for "+MOVIES_NAME+" movie download telegram link</h5> <ul> <li>Subtitles (Hindi Dubbed)</li> <li>Closed Captions mkv</li> <li>SDH (Subtitles for the Deaf or Hard-of-Hearing)</li> </ul> <p><strong>"+MOVIES_NAME+" movie download 720p</strong> give thorough understanding of the video program you watch. Unlike non-HI <a href='https://www.needevery.in' target='_blank' rel='noreferrer noopener'>subtitles</a> it include not only dialogs spoken by characters but also the subtle sounds that pops up all around the program. Some of those sounds are namely gunshots, glass break, blast, grunting, barking, shouting.</p> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <h3><strong>Types of subtitles</strong></h3> <p>Subtitles is a medium to make "+MOVIES_NAME+" enjoyable for Deaf and people who do not understand "+MOVIES_NAME+" movie original language.</p> <ol> <li><strong>Subtitles</strong>: These are the subtitles for <strong>"+MOVIES_NAME+" movie download 480p</strong> intended for the viewer who does not understand the original language of content. Not recommended for hearing impaired people.</li> <li><strong>SDH</strong>: These are the subtitles for <strong>"+MOVIES_NAME+" full movie download 1080p</strong> intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreigner audiences who doesn't understand that specific language of content.</li> <li><strong>Closed Caption</strong>: These are the subtitles for <strong>"+MOVIES_NAME+" movie download hindi</strong> intended for the viewer who is audibly challenged. Closed Captions are in same language as that of the content. Not recommended for foreigner audiences who doesn't understand that specific language</li> </ol> <div style='float: none; margin-bottom: 15px; margin: 0px 0px 15px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p>Thanks for downloading <strong>"+MOVIES_NAME+" movie download ibomma</strong> full movie from <strong><a href='https://www.needevery.in/' data-type='URL' data-id='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>needevery.in</a></strong>. If you found this article helpful please support us by sharing these posts with your friends. We try to keep you updated with the <a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>latest movies</a> and Netflix series.</p> <h3><strong>Disclaimer</strong></h3> <p>This website is for <strong>INFORMATION PURPOSE</strong> only. We neither provide any copyrighted content nor support piracy on this website through any of its article. Nevertheless, what we do give is News &amp; details easily available all over the internet. Theft of anyone's intellectual property, art or any type of physical or digital material is a punishable offense under the Copyright Act.&nbsp;Always watch movie in Theatres or <strong>OTT platform</strong> with valid subscriptions. </p> </div><script type='text/javascript'> domReady(() => { linkButton() }) function domReady (callback) { if (document.readyState === 'complete') { callback() } else { window.addEventListener('load', callback, false); } } function linkButton() { linkin = document.location.href mfd; document.querySelector('.button__link').href = linkin; } </script>"
            # print(TEMPLATE_1)
            TEMPLATE = TEMPLATE_1 + TEMPLATE_2
            with open("post/"+TEXT_FILE_NAME, "w") as file:
                file.write(TEMPLATE)
            POST['MOVIES_CONTENT'] = "post/"+TEXT_FILE_NAME
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            DATA['STATUS'] = 3  
            DATA['TEMPLATE'] = 3
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            time.sleep(2)
            subprocess.Popen('python blogger.py', shell=True)

            
        if DATA["TEMPLATE"] ==3:
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
            print("\n[+]"+FAIL+" Are You Search Movies IMDB URL Google? OPTIONS : "+OKGREEN+"[y]YES"+CEND+" or "+OKBLUE+"[n]NO"+CEND)
            OPTIONS_MOVIES_IMDB = input("[+]"+WARNING +" PRESS NOW: "+ CEND)
            print("")
            if OPTIONS_MOVIES_IMDB=="y":
                IMDB_URL = "https://www.google.com/search?q="+MOVIES_NAME+"+movie+imdb"
                IMDB_DATA = requests.get(IMDB_URL,headers=headers).content.decode('utf-8').encode('cp850','replace').decode('cp850')
                IMDB_SOUP = BeautifulSoup(IMDB_DATA, "html.parser")
                IMDB_CONTENT = IMDB_SOUP.find('div',class_="kCrYT").a['href']
                # IMDB_CONTENT_1 = IMDB_SOUP.find('div',class_="kCrYT").a[1]['href']
                # IMDB_CONTENT_2 = IMDB_SOUP.find('div',class_="kCrYT").a[2]['href']
                if IMDB_CONTENT:
                    print(WARNING +IMDB_CONTENT +CEND)
                    MOVIES_IMDB = input("[+]"+WARNING +" ADD MOVIES IMDB: "+ CEND)
                    while not MOVIES_IMDB:
                        MOVIES_IMDB = "https://www.imdb.com/find?q=" + MOVIES_NAME
                else:
                    MOVIES_IMDB = input("[+]"+WARNING +" ADD MOVIES IMDB: "+ CEND)
                    while not MOVIES_IMDB:
                        MOVIES_IMDB = "https://www.imdb.com/find?q=" + MOVIES_NAME

            if OPTIONS_MOVIES_IMDB=="n":
                MOVIES_IMDB = input("[+]"+WARNING +" ADD MOVIES IMDB: "+ CEND)

            else:
                MOVIES_IMDB = "https://www.imdb.com/find?q=" + MOVIES_NAME
            
            print("")


            MOVIES_DATE = input(WARNING +"EDIT MOVIES RELEASE DATE: "+ CEND)
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

                MOVIES_DATE = input(WARNING +"EDIT MOVIES RELEASE DATE: "+ CEND)    

                if OPTIONS_MOVIES_DATE =="n":
                    print("\n[-] You must enter a EDIT MOVIES RELEASE DATE at least!", file=sys.stderr)
                    MOVIES_DATE = input(WARNING +"EDIT MOVIES RELEASE DATE: "+ CEND)
            
            with open(CONTENT) as CONTENT_DATA:
                NEWS_CONTENT = CONTENT_DATA.read()
                print(WARNING + "MOVIES CONTENT: "+ OKCYAN + NEWS_CONTENT + CEND)
                print("")
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
            TEMPLATE_1 = "<div class='contentAI'> <h3> <blockquote>"+MOVIES_STORY+"</blockquote> </h3> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' border='0' data-original-height='836' data-original-width='1254' height='169' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1' width='113' /> </a> <noscript> <img decoding='async' width='113' height='169' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 2022 480p 720p 1080p 1'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME+" "+TAG_MOVIES+"</figcaption> </div> <p><strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla 2022 480p 720p 1080p Full HD</strong>&nbsp;for the&nbsp;<strong>Deaf or Hard-of-Hearing</strong>&nbsp;(SDH). These are the text format of the spoken part of a&nbsp;<strong>television</strong>, movie, or TV series. In most cases,&nbsp;<strong>OTT&nbsp;</strong>platforms provide audiences with one of three options to make their index of Mkv,&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla&nbsp;</strong>2022 480p 720p 1080p&nbsp;<strong>Full HD</strong>&nbsp;more accessible and easy to understand.</p> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p>Newly released<strong>&nbsp;"+MOVIES_NAME+" 2 Movie Download in Filmyzilla&nbsp;2022 HD cam movie download</strong>&nbsp;with subtitles &amp; watch&nbsp;<strong>online</strong>&nbsp;versions are available in multiple resolutions like&nbsp;<strong>1080p, 720p, and 480p.</strong>&nbsp;You can&nbsp;"+MOVIES_NAME+" Movie Download in Filmyzilla<strong>&nbsp;</strong>massaman in&nbsp;<strong>BluRay, WEB-DL, HDRip, WEBRip</strong>&nbsp;&amp; mp4 video formats. The movie is&nbsp;<strong>available</strong>&nbsp;in full HD on different online movie-watching&nbsp;<strong>websites</strong>&nbsp;for free in MKV.</p> <div class='ads-code-block ads-code-block-1' style='clear: both; margin: 8px 0px;'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> <h3>"+MOVIES_NAME+" Movie Release Date: <strong>"+MOVIES_DATE+"</strong></h3> <hr style='background-color: #cccccc; border-bottom: 1px solid; border-image: initial; border-left: none; border-right: none; border-top: 1px solid; border: 1px solid; box-sizing: content-box; height: 1px; margin-bottom: 1.5em; max-width: 100%;' /> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla Full Hd Link</h2> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-3'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p><strong>"+MOVIES_NAME_MIX+" Movies Download in Filmyzilla&nbsp;720p gives</strong>&nbsp;a thorough understanding of the video program you watch. Unlike non-Hl subtitles, it includes not only dialogs spoken by characters but also the subtle sounds&nbsp;<strong>that pop up all around&nbsp;</strong>the program. Some of&nbsp;<strong>those sounds</strong>&nbsp;are namely gunshots, glass break, blast, grunting, barking<a href='https://www.codehemu.com/' rel='noreferrer noopener nofollow' target='_blank'>,</a>&nbsp;and shouting.</p> <p><strong>More details: <a data-id='"+MOVIES_IMDB+"' data-type='URL' href='https://www.imdb.com/find?q=' rel='noreferrer noopener nofollow' target='_blank'>Click Here</a></strong></p> <p class='has-background' style='background-color: #eb6f6f; border: 0px; box-sizing: inherit; color: #212121; font-family: Poppins, sans-serif; font-size: 17px; margin: 0px 0px 1.5em; padding: 1.25em 2.375em;'><span style='box-sizing: inherit; font-weight: 700;'>Note:</span>&nbsp;We never support or promote any piracy content.</p> <hr style='background-color: #cccccc; border-bottom: 1px solid; border-image: initial; border-left: none; border-right: none; border-top: 1px solid; border: 1px solid; box-sizing: content-box; height: 1px; margin-bottom: 1.5em; max-width: 100%;' /> <p>• Subtitles (<strong>Hindi English</strong>&nbsp;Dubbed)</p> <p>• Closed Captions Mkv</p> <p>• SDH (Subtitles for the Deaf or Hard-of-Hearing)</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movies Download 2022</h2> <p>Promovies has also leaked&nbsp;"+MOVIES_NAME+" Movies Download in Filmyzilla&nbsp;in Hindi&nbsp;and&nbsp;<strong>millions of people have downloaded</strong>&nbsp;from this website. This&nbsp;<strong>website</strong>&nbsp;also leaks to websites and movies online within a day of its release. This website is very popular due to the option of downloading new&nbsp;<strong>Hindi,&nbsp;</strong>languages <strong>movies&nbsp;</strong>and web series on this&nbsp;<strong>website</strong>&nbsp;as well as watching them online.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Button for "+MOVIES_NAME+" Movie Download Server</h2> <p style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: rgb(66, 133, 244); border-radius: 1px !important; border: 1px solid rgb(51, 101, 183); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: white; display: inline-block; font-family: Oswald; font-size: 15px; letter-spacing: 0.05em; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 10px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>DIRECT LINK (FAST)</a> <span style='background-color: white; color: #555555; font-family: Roboto, sans-serif, Arial; font-size: 14px; text-align: -webkit-center;'>&nbsp;</span> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: url(&quot;&quot;) -1px 0px no-repeat rgb(13, 110, 175); border-radius: 1px !important; border: 2px solid rgb(8, 89, 144); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: rgb(255, 255, 255) !important; display: inline-block; font-family: Oswald; font-size: 15px; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 14px 9px 20px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>G DRIVE &amp; DIRECT LINK</a> <span style='background-color: white; color: #555555; font-family: Roboto, sans-serif, Arial; font-size: 14px; text-align: -webkit-center;'>&nbsp;</span> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: url(&quot;&quot;) -1px 0px no-repeat green; border-radius: 1px !important; border: 2px solid rgb(8, 89, 144); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: rgb(255, 255, 255) !important; display: inline-block; font-family: Oswald; font-size: 15px; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 14px 9px 20px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>SINGLE DOWNLOAD LINKS</a> </p> <div style='float: none; margin-top: 5px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME_MIX+" Movies Download in Filmyzilla</h2> <p>Filmyzilla is a torrent website that&nbsp;<strong>releases</strong>&nbsp;any movie and web series within a few hours as soon as it is released. For this reason this website has become even more popular in a very short time. In today's time, more t<strong>han 1 million people</strong>&nbsp;use this website to download movies and web series.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 480p 2022</h2> <p>You might<strong>&nbsp;also want to know</strong>&nbsp;that to download&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla</strong>&nbsp;Full Movie. So for your information, let me tell you that some sites have leaked<strong>&nbsp;</strong>"+MOVIES_NAME+" Movie Download in Filmyzilla &nbsp;in different quality which you can&nbsp;<strong>easily download</strong>. You have to search by typing this, such as the "+MOVIES_NAME+" Movie Download in Filmyzilla movieshub1<strong>080p, 720p, 480p, Full HD&nbsp;</strong>will be seen.</p> <div id='toc_container'>"
            TEMPLATE_2 ="<p class='toc_title'> Also Read </p> <ul class='toc_list'> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' data-id='https://www.needevery.in/2022/11/the-soccer-football-movie-2022-hindi.html' data-type='URL' href='https://www.needevery.in/2022/11/the-soccer-football-movie-2022-hindi.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>The Soccer Football Movie 2022 Download</a> </strong> </li> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' href='https://www.needevery.in/2022/11/vengeance-2022-hindi-org-dual-audio.html' data-id='https://www.needevery.in/2022/11/vengeance-2022-hindi-org-dual-audio.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>Vengeance 2022 Movie Download in moviesda</a> </strong> </li> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' href='https://www.needevery.in/2022/11/ori-devuda-movie-download-in-hdhub4u.html' data-id='https://www.needevery.in/2022/11/ori-devuda-movie-download-in-hdhub4u.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>Ori Devuda Movie Download filmy4wap</a> </strong> </li> </ul> </div> <p><strong>"+MOVIES_NAME+" Movie Download in Filmyzilla</strong>&nbsp;and If you want to download this movies from&nbsp;<strong>filmyzilla</strong>, then you have to go to this website and you will get<strong>&nbsp;350 MB in 480p</strong>&nbsp;and you will be able to download it very easily from this website. Not recommended for hearing impaired people.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 720p</h2> <p>If you want to download "+MOVIES_NAME+" Movie Download in Filmyzilla<strong>,</strong>&nbsp;then you have to go to this website and you will get<strong>&nbsp;735 MB in 720p</strong>&nbsp;and you will be able to download it very easily from this website.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 1080p</h2> <p>If you want to download this movies from&nbsp;<strong>filmyzilla</strong>, then you have to go to this website and you will get<strong>&nbsp;1.26 GB in 720p</strong>&nbsp;and you will be able to download it very easily from this website. in this&nbsp;<strong>website you&nbsp;</strong>can download all movies but&nbsp;<strong>i not recommended you download any movies&nbsp;</strong>in other website.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Downloadhub 480p 2022</h2> <p>How To Download From DownloadHub. You might<strong>&nbsp;also want to know</strong>&nbsp;that to download&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Downloadhub</strong>&nbsp;Full Movie. So for your information, let me tell you that some sites have leaked<strong>&nbsp;</strong>"+MOVIES_NAME+" Movie Download in Filmyzilla &nbsp;in different quality which you can&nbsp;<strong>easily download</strong>. You have to search by typing this, such as the "+MOVIES_NAME+" Movie Download in Downloadhub<strong>080p, 720p, 480p, Full HD&nbsp;</strong>will be seen.</p> <div title='How To Movies Download From serach' class='separator' style='clear: both; text-align: center;'><object class='BLOG_video_class' contentid='6940daa0c706cad1' width='600' height='498' id='BLOG_video-6940daa0c706cad1' aria-label='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla'></object></div>  <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Full HD "+MOVIES_NAME+" Movie Download hdhub4u</h2> <p>Filmymeet is a&nbsp;<strong>torrent website</strong>&nbsp;that releases any movie and web series within a few hours as soon as it is released. For this reason this website has become&nbsp;<strong>even more popula</strong>r in a very short time. In today's time, more than 1 million people use this website to download movies and web series.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Tamilrockers</h2> <p>"+MOVIES_NAME+" Movie Download in<strong>&nbsp;</strong>Tamilrockers is one of the trending searches by the fans of "+MOVIES_NAME+" Movie Download in Tamilrockers is a pirated website that&nbsp;<strong>illegally&nbsp;</strong>leaks movies, web series, videos for free. If any movies are leaked by Tamilrockers, people should avoid using them and use the legal platform. By doing so would be a great support for the film industry.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/avatar-2-2022-hindi-dual-audio-1080p.html'> <blockquote>Avatar 2 (2022) Full Movie In Hindi Download Filmyzilla [320p, 480p, 720p, 4k Full HD] Mp4moviez, Filmymeet, Filmywap, Vegamovies</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmywap</h2> <p>Doing piracy of the copy righted is illegal and it is considered a crime. People who search for "+MOVIES_NAME+" Movie Download in Filmywap this article is for you. On the torrent website, Filmywap users can download the latest movies, Bollywood movies, dubbed Hindi movies, etc. But using this torrent website is safe? No, it is not safe, as this is a third-party website it is illegal to use it. Avoid using torrent websites and start using legal platforms.&nbsp;&nbsp;</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in mp4moviez</h2> <p>"+MOVIES_NAME+" Movie Download in Mp4moviez leaks Hindi, Hollywood movies, Hindi dubbed movies for free. Once a movie is released, mp4moviez uploads the movie illegally on its website. It is a crime to piracy a movie and download a piracy movie. So people should avoid searching on "+MOVIES_NAME+" Movie Download in mp4moviez and use legal ways for streaming the movie.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/black-adam-2022-hindi-russian-english.html'> <blockquote>Black Adam(2022) Download In Hindi Telegram Link, Filmywap, Fillmyzilla, 123mkv, Mp4moviez [HD, 320p, 780p, 1080p]</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME_MIX+" Movie Download in Kuttymovies</h2> <p>Kuttymovies is also a pirated website famous for tamil movies download,"+MOVIES_NAME+" Movie Download in Hindi dubbed movies download. The content available on the torrent website Kuttymovies are all pirated contents. Users are allowed to download unlimited of movies from the torrent website.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/bhediya-2022-movie-1080p-720p-480p.html'> <blockquote>Bhediya(2022) Download Full Movie In Download Filmyzilla [320p, 480p, 720p, 4k Full HD] Mp4moviez, Filmymeet, Filmywap, Vegamovies</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in iBomma</h2> <p>iBomma, this website also leaks Hollywood, Hindi, "+MOVIES_NAME+" Movie Download in Hindi movies for free. But using iBomma and other torrent wbeiste is not safe and we do not recommend to use torrent websites.&nbsp;</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Types of subtitle</h2> <p>1. Subtitles:- These are the subtitles for&nbsp;<strong>"+MOVIES_NAME+" Movie Download in</strong>&nbsp;300MB intended for the viewer who does not understand the original language of the content. Not recommended for hearing impaired people.</p> <p>2. SDH:- These are the subtitles for<strong>&nbsp;"+MOVIES_NAME+" 2 Movie Download filmywap</strong>&nbsp;in 1080p intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreign audiences who don't understand the specific language of the content.</p> <p>3. Closed Caption:- These are the subtitles for&nbsp;<strong>"+MOVIES_NAME+" Movie Download in</strong>&nbsp;<strong>tamilrockers&nbsp;</strong>intended for the viewer who is audibly challenged. Closed Captions are in the same language as the content.&nbsp;<strong>Not recommended for foreign&nbsp;</strong>audiences who don't understand that&nbsp;<strong>specific language.</strong></p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i><strong>Disclaimer</strong></h2> <p>This website is for <strong>INFORMATION PURPOSE</strong> only. We neither provide any copyrighted content nor support piracy on this website through any of its article. Nevertheless, what we do give is News &amp; details easily available all over the internet. </p> </div> <script type='text/javascript'> domReady(() => { linkButton() }) function domReady (callback) { if (document.readyState === 'complete') { callback() } else { window.addEventListener('load', callback, false); } } function linkButton() { linkin = document.location.href; document.querySelector('.button__link').href = linkin; } </script>"
            # print(TEMPLATE_1)
            TEMPLATE = TEMPLATE_1 + TEMPLATE_2
            with open("post/"+TEXT_FILE_NAME, "w") as file:
                file.write(TEMPLATE)
            POST['MOVIES_CONTENT'] = "post/"+TEXT_FILE_NAME
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            DATA['STATUS'] = 3  
            DATA['TEMPLATE'] = 1
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2) 
            subprocess.Popen('python blogger.py', shell=True)


except Exception as e:   
        print("ERROR: edit.py")  
        print(e)


