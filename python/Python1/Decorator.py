
#尝试制作一个装饰器
def get_dec(func_name):   #给装饰器增加一个参数
	def dec(func):
		def inner(*args,**kwargs):
			print(func_name + "Caculate:")
			return func(*args,**kwargs)
		return inner
		#该函数相当于sun = dec(sum)
	return dec   #返回一个装饰器

@get_dec('sum')  #传递一个参数
def sum(a,b):
	return a + b
	
@get_dec('dif')
def dif(a,b):
	return a - b

@get_dec('mul')
def mul(a,b):
	return a * b
	
@get_dec('div')
def div(a,b):
	return a / b

a,b = 9,8
print(sum(a,b))
print(dif(a,b))
print(mul(a,b))
print(div(a,b))





