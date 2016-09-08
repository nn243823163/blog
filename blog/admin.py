#coding:utf-8
from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    #引入富文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.9/kindeditor-min.js',
            '/static/js/kindeditor-4.1.9/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.9/config.js',
        )

# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ad)
admin.site.register(Links)