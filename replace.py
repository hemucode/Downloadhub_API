#!/usr/bin/env python3
import os
import json
import subprocess

os.system('color')

DATA_FILE = 'data.json'
POST_FILE = 'post.json'
with open(POST_FILE) as POST_DATA:
    POST = json.load(POST_DATA)
with open(DATA_FILE) as MAIN_DATA:
    DATA = json.load(MAIN_DATA)

try:
    MOVIES_NAME = POST['MOVIES_NAME']
    MOVIES_NAME_MIX = POST['MOVIES_NAME_MIX']
    MOVIES_STORY = POST['MOVIES_STORY'] 
    MOVIES_IMG = POST['MOVIES_IMG']
    MOVIES_DATE = POST['MOVIES_DATE']
    MOVIES_IMDB = POST['MOVIES_IMDB']
    TEMPLATE = DATA["TEMPLATE"]

    if TEMPLATE:
        if TEMPLATE == 1 or TEMPLATE == 2 or TEMPLATE == 3 or TEMPLATE == 4 or TEMPLATE == 5 :
            if MOVIES_NAME and MOVIES_NAME_MIX and MOVIES_IMG:
                if TEMPLATE == 1:
                    print("")
                    print('\033[94m' + "[+] SELECT TEMPLATE 1" + '\033[0m')
                    print("")
                    subprocess.Popen('python template_1.py', shell=True)

                if TEMPLATE == 2 :
                    print("")
                    print('\033[94m' + "[+] SELECT TEMPLATE 2" + '\033[0m')
                    print("")
                    subprocess.Popen('python template_2.py', shell=True)

                if MOVIES_DATE and MOVIES_IMDB and TEMPLATE == 3:
                    print("")
                    print('\033[94m' + "[+] SELECT TEMPLATE 3" + '\033[0m')
                    print("")
                    subprocess.Popen('python template_3.py', shell=True)

                if TEMPLATE == 4:
                    print("")
                    print('\033[94m' + "[+] SELECT TEMPLATE 4" + '\033[0m')
                    print("")
                    subprocess.Popen('python template_4.py', shell=True)
                
                if TEMPLATE == 5:
                    print("")
                    print('\033[94m' + "[+] SELECT TEMPLATE 5" + '\033[0m')
                    print("")
                    subprocess.Popen('python template_5.py', shell=True)
            else:
                print("")
                print('\033[93m' +"[+] POST DATA NOT FOUND WAIT..."+ '\033[0m')
                print("")
                DATA['STATUS'] = 2  
                json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
                subprocess.Popen('python edit.py', shell=True)

        else:
            print("")
            DATA["TEMPLATE"] = int(input('\033[93m' +"UPLOAD TEMPLATE NUMBER: "+ '\033[0m'))
            json.dump(POST, open(POST_FILE, "w"), indent = 2)
            json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
            subprocess.Popen('python replace.py', shell=True)
    else:
        print("")
        DATA["TEMPLATE"] = int(input('\033[93m' + "UPLOAD TEMPLATE NUMBER: " + '\033[0m'))
        print("")
        json.dump(POST, open(POST_FILE, "w"), indent = 2)
        json.dump(DATA, open(DATA_FILE, "w"), indent = 2)
        subprocess.Popen('python replace.py', shell=True)

except Exception as e:   
        print("ERROR: replace.py")  
        print(e)


