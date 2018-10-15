#写一个运算任意阶乘的递归函数

def fac(n):
	if n == 1:
		return 1
	return n * fac(n - 1)

res = fac(6)
print(res)














