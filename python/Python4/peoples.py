aliens = []
for alien_num in range(10):
	new_alien = {'color':'red','speed':'medium','point':10}
	aliens.append(new_alien)
for alien in aliens[:3]:
	print(alien)
print("  ...")

print("total number of alien: " + str(len(aliens)))
for alien in aliens[:2]:
	if alien['color']=='red':
		alien['color']='blue'
		alien['speed']='fast'
		alien['point']=15
for alien in aliens[:6]:
	print(alien)
print('...')
