#!/usr/bin/env python3
import os;
import json
from datetime import datetime
import random
import subprocess
os.system('color')

TAG_MOVIES = random.choice(["Download in Downloadhub","Movie download filmyzilla","Movie Download in filmywap","movie download vegamovies","Movie download telegram","Movie download telegram link","Movie Download in telegram","download movie in telegram link","movie download hdhub4u","full Movie download filmymeet","full Movie download link","Movie download filmy4wap","Movie Download in Hindi filmyzilla"])

DATA_FILE = 'data.json'
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)

POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)

TEXT_FILE_NAME = "".join([datetime.now().strftime("%y%m%d%H%M%S"),'.txt'])

try:
    MOVIES_NAME = POST['MOVIES_NAME']
    MOVIES_NAME_MIX = POST['MOVIES_NAME_MIX']
    MOVIES_STORY = POST['MOVIES_STORY'] 
    MOVIES_IMG = POST['MOVIES_IMG']
    TEMPLATE_NO = DATA["TEMPLATE"]
    if MOVIES_NAME and MOVIES_NAME_MIX and MOVIES_NAME_MIX and MOVIES_STORY and MOVIES_IMG and TEMPLATE_NO:
        TEMPLATE = "<style type='text/css'> ol{ margin: 0 0 1.5em 3em; } h3{ line-height: 1.4; margin-bottom: 20px; } li{ border: 0; font-size: 100%; font-style: inherit; font-weight: inherit; margin: 0; outline: 0; padding: 0; vertical-align: baseline; } a{ color: #0274be; transition: all .2s linear; }#download{margin-bottom: 20px;text-align: center;user-select: none;} .button__link{ border-style: solid; border-top-width: 0; border-right-width: 0; border-left-width: 0; border-bottom-width: 0; border-color: #0274be; background:linear-gradient(135deg,rgb(76,16,145) 0%,rgb(125,9,36) 100%); color: #ffffff; font-family: inherit; font-weight: inherit; line-height: 1; border-radius: 2px; padding-top: 10px; padding-right: 40px; padding-bottom: 10px; padding-left: 40px; display: inline-block; text-align: center; word-break: break-word; box-sizing: border-box; font-size: inherit; margin-bottom: 5px; animation: color 10s ease-out infinite; } .button__link:hover{ background-color: #404040; } @keyframes color{ 0%{background: linear-gradient(to left, #fd746c, #ff9068);} 10%{background: linear-gradient(to left, #fd746c, #f0ff68);} 20%{background: linear-gradient(to left, #fd746c, #99ff68);} 30%{background: linear-gradient(to left, #fdc36c, #68ff9f);} 40%{background: linear-gradient(to left, #fdc36c, #68d3ff);} 50%{background: linear-gradient(to left, #b2fd6c, #687cff);} 60%{background: linear-gradient(to left, #6cfdac, #f968ff);} 70%{background: linear-gradient(to left, #6c7dfd, #f968ff);} 80%{background: linear-gradient(to left, #6c7dfd, #ff6882);} 90%{background: linear-gradient(to left, #EC4A5E, #68ffee);} 100%{background: linear-gradient(to left, #d96cfd, #68ffee);} } </style> <div class='entry-content clear' itemprop='text' style='height: auto !important;'> <div class='code-block code-block-1' style='margin: 8px 0; clear: both;'> <!-- ads --> </div> <h3>"+MOVIES_NAME+" movie download telegram link</h3> <div style='height: auto !important;'> <div style='height: auto !important;'> <div data-ad-id='2171' style='text-align: center; float: none; height: auto !important;'> <div style='font-size:10px;text-align:center;color:#cccccc;'>Advertisement</div> <!-- ads --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> </div> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img width='97' height='140' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download , "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" full movie download in hindi mp4moviez' border='0' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 480p 720p 1080p 1' /> </a><noscript><img decoding='async' width='97' height='140' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download , "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" full movie download in hindi mp4moviez' title='"+MOVIES_NAME+" movie download filmyzilla 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME +" "+ TAG_MOVIES +"</figcaption> </div> <p><strong>"+MOVIES_NAME+" movie download</strong> () <strong><a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>Hindi Dubbed</a></strong> in English for the Deaf or Hard-of-Hearing (SDH). These&nbsp;are the text format of the spoken part of a television, movie, or TV series. In most cases, OTT platforms provide audiences with one of three options to make their <em><a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>"+MOVIES_NAME_MIX+"</a></em> more accessible and easy to understand &gt;&gt;</p> <div style='height: auto !important;'> <div style='height: auto !important;'> <div data-ad-id='2171' style='text-align: center; float: none; height: auto !important;' class='afw afw-ga afw_ad afwadid-2171 '> <div style='font-size:10px;text-align:center;color:#cccccc;'>Advertisement</div> <!-- ads --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> </div> <p>Newly released <strong><strong>"+MOVIES_NAME_MIX+"</strong> movie free download</strong> &amp; watch online versions are available in multiple resolutions like&nbsp;<strong>1080p</strong>,<strong>&nbsp;720p,</strong>&nbsp;<strong>480p</strong>. You can <strong>download "+MOVIES_NAME+" movie in&nbsp;BluRay</strong>,&nbsp;WEB-DL,&nbsp;HDRip,&nbsp;WEBRip&nbsp;&amp;&nbsp;mp4&nbsp;video formats. The movie is available in full hd on different online movie-watching <a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'><strong>websites</strong></a> for free in mkv.</p> <div style='margin: 8px 0; clear: both;'> <!-- ads --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> <h4>"+MOVIES_STORY+"</h4> <div style='height: auto !important;'> <div style='height: auto !important;'> <div data-ad-id='2171' style='text-align: center; float: none; height: auto !important;'> <div style='font-size:10px;text-align:center;color:#cccccc;'>Advertisement</div> <!-- ads --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div></div> <p><strong>Hit the below download "+MOVIES_NAME_MIX+" movie button</strong></p> <div> <div id='download' style='text-align: center;user-select: none;'><a class='button__link' href='?a=superstar' target='_blank' rel='noreferrer noopener'><strong>"+MOVIES_NAME_MIX+" movie download</strong></a></div> </div> <div style='height: auto !important;'> <div style='height: auto !important;'> <div data-ad-id='2171' style='text-align: center; float: none; height: auto !important;' class='afw afw-ga afw_ad afwadid-2171 '> <div style='font-size:10px;text-align:center;color:#cccccc;'>Advertisement</div> <!-- ad --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> </div> <h5>Button for "+MOVIES_NAME_MIX+" movie download telegram link</h5> <ul> <li>Subtitles (Hindi Dubbed)</li> <li>Closed Captions mkv</li> <li>SDH (Subtitles for the Deaf or Hard-of-Hearing)</li> </ul> <p><strong>"+MOVIES_NAME+" movie download 720p</strong> give thorough understanding of the video program you watch. Unlike non-HI <a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>subtitles</a> it include not only dialogs spoken by characters but also the subtle sounds that pops up all around the program. Some of those sounds are namely gunshots, glass break, blast, grunting, barking, shouting.</p> <h3><strong>Types of subtitles</strong></h3> <ol> <li><strong>Subtitles</strong>: These are the subtitles for <strong>"+MOVIES_NAME_MIX+" movie download in 480p</strong> intended for the viewer who does not understand the original language of content. Not recommended for hearing impaired people.</li> <li><strong>SDH</strong>: These are the subtitles for <strong><strong>"+MOVIES_NAME+"</strong> full movie download filmyzilla1080p</strong> intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreigner audiences who doesn't understand that specific language of content.</li> <li><strong>Closed Caption</strong>: These are the subtitles for <strong>"+MOVIES_NAME_MIX+" movie hindi dubbed download</strong> intended for the viewer who is audibly challenged. Closed Captions are in same language as that of the content. Not recommended for foreigner audiences who doesn't understand that specific language</li> </ol> <p>Thanks for downloading <strong><strong>"+MOVIES_NAME_MIX+"</strong> download link telegram</strong> full movie from <strong><a href='https://www.needevery.in//' data-type='URL' data-id='https://www.needevery.in//' target='_blank' rel='noreferrer noopener'>www.needevery.in</a></strong>. If you found this article helpful please support us by sharing these posts with your friends. We try to keep you updated with the <a href='https://www.needevery.in/' target='_blank' rel='noreferrer noopener'>latest movies</a> and Netflix series.</p> <h2><strong>Disclaimer</strong></h2> <p>This website is for <strong>INFORMATION PURPOSE</strong> only. We neither provide any copyrighted content nor support piracy on this website through any of its article. Nevertheless, what we do give is News &amp; details easily available all over the internet. </p> <div class='code-block code-block-6' style='margin: 8px 0; clear: both;'> <!-- ads --> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div>"
        with open("post/"+TEXT_FILE_NAME, "w") as file:
            file.write(TEMPLATE)
        POST['MOVIES_CONTENT'] = "post/"+TEXT_FILE_NAME
        DATA['STATUS'] = 4  
        DATA['TEMPLATE'] = 1
        json.dump(POST, open(POST_FILE, "w"), indent = 2)
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
        print('\033[92m'+"[+] POST RADY FOR UPLOAD" + '\033[0m') 
        print("")
        subprocess.Popen('python blogger.py', shell=True)
    else:
        print("")
        print('\033[92m'+"[+] WAIT INPUT ARE NOT UPDATED" + '\033[0m')
        subprocess.Popen('python edit.py', shell=True)
        print("")

    
except Exception as e:   
        print("ERROR: replace.py")  
        print(e)


