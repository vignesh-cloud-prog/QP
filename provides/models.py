from pyexpat import model
from django.db import models
import os
from datetime import datetime
from nouns.models import *
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

def update_filename_and_path(instance, filename):
    path = f"qpweb/provides/{instance.paper_type}/{instance.education_type}/{instance.governing_body}/{instance.course_name}/{instance.period}/"
    extension = "." + filename.split('.')[-1]
    format = f"{instance.paper_year}_{instance.subject_name }_{instance.paper_title}_{extension}"
    return os.path.join(path, format)
def update_filename_and_path_dev(instance, filename):
    path = f"qpweb/provides/dev/{instance.paper_type}/{instance.education_type}/{instance.governing_body}/{instance.course_name}/{instance.period}/"
    extension = "." + filename.split('.')[-1]
    format = f"{instance.paper_year}_{instance.subject_name }_{instance.paper_title}_{extension}"
    return os.path.join(path, format)


class Provide(models.Model):
    """
    Stores all the question papers shared by user, which are to be reviewed , related to :model:`provides.Provide` and
    :model:`auth.User`.
    """
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True,help_text="The user who share the question paper")
    provider_email=models.EmailField()
    # All fields used below are same as Question_paper model inter changebly used between universities and boards related items
    PAPER_CHOICES=[('board','board'),('university','university')]
    paper_type=models.SlugField(max_length=12,choices=PAPER_CHOICES,help_text="Different levels of schools and colleges like Board and University")
    education_type = models.ForeignKey(ExaminationType,on_delete=models.CASCADE,help_text="Different education types like SSLC, PUC,Degree, Engineering or Diploma")
    # university field contains diffrent board/ universities (Ex: Mangalore University, CBSE)
    governing_body=models.ForeignKey(GoverningBody,on_delete=models.CASCADE,help_text="The authority who governs that Education system. Ex: CBSE, Mangalore University")
    # course - includes all courses or streams in university and for boards it's by default "board"
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,help_text="Name of the course")
    # year - It includes semister or years
    PERIOD_CHOICES=[
        ('first','first'),('second','second'),('third','third'),('fourth','fourth'),
        ('fifth','fifth'),('sixth','sixth'),('seventh','seventh'),('eighth','eighth'),('none','none'),
    ]
    period=models.ForeignKey(Period,on_delete=models.CASCADE,help_text="different portion of the course like semisters or years")
    # subject contains name of the subject
    subject_name= models.ForeignKey(Subject,on_delete=models.CASCADE,help_text="Question paper subject")
    # examination holds exam info like examination year
    paper_year = models.DateField(help_text="year when the question paper was released")
    #examination
    paper_title=models.CharField(max_length=100, help_text="title of the paper")
    if str(os.environ.get('DEBUG')) == "1":
        doc = models.FileField(upload_to=update_filename_and_path_dev,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],max_length=300, storage=RawMediaCloudinaryStorage())
    else:
        doc = models.FileField(upload_to=update_filename_and_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])],max_length=300, storage=RawMediaCloudinaryStorage())


    provided_date=models.DateTimeField(auto_now_add=True,)
    
    
    def __str__(self):
        return  f"{self.paper_type}-{self.paper_type}-{self.subject_name}" 

