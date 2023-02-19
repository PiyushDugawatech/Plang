
'''
Author : Piyush Dugawa
Credits : GeeksforGeeks.com, CodePulse(yt channel)
Language Used : Python
Licenced to : PD TECH ZONE
'''

#importing modules

import os
from funcs import functions, version
import time

#greetings

greet = f'Plang {version} | [{time.ctime()}] |\nPlang on Python\nType "help", "Copyright", "Credits" or "License" for more information.'

print(greet)

#main loop

while True : 

	b = input("==> ") #input from user
	
	#commanding
	
	d = functions()
	d.work(b)