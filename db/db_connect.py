import pymysql

# 打开数据库连接
__connection = pymysql.connect(host='localhost',
                               user='root',
                               password='qwe159852',
                               database='dianpingdb')

# 使用 cursor() 方法创建一个游标对象 cursor
__cursor = __connection.cursor()


def replace_recommend(user_id, recommend_shop_id_list):
    sql = f'REPLACE INTO recommend(id,recommend) VALUES({user_id},"{recommend_shop_id_list}")'
    __cursor.execute(sql)
    __connection.commit()


def select_recommend(user_id):
    sql = f'SELECT * from recommend where  id={user_id}'
    # 使用execute方法执行SQL语句
    __cursor.execute(sql)

    # 使用 fetchone() 方法获取一条数据
    return __cursor.fetchone()
