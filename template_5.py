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
    MOVIES_DATE = POST['MOVIES_DATE']
    MOVIES_IMDB = POST['MOVIES_IMDB']
    TEMPLATE_NO = DATA["TEMPLATE"]
    if MOVIES_IMDB and MOVIES_DATE and MOVIES_NAME and MOVIES_NAME_MIX and MOVIES_NAME_MIX and MOVIES_STORY and MOVIES_IMG and TEMPLATE_NO:
        TEMPLATE = "<div class='contentAI'> <h3> <blockquote>"+MOVIES_STORY+"</blockquote> </h3> <div class='separator' style='clear: both;'> <a href='"+MOVIES_IMG+"' style='display: block; padding: 1em 0px; text-align: center;'> <img alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' border='0' data-original-height='836' data-original-width='1254' height='169' src='"+MOVIES_IMG+"' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 480p 720p 1080p 1' width='113' /> </a> <noscript> <img decoding='async' width='113' height='169' src='"+MOVIES_IMG+"' alt='"+MOVIES_NAME+" movie download downloadhub,"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download telegram, "+MOVIES_NAME+" movie download hdhub4u, "+MOVIES_NAME+" full movie download filmymeet, "+MOVIES_NAME+" full movie download link, "+MOVIES_NAME+" movie download filmy4wap, "+MOVIES_NAME+" movie download in hindi filmyzilla,' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 480p 720p 1080p 1'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME+" "+TAG_MOVIES+"</figcaption> </div> <p><strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla 480p 720p 1080p Full HD</strong>&nbsp;for the&nbsp;<strong>Deaf or Hard-of-Hearing</strong>&nbsp;(SDH). These are the text format of the spoken part of a&nbsp;<strong>television</strong>, movie, or TV series. In most cases,&nbsp;<strong>OTT&nbsp;</strong>platforms provide audiences with one of three options to make their index of Mkv,&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla&nbsp;</strong> 480p 720p 1080p&nbsp;<strong>Full HD</strong>&nbsp;more accessible and easy to understand.</p> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p>Newly released<strong>&nbsp;"+MOVIES_NAME+" 2 Movie Download in Filmyzilla&nbsp; HD cam movie download</strong>&nbsp;with subtitles &amp; watch&nbsp;<strong>online</strong>&nbsp;versions are available in multiple resolutions like&nbsp;<strong>1080p, 720p, and 480p.</strong>&nbsp;You can&nbsp;"+MOVIES_NAME+" Movie Download in Filmyzilla<strong>&nbsp;</strong>massaman in&nbsp;<strong>BluRay, WEB-DL, HDRip, WEBRip</strong>&nbsp;&amp; mp4 video formats. The movie is&nbsp;<strong>available</strong>&nbsp;in full HD on different online movie-watching&nbsp;<strong>websites</strong>&nbsp;for free in MKV.</p> <div class='ads-code-block ads-code-block-1' style='clear: both; margin: 8px 0px;'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> <h3>"+MOVIES_NAME+" Movie Release Date: <strong>"+MOVIES_DATE+"</strong> </h3> <hr style='background-color: #cccccc; border-bottom: 1px solid; border-image: initial; border-left: none; border-right: none; border-top: 1px solid; border: 1px solid; box-sizing: content-box; height: 1px; margin-bottom: 1.5em; max-width: 100%;' /> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla Full Hd Link</h2> <div style='float: none; margin: 0px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-3'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <p><strong>"+MOVIES_NAME_MIX+" Movies Download in Filmyzilla&nbsp;720p gives</strong>&nbsp;a thorough understanding of the video program you watch. Unlike non-Hl subtitles, it includes not only dialogs spoken by characters but also the subtle sounds&nbsp;<strong>that pop up all around&nbsp;</strong>the program. Some of&nbsp;<strong>those sounds</strong>&nbsp;are namely gunshots, glass break, blast, grunting, barking<a href='https://www.codehemu.com/' rel='noreferrer noopener nofollow' target='_blank'>,</a>&nbsp;and shouting.</p> <p><strong>More details: <a data-id='"+MOVIES_IMDB+"' data-type='URL' href='"+MOVIES_IMDB+"' rel='noreferrer noopener nofollow' target='_blank'>Click Here</a></strong></p> <p class='has-background' style='background-color: #eb6f6f; border: 0px; box-sizing: inherit; color: #212121; font-family: Poppins, sans-serif; font-size: 17px; margin: 0px 0px 1.5em; padding: 1.25em 2.375em;'><span style='box-sizing: inherit; font-weight: 700;'>Note:</span>&nbsp;We never support or promote any piracy content.</p> <hr style='background-color: #cccccc; border-bottom: 1px solid; border-image: initial; border-left: none; border-right: none; border-top: 1px solid; border: 1px solid; box-sizing: content-box; height: 1px; margin-bottom: 1.5em; max-width: 100%;' /> <p>• Subtitles (<strong>Hindi English</strong>&nbsp;Dubbed)</p> <p>• Closed Captions Mkv</p> <p>• SDH (Subtitles for the Deaf or Hard-of-Hearing)</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movies Download </h2> <p>Promovies has also leaked&nbsp;"+MOVIES_NAME+" Movies Download in Filmyzilla&nbsp;in Hindi&nbsp;and&nbsp;<strong>millions of people have downloaded</strong>&nbsp;from this website. This&nbsp;<strong>website</strong>&nbsp;also leaks to websites and movies online within a day of its release. This website is very popular due to the option of downloading new&nbsp;<strong>Hindi,&nbsp;</strong>languages <strong>movies&nbsp;</strong>and web series on this&nbsp;<strong>website</strong>&nbsp;as well as watching them online.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Button for "+MOVIES_NAME+" Movie Download Server</h2> <p style='text-align: center;'> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: rgb(66, 133, 244); border-radius: 1px !important; border: 1px solid rgb(51, 101, 183); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: white; display: inline-block; font-family: Oswald; font-size: 15px; letter-spacing: 0.05em; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 10px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>DIRECT LINK (FAST)</a> <span style='background-color: white; color: #555555; font-family: Roboto, sans-serif, Arial; font-size: 14px; text-align: -webkit-center;'>&nbsp;</span> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: url(&quot;&quot;) -1px 0px no-repeat rgb(13, 110, 175); border-radius: 1px !important; border: 2px solid rgb(8, 89, 144); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: rgb(255, 255, 255) !important; display: inline-block; font-family: Oswald; font-size: 15px; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 14px 9px 20px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>G DRIVE &amp; DIRECT LINK</a> <span style='background-color: white; color: #555555; font-family: Roboto, sans-serif, Arial; font-size: 14px; text-align: -webkit-center;'>&nbsp;</span> <a class='button__link' href='?a=superstar' rel='noopener noreferrer' style='background: url(&quot;&quot;) -1px 0px no-repeat green; border-radius: 1px !important; border: 2px solid rgb(8, 89, 144); box-shadow: rgba(0, 0, 0, 0.2) 4px 4px 3px 0px; box-sizing: border-box; color: rgb(255, 255, 255) !important; display: inline-block; font-family: Oswald; font-size: 15px; line-height: 25px; margin-right: 10px; margin-top: 20px; opacity: 0.96; padding: 9px 14px 9px 20px; text-align: -webkit-center; text-decoration-line: none !important; text-transform: uppercase; transition: all 0.2s ease 0s; width: 288px;' target='_blank'>SINGLE DOWNLOAD LINKS</a> </p> <div style='float: none; margin-top: 5px; text-align: center;'> <div style='color: #cccccc; font-size: 10px; text-align: center;'>Advertisement</div> <div class='ads-code-block ads-code-block-2'> <ins class='adsbygoogle' data-ad-client='ca-pub-1364712756444138' data-ad-format='fluid' data-ad-layout='in-article' data-ad-slot='3179258459' style='display: block; text-align: center;'></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div>"
        TEMPLATE_2 = "<h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME_MIX+" Movies Download in Filmyzilla</h2> <p>Filmyzilla is a torrent website that&nbsp;<strong>releases</strong>&nbsp;any movie and web series within a few hours as soon as it is released. For this reason this website has become even more popular in a very short time. In today's time, more t<strong>han 1 million people</strong>&nbsp;use this website to download movies and web series.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 480p </h2> <p>You might<strong>&nbsp;also want to know</strong>&nbsp;that to download&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Filmyzilla</strong>&nbsp;Full Movie. So for your information, let me tell you that some sites have leaked<strong>&nbsp;</strong>"+MOVIES_NAME+" Movie Download in Filmyzilla &nbsp;in different quality which you can&nbsp;<strong>easily download</strong>. You have to search by typing this, such as the "+MOVIES_NAME+" Movie Download in Filmyzilla movieshub1<strong>080p, 720p, 480p, Full HD&nbsp;</strong>will be seen.</p> <div id='toc_container'> <p class='toc_title'> Also Read </p> <ul class='toc_list'> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' data-id='https://www.needevery.in/2022/11/the-soccer-football-movie-2022-hindi.html' data-type='URL' href='https://www.needevery.in/2022/11/the-soccer-football-movie-2022-hindi.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>The Soccer Football Movie Download</a> </strong> </li> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' href='https://www.needevery.in/2022/11/vengeance-2022-hindi-org-dual-audio.html' data-id='https://www.needevery.in/2022/11/vengeance-2022-hindi-org-dual-audio.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>Vengeance Movie Download in moviesda</a> </strong> </li> <li> <strong> <a data-type='URL' data-nodal='' data-type='post' href='https://www.needevery.in/2022/11/ori-devuda-movie-download-in-hdhub4u.html' data-id='https://www.needevery.in/2022/11/ori-devuda-movie-download-in-hdhub4u.html' rel='noreferrer noopener nofollow' target='_blank' vcdaldp-fin=''>Ori Devuda Movie Download filmy4wap</a> </strong> </li> </ul> </div> <p><strong>"+MOVIES_NAME+" Movie Download in Filmyzilla</strong>&nbsp;and If you want to download this movies from&nbsp;<strong>filmyzilla</strong>, then you have to go to this website and you will get<strong>&nbsp;350 MB in 480p</strong>&nbsp;and you will be able to download it very easily from this website. Not recommended for hearing impaired people.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 720p</h2> <p>If you want to download "+MOVIES_NAME+" Movie Download in Filmyzilla<strong>,</strong>&nbsp;then you have to go to this website and you will get<strong>&nbsp;735 MB in 720p</strong>&nbsp;and you will be able to download it very easily from this website.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmyzilla 1080p</h2> <p>If you want to download this movies from&nbsp;<strong>filmyzilla</strong>, then you have to go to this website and you will get<strong>&nbsp;1.26 GB in 720p</strong>&nbsp;and you will be able to download it very easily from this website. in this&nbsp;<strong>website you&nbsp;</strong>can download all movies but&nbsp;<strong>i not recommended you download any movies&nbsp;</strong>in other website.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Downloadhub 480p </h2> <p>How To Download From DownloadHub. You might<strong>&nbsp;also want to know</strong>&nbsp;that to download&nbsp;<strong>"+MOVIES_NAME_MIX+" Movie Download in Downloadhub</strong>&nbsp;Full Movie. So for your information, let me tell you that some sites have leaked<strong>&nbsp;</strong>"+MOVIES_NAME+" Movie Download in Filmyzilla &nbsp;in different quality which you can&nbsp;<strong>easily download</strong>. You have to search by typing this, such as the "+MOVIES_NAME+" Movie Download in Downloadhub<strong>080p, 720p, 480p, Full HD&nbsp;</strong>will be seen.</p> <div class='separator' style='clear: both;'> <a href='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG' style='display: block; padding: 1em 0px; text-align: center;'> <img decoding='async' width='658' height='548' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download , "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" full movie download in hindi mp4moviez' border='0' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG' data-src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG' title='"+MOVIES_NAME+" Movie Download in Filmyzilla 480p 720p 1080p 1' /> </a><noscript> <img decoding='async'decoding='async' width='658' height='548' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG' alt='"+MOVIES_NAME+" movie download filmyzilla, "+MOVIES_NAME+" movie download kuttymovies, "+MOVIES_NAME+" movie download , "+MOVIES_NAME+" movie download telegram link, "+MOVIES_NAME+" movie download vegamovies, "+MOVIES_NAME+" movie download filmymeet, "+MOVIES_NAME+" movie download filmywap, "+MOVIES_NAME+" full movie download in hindi mp4moviez' srcset='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG 658w, https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaOtV81dra0SrD3LeBqeRXFS4Bnvf45TCEypONCNnKQGsJE0w8-GSvzSKJT5UmIDk1D82UsKcSwpw08yAT3XJJa1mSQo3632QupNEYhHaKRWxfDzrVEXxMcYR2qfIHYfOBzl3rS-yUp0DGfI87OIIl4BQi3PaEzkJ-NpRroi24wYQDzmqDEgd0d-uE/s1600/3124545.PNG' sizes='(max-width: 658px) 100vw, 658px' title='"+MOVIES_NAME+" movie download filmyzilla 2'> </noscript> <figcaption style='font-size: 10px; margin: 0px 25px 0px 0px; text-align: center;'>"+MOVIES_NAME +" "+ TAG_MOVIES +"</figcaption> </div> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Full HD "+MOVIES_NAME+" Movie Download hdhub4u</h2> <p>Filmymeet is a&nbsp;<strong>torrent website</strong>&nbsp;that releases any movie and web series within a few hours as soon as it is released. For this reason this website has become&nbsp;<strong>even more popula</strong>r in a very short time. In today's time, more than 1 million people use this website to download movies and web series.</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Tamilrockers</h2> <p>"+MOVIES_NAME+" Movie Download in<strong>&nbsp;</strong>Tamilrockers is one of the trending searches by the fans of "+MOVIES_NAME+" Movie Download in Tamilrockers is a pirated website that&nbsp;<strong>illegally&nbsp;</strong>leaks movies, web series, videos for free. If any movies are leaked by Tamilrockers, people should avoid using them and use the legal platform. By doing so would be a great support for the film industry.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/avatar-2-2022-hindi-dual-audio-1080p.html'> <blockquote>Avatar 2 Full Movie In Hindi Download Filmyzilla [320p, 480p, 720p, 4k Full HD] Mp4moviez, Filmymeet, Filmywap, Vegamovies</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in Filmywap</h2> <p>Doing piracy of the copy righted is illegal and it is considered a crime. People who search for "+MOVIES_NAME+" Movie Download in Filmywap this article is for you. On the torrent website, Filmywap users can download the latest movies, Bollywood movies, dubbed Hindi movies, etc. But using this torrent website is safe? No, it is not safe, as this is a third-party website it is illegal to use it. Avoid using torrent websites and start using legal platforms.&nbsp;&nbsp;</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in mp4moviez</h2> <p>"+MOVIES_NAME+" Movie Download in Mp4moviez leaks Hindi, Hollywood movies, Hindi dubbed movies for free. Once a movie is released, mp4moviez uploads the movie illegally on its website. It is a crime to piracy a movie and download a piracy movie. So people should avoid searching on "+MOVIES_NAME+" Movie Download in mp4moviez and use legal ways for streaming the movie.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/black-adam-2022-hindi-russian-english.html'> <blockquote>Black Adam Download In Hindi Telegram Link, Filmywap, Fillmyzilla, 123mkv, Mp4moviez [HD, 320p, 780p, 1080p]</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME_MIX+" Movie Download in Kuttymovies</h2> <p>Kuttymovies is also a pirated website famous for tamil movies download,"+MOVIES_NAME+" Movie Download in Hindi dubbed movies download. The content available on the torrent website Kuttymovies are all pirated contents. Users are allowed to download unlimited of movies from the torrent website.&nbsp;</p> <h3> <a href='https://www.needevery.in/2022/11/bhediya-2022-movie-1080p-720p-480p.html'> <blockquote>Bhediya Download Full Movie In Download Filmyzilla [320p, 480p, 720p, 4k Full HD] Mp4moviez, Filmymeet, Filmywap, Vegamovies</blockquote> </a> </h3> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>"+MOVIES_NAME+" Movie Download in iBomma</h2> <p>iBomma, this website also leaks Hollywood, Hindi, "+MOVIES_NAME+" Movie Download in Hindi movies for free. But using iBomma and other torrent wbeiste is not safe and we do not recommend to use torrent websites.&nbsp;</p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i>Types of subtitle</h2> <p>1. Subtitles:- These are the subtitles for&nbsp;<strong>"+MOVIES_NAME+" Movie Download in</strong>&nbsp;300MB intended for the viewer who does not understand the original language of the content. Not recommended for hearing impaired people.</p> <p>2. SDH:- These are the subtitles for<strong>&nbsp;"+MOVIES_NAME+" 2 Movie Download filmywap</strong>&nbsp;in 1080p intended for the viewer who does not understand the original language of content as well as audibly challenged or deaf. Highly Recommended for both hearing impaired audiences and foreign audiences who don't understand the specific language of the content.</p> <p>3. Closed Caption:- These are the subtitles for&nbsp;<strong>"+MOVIES_NAME+" Movie Download in</strong>&nbsp;<strong>tamilrockers&nbsp;</strong>intended for the viewer who is audibly challenged. Closed Captions are in the same language as the content.&nbsp;<strong>Not recommended for foreign&nbsp;</strong>audiences who don't understand that&nbsp;<strong>specific language.</strong></p> <h2><i aria-hidden='true' class='fa fa-plus-square'></i><strong>Disclaimer</strong></h2> <p>This website is for <strong>INFORMATION PURPOSE</strong> only. We neither provide any copyrighted content nor support piracy on this website through any of its article. Nevertheless, what we do give is News &amp; details easily available all over the internet. </p> </div> <script type='text/javascript'> domReady(() => { linkButton() }) function domReady(callback) { if (document.readyState === 'complete') { callback() } else { window.addEventListener('load', callback, false); } } function linkButton() { linkin = document.location.href; document.querySelector('.button__link').href = linkin; } </script>"
        TEMPLATE_ALL = TEMPLATE + TEMPLATE_2
        with open("post/"+TEXT_FILE_NAME, "w") as file:
            file.write(TEMPLATE_ALL)
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
        print("ERROR: ")  
        print(e)


