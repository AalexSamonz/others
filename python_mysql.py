import MySQLdb

# 连接数据库
conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='password', db='database')

# 创建游标
cursor = conn.cursor()

# 执行查询
cursor.execute('SELECT c FROM b')

# 获取结果
results = cursor.fetchall()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

# 输出结果
for result in results:
    print(result[0])
