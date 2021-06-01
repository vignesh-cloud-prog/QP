from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Provider(models.Model):
    name=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default="user",blank=True,null=True)
    # All fields used below are same as Question_paper model inter changebly used between universities and boards related items
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=12,choices=PAPER_CHOICES) 
    college = models.CharField(max_length=100)
    board=models.CharField(max_length=100)
    claass = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    sub= models.CharField(max_length=100)
    papertitle=models.CharField(max_length=100)
    doc = models.FileField(upload_to='provider')
    provide_date=models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return  self.paper_type +' , '+self.board + ' - '+ self.sub 