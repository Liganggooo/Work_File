
#练习使用包的封装
def pack():
	funcs = []
	for i in range(1,4):
		#开始循环的时候并没有运行pack2,所以只能算作一个标识符
		#所以徐娜换的时候并没有打印i
		# 如果我们在循环中使用pack（）调用函数
		#才会调用相应的print（i）
		def pack2():
			print(i)
		#这一步中funcs中存储的只是函数名，不是打印的值
		funcs.append(pack2)
	# num = 11

	return funcs

# f = pack()
# print(f)
# f[0]()
# f[1]()
# f[2]()

#对上一个案例进行改进
def modi():
	func = []
	for i in range(1,4):
		def modi1(num):
			def inner():
				print(num)
			return inner
		func.append(modi1(i))#在此处运行modi1
		# 并将i传递给num，借用inner打印num
	return func


m = modi()
# print(m)
m[0]()
m[1]()
m[2]()






