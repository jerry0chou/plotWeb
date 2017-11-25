#encoding: utf-8

import os

# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC_DATA = os.path.join(APP_ROOT, 'static/data') #设置一个专门的类似全局变量的东西