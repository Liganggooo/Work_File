alien_colors=['green','yellow','red']
alien_colors.pop(1)
for alien_color in alien_colors:
	if alien_color == 'green':
		print("you killed a " + alien_color + " alien,get five points!" )
	elif alien_color == 'yellow':
		print("you killer a " + alien_color + " alien,get ten points!")
	else:
		print("you killer a " + alien_color + " alien,get fifteen points!")
