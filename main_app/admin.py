from django.contrib import admin

from .models import Winery, Wine, Grape, County, Comment
# Register your models here.
admin.site.register(Winery)
admin.site.register(Wine)
admin.site.register(Grape)
admin.site.register(Comment)