from django.contrib import admin

from .models import Winery, Wine, Grape, County
# Register your models here.
admin.site.register(Winery)
admin.site.register(Wine)
admin.site.register(Grape)
## registering county model for testing,
## but will remove it once full data is loaded
admin.site.register(County)