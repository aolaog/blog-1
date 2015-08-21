from django.contrib import admin
from blogapp.models import *
# Register your models here.


class articleAdmin(admin.ModelAdmin):
        list_display = ('title','author','view_count','comment_count','publish_date')

admin.site.register(article,articleAdmin)
admin.site.register(userinfo)
