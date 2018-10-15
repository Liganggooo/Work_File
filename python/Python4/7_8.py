responses = {}
while True:
	name = input("\nwhat is you name? ")
	response = input("if you could visit one place in the world,where would you go? ")
	responses[name] = response
	repeat = input("would you like ro let another people response?(yes/no) ")
	if repeat == 'no':
		break
print("\n...polling result...")
for name,response in responses.items():
	print(name + " want to go to " + response + ".")
