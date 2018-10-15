def make_album(name,album_name,song_num=''):
	"""make a album dic"""
	music_album={'name':name.title(),'album_name':album_name}
	if song_num:
		music_album['song_num']=song_num
	return(music_album)
	
name_prompt = "\nplease tell us your fvorite singer: "
album_name_prompt = "What album are you thinking of? "
print("(enter 'p' at any time to quit)")
while True:
	name = input(name_prompt)
	if name == 'q':
		break
	album_name = input(album_name_prompt)
	if album_name == 'q':
		break
	album_names = make_album(name,album_name)
	print(album_names)
print("thank you for your responding?")
