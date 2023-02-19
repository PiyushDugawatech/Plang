
'''
Author : Piyush Dugawa
Language Used : Python
Licenced to : ABC Company
'''

import sys
from funcs_compiler import functions

#reading file
if __name__ == "__main__" :
	'''
	file_path = sys.argv[0]
	f1 = open(file_path, 'r')
	path = f1.readline()
	f1.close()
	'''
	f = open(sys.argv[1], 'r')
	count = 0

	#starting loop
	
	while True:
		
		#increamentation
		
		count += 1
		k = f.readline()
		
		if not k:
			break
		
		#functioning
		
		d = functions()
		d.work(k)