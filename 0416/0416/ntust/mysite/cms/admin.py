from django.contrib import admin

from .models import Uname,Gender,Birth,Introduction
# Register your models here.
admin.site.register(Uname)
admin.site.register(Gender)
admin.site.register(Birth)
admin.site.register(Introduction)