# coding:utf-8

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.extend(['E:\\web\\itbook', ])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
application = get_wsgi_application()
import django

django.setup()
from itbook.models import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'media')

file_dir = "book\\Linux"

root_dir = os.path.join(BASE_DIR, file_dir)
print(root_dir)
for i in os.listdir(root_dir):
    print(file_dir, i)
    # video_duration = get_duration(os.path.join(root_dir, i))
    # img_name = get_video_img(os.path.join(root_dir, i))
    # 插入书籍数据
    v = Book.objects.get_or_create(
        name=i.split('.')[0],
        link=os.path.join(file_dir, i),
        img=os.path.join(file_dir, 'book_cover.jpg'),
        # passwd = “”
        introduce="Linux相关书籍",
        cate=Cate.objects.get(name='Linux')
    )
    print("》》》插入书籍成功！")
