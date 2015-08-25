#!/usr/bin/python

import MySQLdb


class connMysql:
	def connMysql(self,statement="select * from blogapp_categoryname"):
		try:
			conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='blog',port=3306)
			cur = conn.cursor()
			cur.execute(statement)
			result = []
			for line in cur.fetchall():
				 result.append(line)
			cur.close()
			conn.commit()
			conn.close()
			return result
		except MySQLdb.Error,e:
			return 0
			print "Mysql Error msg: ",e
#a = connMysql()
#b = "select category_name,count(category_name) as count from blogapp_categoryname,blogapp_article where category_id =  blogapp_categoryname.id group by category_name;"
#print  a.connMysql(b)
#for i in c:
#	print i[0]


