import json
while True:
	name = input("Name: ")
	account = input("Account: ")
	password = input("Password: ")
	age = int(input("Age: "))
	location = input("location: ")
	
	users,user = [],{}
	user['name'] = name
	user['accounr'] = account
	user['password'] = age
	user['location'] = location
	users.append(user.copy())
	break

filename = 'users.json'
with open(filename,'w') as f:
	json.dump(users,f)
	
