from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Provide(models.Model):
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True)
    # All fields used below are same as Question_paper model inter changebly used between universities and boards related items
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=12,choices=PAPER_CHOICES)
    EDUCATION_CHOICES=[('sslc','SSLC'),('puc','PUC'),('degree','Degree'),('engineering','Engineering'),('diploma','Diploma'),('iti','ITI')] 
    college = models.CharField(max_length=100,choices=EDUCATION_CHOICES,null=True,blank=True)
    board=models.CharField(max_length=100)
    claass = models.CharField(max_length=100)
    PERIOD_CHOICES=[
        ('first','first'),('second','second'),('third','third'),('fourth','fourth'),
        ('fifth','fifth'),('sixth','sixth'),('seventh','seventh'),('eighth','eighth'),
    ]
    sem = models.CharField(max_length=100,choices=PERIOD_CHOICES,null=True,blank=True)
    sub= models.CharField(max_length=100)
    paper_year = models.DateField()
    papertitle=models.CharField(max_length=100)
    doc = models.FileField(upload_to='provider')
    provide_date=models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return  self.paper_type +' , '+self.board + ' - '+ self.sub 