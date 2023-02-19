
#importing modules

import parser
import lexer
import os

#writing functions

version = "v3.1.0"

class functions:
	
	#main function
	
	def work(self, c):
		
		
		keys = '''
print  -->  Prints the statement written just after a space.
		
echo  -->  Prints the statement written just after a space.

plang --<function>  --> aquires the function.(get function list from plang.in)

typecast <expression> --> gives type of expression.

calc <expression> --> calculates given expression.
'''
		
		#variable assignment
		
		digits = [0,1,2,3,4,5,6,7,8,9]
		f1 = open('compiler.py', 'r')
		
		#command conditions
		
		if("#" in c):
			c = ""
		
		if ("echo" in c):
			if ("\n" not in c):
				c = c[5:]
				print(c)
			else:
				c = c[5:]
				c = c[:-1]
				print(c)
		elif("print(" in c):
			if("\n" not in c):
				c = c[7:]
				c = c[:-2]
				print(c)
			else:
				c = c[7:]
				c = c[:-3]
				print(c)
		elif("print (" in c):
			c = c[8:]
			c = c[:-3]
			print(c)
		elif("print" in c):
			if ("\n" not in c):
				c = c[6:]
				print(c)
			else:
				c = c[6:]
				c = c[:-1]
				print(c)
		elif("open" in c):
			c = c[5:]
			try:
				with open('filepath.txt', 'w') as f:
					f.write(c)
			except Exception as e:
				print ("There was an error: " + str(e))
		elif(c == "\n"):
			pass
		elif(c == ""):
			pass
		elif(c == "ls"):
			print(os.listdir())
		elif(c == "plang --version" or c == "plang --version\n" ):
			print("Version intalled : Plang " + version)
		elif(c == "plang --keywords" or c == "plang --keywords\n" or c == "help"):
			print(keys)
		elif(c == "Credits" or c == "credits"):
			print('''
Author : Piyush Dugawa
Credits : GeeksforGeeks.com, CodePulse(yt channel)
			''')
		elif(c == "License" or c == "license"):
			print("Licensed to : PD TECH ZONE")
		elif(c == "copyright" or c == "Copyright"):
			
			print("©Copyright 2022-23")
		elif("typecast" in c):
			c = c[9:]
			c = c[:-1]
			result, error = lexer.run('<stdin>', c)
			if error:
				print(error.as_string())
			else:
				print(result)
		elif("calc" in c):
			if ("\n" not in c):
				c = c[5:]
				result, error = parser.run('<stdin>', c)
				if error:
					print(error.as_string())
				else:
					print(result)
			else:
				c = c[5:]
				c = c[:-1]
				result, error = parser.run('<stdin>', c)
				if error:
					print(error.as_string())
				else:
					print(result)
		elif (c == "quit()"):
			print("Successfully completed process.")
			exit()
		else:
			print("Invalid Input!!!")