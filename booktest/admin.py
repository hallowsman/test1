from django.contrib import admin
from .models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle', 'bpub_date']
    list_filter = ['btitle', 'bpub_date']
    search_fields = ['btitle', 'bpub_date']
    list_per_page = 1
    fieldsets = [('基础信息', {'fields': ['btitle']}), ('更多', {'fields': ['bpub_date']})]


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
