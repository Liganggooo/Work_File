import pymysql

#打开数据库连接
db = pymysql.connect('localhost','root','lg083533','student')
#创建游标对象
cursor = db.cursor()

# 查询数据库中的数据
# sql = 'select * from stu'
# try:
# 	cursor.execute(sql)
# 	#提取第一行
# 	# student = cursor.fetchone()
# 	#提取所有行
# 	students = cursor.fetchall()
# 	for student in students:
# 		# print(type(student))
# 		print(student)
# except Exception as ex:
# 	print(ex)

#插入一条记录
# sql = 'insert into stu values (%s,%s,%s,%s)'
# try:
# 	cursor.execute(sql,('陈德凤','20150108020129','15285381046','贵州'))
# 	db.commit()

# except Exception as ex:
# 	db.rollback()
# 	print(ex)

#条件查询
# sql = 'select * from stu where 年龄 >= %s'
# try:
# 	cursor.execute(sql,(20))
# 	students = cursor.fetchall()
# 	for student in students:
# 		stu_num = {
# 			'name':student[0],
# 			'sc_num':student[1],
# 			'age':student[2],
# 			'tel':student[3],
# 			'address':student[4]}
# 		print(stu_num)
# except Exception as ex:
# 	print(ex)

#创建一个表
# try:
# 	cursor.execute("drop table if exists stuff")

# 	sql = 'create table stuff(name char(8) not null,age char(2))'


# 	cursor.execute(sql)

# except Exception as ex:
# 	print(ex)

#插入一条记录
# sql = 'insert into stuff values (%s,%s)'
# try:
# 	cursor.execute(sql,('陈德凤',20))
# 	db.commit()

# except Exception as ex:
# 	db.rollback()
# 	print(ex)

# 查询数据库中的数据
# sql = 'select 电影,豆瓣评分 from doubanmovies where 豆瓣评分 >= 8 \
# order by 豆瓣评分 desc'
# try:
# 	cursor.execute(sql)
# 	#提取第一行
# 	# student = cursor.fetchone()
# 	#提取所有行
# 	students = cursor.fetchall()
# 	for student in students:
# 		# print(type(student))
# 		print(student)
# except Exception as ex:
# 	print(ex)


# sql = 'select 电影,豆瓣评分 from doubanmovies where 豆瓣评分 >= %s \
# order by 豆瓣评分 desc'%('8')
# try:
# 	cursor.execute(sql)
# 	#提取第一行
# 	# student = cursor.fetchone()
# 	#提取所有行
# 	students = cursor.fetchall()
# 	for student in students:
# 		# print(type(student))
# 		print(student)
# except Exception as ex:
# 	print(ex)

sql = 'select 电影,豆瓣评分 from doubanmovies where 电影 like '%s'' % ('爱%')
try:
	cursor.execute(sql)
	#提取第一行
	# student = cursor.fetchone()
	#提取所有行
	students = cursor.fetchall()
	for student in students:
		# print(type(student))
		print(student)
except Exception as ex:
	print(ex)

cursor.close
db.close
