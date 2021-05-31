#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import emails
from emails.template import JinjaTemplate as T


USERNAME = 'wujk@ucssi.com'
PASSWORD = 'Xhsd@2013'
smtp_conf = {'host': 'smtp.office365.com',
             'user': USERNAME,
             'password': PASSWORD,
             'port': 587,
             'tls': True}


def send_email(to_email):

    html = """
    <html>  
    <head></head>  
    <body>  
        <p>Hi!<br>  
        How are you?<br>  
        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
        </p> 
        <img src="https://img-blog.csdnimg.cn/20200813165242761.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNTk2NzM0,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
    </body>  
    </html>  
    """
    message = emails.html(subject=T('测试邮件'),
                          html=T(html),
                          mail_from=('Jack.Wu', USERNAME))
    # message.attach(data=open('readme.md', 'r'), filename="readme.txt")
    r = message.send(to=(to_email), smtp=smtp_conf)
    print(r)


def office365():
    import smtplib
    mailserver = smtplib.SMTP('smtp.office365.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(USERNAME, PASSWORD)
    mailserver.sendmail(USERNAME, USERNAME, 'python email')
    mailserver.quit()


if __name__ == "__main__":
    send_email('wujikun@honghe-tech.com')
