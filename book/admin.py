from django.contrib import admin

from .models import *


# Register your models here.

class CateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'img', 'passwd', 'cate', 'views', 'create_time', 'status']
    list_editable = ['status', 'passwd']
    list_filter = ['cate', 'status']
    search_fields = ['introduce']


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'label']


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'view_date']
    list_filter = ['user', 'book', 'view_date']


admin.site.register(Cate, CateAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Likes, )
admin.site.register(History, HistoryAdmin)
