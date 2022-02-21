from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ExaminationType)
admin.site.register(GoverningBody)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(Subject)