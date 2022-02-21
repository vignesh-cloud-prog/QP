from django.db import models
from datetime import datetime
from nouns.models import *
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary_storage.storage import RawMediaCloudinaryStorage
import os

def update_filename_and_path(instance, filename):
    path = f"qpweb/{instance.paper_type}/{instance.education_type}/{instance.governing_body}/{instance.course_name}/{instance.period}/"
    extension = "." + filename.split('.')[-1]
    format = f"{instance.paper_year}_{instance.subject_name }_{instance.paper_title}_{extension}"
    return os.path.join(path, format)
def update_filename_and_path_dev(instance, filename):
    path = f"qpweb/dev/{instance.paper_type}/{instance.education_type}/{instance.governing_body}/{instance.course_name}/{instance.period}/"
    extension = "." + filename.split('.')[-1]
    format = f"{instance.paper_year}_{instance.subject_name }_{instance.paper_title}_{extension}"
    return os.path.join(path, format)

# It is suggested to replace all spaces with underscore for best results
class Question_paper(models.Model):
    """
    Stores the published Question paper. Related to :model:`question_papers.Question_paper` and
    :model:`auth.User`.
    """
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True,help_text="The user who share the question paper")
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
        paper_doc = models.FileField(upload_to=update_filename_and_path_dev,validators=[FileExtensionValidator(allowed_extensions=['pdf'])], storage=RawMediaCloudinaryStorage(),help_text="The actual paper documnet",max_length=200)
    else:
        paper_doc = models.FileField(upload_to=update_filename_and_path,validators=[FileExtensionValidator(allowed_extensions=['pdf'])], storage=RawMediaCloudinaryStorage(),help_text="The actual paper documnet",max_length=200)

    # complete_ref includes all the fields value used in query search
    complete_ref=models.CharField(max_length=800 , blank=True,help_text="a complete reference which is used in search")
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return  f"{self.paper_type}  {self.education_type}  {self.course_name} {self.period} {self.subject_name} {self.paper_year}"

    def save(self, *args, **kwargs):
        self.complete_ref=f"{self.governing_body}-{self.course_name}-{self.subject_name}-{self.paper_title}-{self.paper_year}-{self.education_type}"
        self.complete_ref=self.complete_ref.lower()
        super(Question_paper,self).save(*args, **kwargs)   



