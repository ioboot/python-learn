import os
from posixpath import abspath
import re
import pdfkit


def html2pdf(path):
    try:
        path_list = os.listdir(path)
        path_array = []
        for file in path_list:
            abs_path = os.path.join(path, file)
            out_path = os.path.join(path,file.split('.html')[0]+'www.babelman.com.pdf')

            config = pdfkit.configuration(
                wkhtmltopdf=r"D:\soft-repo\wkhtmltopdf\bin\wkhtmltopdf.exe")
            pdfkit.from_file(abs_path, out_path, configuration=config)
        # if re.search('(\.html)', file):
        #     with open(abs_path, 'r', encoding="utf-8") as f:
        #         config = pdfkit.configuration(wkhtmltopdf=r"D:\soft-repo\wkhtmltopdf\bin\wkhtmltopdf.exe")
        #         pdfkit.from_file(f,'out.pdf',configuration=config)
    except Exception as e:
        print(e)


html2pdf(r"C:\Users\ioboot\Desktop\34 玩转VS Code\pdf")
