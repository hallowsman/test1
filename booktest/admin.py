from django.contrib import admin
from .models import *


# class HeroInfoAdmin(admin.ModelAdmin):
#     def gender(self):
#         if self.hgender:
#             return '男'
#         else:
#             return '女'
#
#         gender.short_description = '性别'
#
#     list_display = ['id', 'hname', 'gender', 'hcontent']


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle', 'bpub_date']
    list_filter = ['btitle', 'bpub_date']
    search_fields = ['btitle', 'bpub_date']
    list_per_page = 10
    fieldsets = [('基础信息', {'fields': ['btitle']}), ('更多', {'fields': ['bpub_date']})]
    inlines = [HeroInfoInline]


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
