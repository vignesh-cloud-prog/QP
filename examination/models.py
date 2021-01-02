from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.IntegerField()

class Practice(models.Model):
	student=models.ForeignKey(User, on_delete=models.CASCADE)
	content = RichTextUploadingField()