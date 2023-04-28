from django.contrib import admin
from proxymodelapp.models import *

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Google)
admin.site.register(Fb)

