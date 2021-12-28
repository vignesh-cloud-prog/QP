from django.db import models
import os
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Provide(models.Model):
    """
    Stores all the question papers shared by user, which are to be reviewed , related to :model:`provides.Provide` and
    :model:`auth.User`.
    """
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True)
    provider_email=models.EmailField()
    # All fields used below are same as Question_paper model inter changebly used between universities and boards related items
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=100,choices=PAPER_CHOICES)
    EDUCATION_CHOICES=[('sslc','SSLC'),('puc','PUC'),('degree','Degree'),('engineering','Engineering'),('diploma','Diploma'),('iti','ITI')] 
    education_type = models.CharField(max_length=20,choices=EDUCATION_CHOICES)
    governing_body=models.CharField(max_length=100)
    course_name = models.CharField(max_length=100,null=True,blank=True)
    PERIOD_CHOICES=[
        ('first','first'),('second','second'),('third','third'),('fourth','fourth'),
        ('fifth','fifth'),('sixth','sixth'),('seventh','seventh'),('eighth','eighth'),('none','none'),
    ]
    period=models.CharField(max_length=12,choices=PERIOD_CHOICES)
    subject_name= models.CharField(max_length=100)
    paper_year = models.DateField()
    paper_title=models.CharField(max_length=100)
    if str(os.environ.get('DEBUG')) == "1":
        doc = models.FileField(upload_to='providers_dev',validators=[FileExtensionValidator(allowed_extensions=['pdf'])], storage=RawMediaCloudinaryStorage())
    else:
        doc = models.FileField(upload_to='providers',validators=[FileExtensionValidator(allowed_extensions=['pdf'])], storage=RawMediaCloudinaryStorage())


    provided_date=models.DateTimeField(auto_now_add=True,)
    
    
    def __str__(self):
        return  self.paper_type +' , '+self.paper_type + ' - '+ self.subject_name 

