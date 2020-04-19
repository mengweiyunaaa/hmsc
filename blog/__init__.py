
import sys
import click
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user


#配置数据库时报错
WIN = sys.platform.startswith('win')
if WIN:
    pre =  'sqlite:///'
else:
    pre =  'sqlite:////'


#定义
app = Flask(__name__)
#配置
app.config['SQLALCHEMY_DATABASE_URI'] = pre + os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db')) + '?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev')







db = SQLAlchemy(app)



