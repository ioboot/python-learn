# -*- coding:utf-8 -*-

import pymysql


def get_data():
    db = pymysql.connect(host='localhost', user='root',
                         password='password@1', database='babelman')
    cursor = db.cursor()
    sql = 'select * from users;'
    try:
        cursor.execute(sql)

        data = cursor.fetchall()

        # for row in data:
        #     for col in range(len(row)):
        #         print(row[col])
        print(data)
    except:
        print("Error: unable to fetch data")
    db.close()


def update_data():
    db = pymysql.connect(host='localhost', user='root',
                         password='password@1', database='babelman')
    cursor = db.cursor()
    sql = 'update users set user_name = replace(replace(user_name,char(10),''),char(13),''),user_email = replace(replace(user_email,char(10),''),char(13),''),user_phone = replace(replace(user_phone,char(10),''),char(13),'');'
    try:
        cursor.execute(sql)

        db.commit()
    except:
        print("Error: unable to update data")
        db.rollback()
    db.close()


if __name__ == "__main__":
    # update_data()
    get_data()
