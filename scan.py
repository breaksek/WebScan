#!/usr/bin/env python
import os, re, urllib, time
from headers import *
from vulnz import *

os.system("clear")
print ga.green+'''
                   _    _      _     _____                            
	  	  | |  | |    | |   /  ___|                           
		  | |  | | ___| |__ \ `--.  ___ __ _ _ __             
		  | |/\| |/ _ \ '_ \ `--. \/ __/ _` | '_ \            
		  \  /\  /  __/ |_) /\__/ / (_| (_| | | | |           
		   \/  \/ \___|_.__/\____/ \___\__,_|_| |_|           
                                                                      
        ##############################################################
        #|                                                          |#
        #|  "WebScan" merupakan adopsi dari "WebPwn3r"              |#
        #|  By : breaksek                                           |#
        #|  Tiktok : https://tiktok.com/@breaksek                   |#
        #|  Author : zigoo0                                         |#
      	#|  Source : https://github.com/zigoo0/webpwn3r             |#
        #|                                                          |#
        ##############################################################
        '''+ga.end

def urls_or_list():
        print ga.blue+'''
 [?] Pilih methode Scan :
     1. Scan dari link/url yang dimasukkan.
     2. Scan dari file daftar target examp(list.txt).
'''+ga.end
	url_or_list = raw_input("  [!] Methode (1/2) : ")
	if url_or_list == "1":
	 	 url = raw_input("  [!] Masukkan link/url examp(https://site.com/product.php?id=1) : ")
		 #if not url.startswith("http://"):
		     #Thanks to Nu11 for the HTTP checker
                     #print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
                     #exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
			print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Enter the list file name .e.g [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [!] Now Scanning %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end				
				print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
		 exit()				
urls_or_list()
os.system("mpv kerjabagus.mp3")




