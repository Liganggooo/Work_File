prompt = "\nhow old are you?"
prompt += "\n please write you age: "
massages = ""
while True:
	 massages = input(prompt)
	if massages == 'quit':
		break
	massages = int(input(prompt))
	if massages <= 3:
		price = "0"
	elif massages <=12:
		price = "10"
	elif massages >12:
		price = "15"
	print("you should pay " + price + " doller!")