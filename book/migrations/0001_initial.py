# Generated by Django 2.1.7 on 2019-04-24 01:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import book.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='书籍名称')),
                ('link', models.FileField(upload_to=book.models.get_book_path, verbose_name='书籍链接')),
                ('img', models.ImageField(upload_to=book.models.get_img_path, verbose_name='书籍图片')),
                ('passwd', models.CharField(blank=True, max_length=10, null=True, verbose_name='下载密码')),
                ('introduce', models.TextField(verbose_name='书籍介绍')),
                ('views', models.IntegerField(default=0, verbose_name='下载次数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('status', models.CharField(choices=[('上线', '上线'), ('下线', '下线')], default='上线', max_length=10,
                                            verbose_name='状态')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类名称',
                'verbose_name_plural': '分类名称',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateTimeField(auto_now_add=True, verbose_name='阅读时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '阅读历史',
                'verbose_name_plural': '阅读历史',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=10, verbose_name='标签名')),
                ('book',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('book',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='书籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                           verbose_name='用户')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Cate', verbose_name='书籍分类'),
        ),
    ]
