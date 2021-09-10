from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# It is suggested to replace all spaces with underscore for best results
class Question_paper(models.Model):
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True)
    PAPER_CHOICES=[('board','board'),('university','university'),('competitive','competitive')]
    paper_type=models.SlugField(max_length=12,choices=PAPER_CHOICES)
    # college means your education type (Ex: SSLC, PUC or Degree, Engineering, Diploma )
    EDUCATION_CHOICES=[('sslc','sslc'),('puc','puc'),('degree','degree'),('engineering','engineering'),('diploma','diploma')]
    education_type = models.SlugField(max_length=12,choices=EDUCATION_CHOICES,null=True,blank=True)
    # university field contains diffrent board/ universities (Ex: Mangalore University, CBSE)
    governing_body=models.SlugField(max_length=800 , null=True,blank=True)
    # course - includes all courses or streams in university and for boards it's by default "board"
    course_name=models.SlugField(max_length=800 , null=True,blank=True)
    # year - It includes semister or years
    PERIOD_CHOICES=[
        ('first','first'),('second','second'),('third','third'),('fourth','fourth'),
        ('fifth','fifth'),('sixth','sixth'),('seventh','seventh'),('eighth','eighth'),('none','none'),
    ]
    period=models.SlugField(max_length=12,choices=PERIOD_CHOICES,null=True,blank=True)
    # subject contains name of the subject
    subject_name= models.SlugField(max_length=100,null=True,blank=True)
    # examination holds exam info like examination year
    paper_year = models.DateField(auto_now=False,auto_now_add=False)
    #examination
    paper_title=models.SlugField(max_length=100)
    paper_doc = models.FileField(upload_to='allqps',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    # complete_ref includes all the fields value used in query search
    complete_ref=models.CharField(max_length=800 , blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return  f"{self.paper_type}  {self.education_type}  {self.course_name} {self.period} {self.subject_name} {self.paper_year}"

    def save(self, *args, **kwargs):
        self.complete_ref=f"{self.course_name}_{self.subject_name}_{self.paper_year}_{self.paper_title}_{self.governing_body}_{self.education_type}"
        self.complete_ref=self.complete_ref.lower()
        super(Question_paper,self).save(*args, **kwargs)   



