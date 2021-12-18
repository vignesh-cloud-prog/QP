from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserOTP(models.Model):
	"""
    Stores randomly generated user OTP, related to :model:`users.UserOTP` and
    :model:`auth.User`.
    """
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.IntegerField()

	def __str__(self):
		return f"{self.user}-{self.otp}"
