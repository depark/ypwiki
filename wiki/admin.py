from django.contrib import admin
from wiki.models import *

# Register your models here.



class MyAdminSite(admin.AdminSite):
    site_title = 'ypwiki 后台'
    site_header = 'wiki backup'
    index_title = 'wiki managment'

admin_site=MyAdminSite()

class Pro_Admin(admin.ModelAdmin):
    list_display = ('id','name','owner','create_time')


class Arti_Admin(admin.ModelAdmin):
    list_display = ('id','title','create_user','create_time','last_update_user','last_update_time')


admin_site.register(Project,Pro_Admin)
admin_site.register(Article,Arti_Admin)
admin_site.register(User)
admin_site.register(Group)