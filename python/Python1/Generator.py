
#写一个生成器
# g = (i for i in range(1,10) if i % 2== 0)

# for l in g:
	# print(l)
# try:
# 	print(next(g))
# 	print(next(g))
# 	print(next(g))
# 	print(next(g))
# 	print(next(g))
# except StopIteration:
# 	print('The number was run out')

#斐波那契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n += 1
	return 'The number was run out'


# f = fib(3)
# print(next(f))  # 使用next一个一个的吧生成器中的数据提取出来
# print(next(f))
# print(next(f))
# print(next(f))


#用遍历的方式，将生成器的当中数字提取出来
f = fib(10)
for g in f:
	print(g)

#用while循环的方法进行遍历
# f = fib(6)
# while True:
# 	try:
# 		g = next(f)
# 		print(g)
# 	except StopIteration as e:
# 		print(e.value)
# 		break


#简洁生成器yield使用案例


# def gene():
# 	yield 1
# 	print('a')

# 	yield 2
# 	print('b')

# 	yield 3
# 	print('c')

# g = gene()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())





