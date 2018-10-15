
#caculate reading comprehension total score
#decorator 
def deco(func):
	def inner(*args):
		print("Total score:")
		return func(*args)
	return inner


#caculate  score
#@deco
def caculate(module):
	#reading comprehension
	#@deco
	def RCscore():
		sA = int(input('Reading compreheension sectionA correct number: '))
		sB = int(input('Reading compreheension sectionB correct number: '))
		sC = int(input('Reading compreheension sectionC correct number: '))
		@deco
		def score1():
			score3 = 3.55*sA+7.1*sB+14.2*sC
			print(score3)
			if score3 < 149.1:
				print("Maybe you're fooler")
			elif score3 >= 149.1:
				print("Good job")
		return score1
	#Listening comprehension
	#@deco
	def LCscore():
		sA = int(input('Listening compreheension sectionA correct number: '))
		sB = int(input('Listening compreheension sectionB correct number: '))
		sC = int(input('Listening compreheension sectionC correct number: '))
		@deco
		def score2():
			score4 = 7.1*sA+7.1*sB+14.2*sC
			print(score4)
			if score4 < 149.1:
				print("Maybe you're idiot!")
			elif score4 >= 149.1:
				print("Good job!")
		return score2
	
	#if
	if module == 'rc':
		return RCscore
	if module == 'lc':
		return LCscore
	
#Total_RCscore = 10*3.5+10*7.1+10*14.2
prompt ='Enter a module you want select:'
prompt += '\n(Reading comprehension/rc)'
prompt += '\n(Listening comprehension/lc)'	
m = input(prompt)
res = caculate(m)
res()()














