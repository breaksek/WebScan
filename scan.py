#!/usr/bin/env python
import re
import urllib
from headers import *
from vulnz import *

print ga.green+'''
               _    _      _     _____                 
	  		  | |  | |    | |   /  ___|                
			  | |  | | ___| |__ \ `--.  ___ __ _ _ __  
			  | |/\| |/ _ \ '_ \ `--. \/ __/ _` | '_ \ 
			  \  /\  /  __/ |_) /\__/ / (_| (_| | | | |
			   \/  \/ \___|_.__/\____/ \___\__,_|_| |_| 
 
        ###############################################################
        #| Source : https://github.com/zigoo0/webpwn3r               |#
        #|                                                           |#
        #| WebScan : Tools yang memiliki fungsi scan vuln pada website |#
        #|                                                           |#
        #|                                                           |#
	    #|                                                           |#
        ###############################################################
        '''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Scan URL or List of URLs? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] Enter the URL: ")
#		 if not url.startswith("http://"):
#		     Thanks to Nu11 for the HTTP checker
#                     print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
#                     exit()
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end			
			print ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Enter the list file name examp[list.txt] : "+ga.end)
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





