f = open('text.txt','r')

# f.write('abc')
# content = f.read()
#将文件存入一个列表中然后对列表进行遍历
lines = f.readlines()
for line in lines:
	print(line.strip())

# print(content)
f.close
#免关闭文件式阅读文件方法
# filename = 'text.txt'
# with open(filename) as f:
	# content = f.read()
# print(content)

# #写入文件、追加文件位置
# with open(filename,'a') as f:
# 	f.write('123')
# with open(filename,'r') as f:
	# content = f.read()
# print(content)




