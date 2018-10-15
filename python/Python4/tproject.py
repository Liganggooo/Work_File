import json
def user_log(account,password):
	filename = 'users.json'
	with open(filename) as f:
		x = json.load(f)
		print(x)
		user_1 = x[0]
		print(account)
	if user_1['accounr'] == account:
		if user_1['password'] == password:
			print("welcome back %s" % user_1['name'])
		else:
			print("Your Password: %s is FALSE" % password)
	else:
		print("You account: %s is False" % user_1['accounr'])
	return account,password
account = input(("enter you account: "))
password = input(("enter you password: "))
			
user_log(account,password)


