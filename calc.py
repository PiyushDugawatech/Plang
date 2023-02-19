import parser

while True:
    text = input('calc ==>  ')
    result, error = parser.run('<stdin>', text)
    if(text == "quit()"):
    	exit()
    elif(error):
    	print(error.as_string())
    else:
    	print(result)