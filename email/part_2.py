#!/usr/bin/python
# -*- coding: UTF-8 -*-

from imap_tools import MailBox, AND
from bs4 import BeautifulSoup
import re

# get list of email subjects from INBOX folder
with MailBox('outlook.office365.com').login('wujk@ucssi.com', 'Xhsd@2013', initial_folder='INBOX/招聘') as mailbox:
    # LIST
    # for f in mailbox.folder.list('INBOX'):
    #     print(f)  # {'name': 'INBOX|cats', 'delim': '|', 'flags': ('\\Unmarked', '\\HasChildren')}
    print(mailbox.fetch())
    for msg in mailbox.fetch(AND(subject='51job.com')):  # 前程无忧
        try:
            soup = BeautifulSoup(msg.html, features="html.parser")
            re_phone = soup.find('td', text=re.compile(
                '.*?手机.*?')).find_next_siblings('td')
            re_job = soup.find('td', text=re.compile(
                '.*?应聘职位.*?')).find_next_siblings('td')
            re_email = soup.find(href=re.compile("mailto"))
            print(
                f"{msg.subject.split('－')[1]} {re_phone[0].string} {re_email.string} {re_job[0].string.split(' ')[0]}")
        except Exception:
            print(Exception.__str__)
            continue
    for msg in mailbox.fetch(AND(subject='Zhaopin.com')):  # 智联招聘
        try:
            soup = BeautifulSoup(msg.html, features="html.parser")
            re_phone = soup.find('td', text=re.compile(
                '.*?手机.*?')).find_next_siblings('td')
            re_job = soup.find('td', text=re.compile(
                '.*?应聘职位.*?')).find_next_siblings('td')
            re_email = soup.find(href=re.compile("mailto"))
            print(
                f"{msg.subject.split('－')[1]} {re_phone[0].string} {re_email.string} {re_job[0].string.split(' ')[0]}")
        except Exception:
            print(Exception.__str__)
            continue