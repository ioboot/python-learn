import os
import re

"""将当前目录下所有文档进行替换操作"""


def change_str(path):
    str_pattern = r"更多课程请加QQ1046877154，微信loveu_110获取"
    str_new = r"更多课程请加请加微信babelman-com"
    path_list = os.listdir(path)
    for file in path_list:
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):
            if re.search('(\.html)', file):
                print(abs_path)
                with open(abs_path, 'r', encoding="utf-8") as f:
                    str_all = f.read()
                with open(abs_path, 'w', encoding="utf-8") as f:
                    f.write(re.sub(str_pattern, str_new, str_all))
                # 修改文件名001
            # if ".下载" in abs_path:
            #         new_name = re.sub("\.下载", '', abs_path)
            #         os.rename(abs_path, new_name)
        else:
            change_str(abs_path)


change_str(os.path.abspath(r'C:\Users\ioboot\Desktop\25 AI技术内参\html'))
