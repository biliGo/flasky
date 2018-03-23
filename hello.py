# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 下午3:30
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : hello.py
# @Software: PyCharm


from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lessguo@163.com'
app.config['MAIL_PASSWORD'] = '********'
mail = Mail(app)

if __name__ == '__main__':
    from flask_mail import Message
    msg = Message('test subject', sender='lessguo@163.com', recipients=['guoxiangyang@quhuanqian.cn'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)
