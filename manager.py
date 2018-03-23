# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 下午3:05
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : manager.py
# @Software: PyCharm

from app import create_app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_content():
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_content))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)
