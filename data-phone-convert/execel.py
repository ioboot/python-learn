# -*- coding: utf-8 -*-
import pandas
import codecs

source_file = 'D:/workspace/python/python-learn/data-phone-convert/data_phone_20210304_pro.xlsx'
dest_file = 'D:/workspace/python/python-learn/data-phone-convert/20210304-473270-SR-UTF8.txt'

df = pandas.read_excel(
    source_file, dtype=object)

# # 读取行列数据及索引
# print(len(df.index.values))  # 行数 不包含表头
# print(df.index.values)  # 行索引
# print(len(df.columns.values))  # 列数
# print(df.columns.values)  # 列索引

# # 读取指定单行或多行数据
# data = df.loc[0].values
# print('第0行数据：\n', data)
# data = df.loc[[1, 2]].values
# print('第1和2行数据：\n', data)

# # 读取指定列或多列数据
# data = df.iloc[:, 0].values
# print('第0列数据：\n', data)
# data = df.iloc[:, [1, 2]].values
# print('第1和2列的数据：\n', data)

# # 读取单元格数据或部分数据
# data = df.iloc[1, 2]
# print(data)
# data = df.iloc[[1, 2], [1, 2]].values
# print(data)

# # 输出满足条件的数据
# writer = pandas.ExcelWriter(
#     'D:/workspace/python/data_phone_20210107_pro_liaocheng.xlsx')
# temp = []
# for i in range(len(df.index.values)):
#     if df.iloc[i, 3] == '聊城市':
#         temp.append(df.iloc[i].values)
# df2 = pandas.DataFrame(data=temp, columns=df.columns.values)
# df2.to_excel(writer, 'Sheet', index=False)
# writer.save()

data = pandas.np.array(df).tolist()

with codecs.open(dest_file, 'w', 'utf-8') as f:
    for i in range(len(data)):
        if i < 1:
            continue
        arry = data[i][1:10]
        # 交换末尾数据
        arry[len(arry)-1], arry[len(arry) - 2] = arry[len(arry) - 2], arry[len(arry)-1]
        # 合并中间数据
        arry[3] = arry[3] + ' ' + arry[4]
        str_row = '"'+str(i)+'",'  # 追加索引
        for j in range(len(arry)):
            # 剔除无用数据
            if j in [1, 2, 4, 6]:
                continue
            str_row = str_row + '"'+str(arry[j])+'",'  # 添加字符
        f.writelines(str_row[:-1]+'\n')
        print(i)
