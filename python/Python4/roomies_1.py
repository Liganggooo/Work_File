roomies = {
    'zudabing':'weilin',
    'shaojunjie':'sinan',
    'huaixinwen':'xinyi',
    }
roomies['zudabing'] = 'caohai'
for key,value in roomies.items():
	print("the " + key.title() + " run though " + value.title())
	print(key.title())
	print(value.title())
for name in roomies.keys():
	print("\nname:")
	print(name.title())
for ad in roomies.values():
	print("\nad:")
	print(ad.title())
