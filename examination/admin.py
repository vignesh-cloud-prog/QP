from django.contrib import admin
from .models import UserOTP,Practice,Profile

# Register your models here.
admin.site.register(UserOTP)
admin.site.register(Practice)
admin.site.register(Profile)