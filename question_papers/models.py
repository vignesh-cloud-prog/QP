from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

# It is suggested to replace all spaces with underscore for best results
class Question_papers(models.Model):
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True,null=True)
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=12,choices=PAPER_CHOICES,blank=True,null=True)
    # college means your education type (Ex: SSLC, PUC or Degree, Engineering, Diploma )
    college = models.CharField(max_length=100)
    # university field contains diffrent board/ universities (Ex: Mangalore University, CBSE)
    university=models.CharField(max_length=100)
    # course - includes all courses or streams in university and for boards it's by default "board"
    course = models.CharField(max_length=100)
    # year - It includes semister or years
    year = models.CharField(max_length=100)
    # subject contains name of the subject
    subject= models.CharField(max_length=100)
    # examination holds exam info like examination year
    examination=models.CharField(max_length=100)
    paper = models.FileField(upload_to='preqps')
    # slug includes all the fields value used in query search
    slug=models.CharField(max_length=400 , blank=True)
    created=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    
    def __str__(self):
        return  self.paper_type + ' , '+ self.college + ' , ' + self.course +' , '+self.year + ' - '+ self.subject 

    def save(self, *args, **kwargs):
        self.slug=self.course+"_" + self.subject +"_" +self.year+"_" +self.examination+"_" + self.university
        self.slug=self.slug.lower()
        super(Question_papers,self).save(*args, **kwargs)

        
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


class Issues(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.DecimalField(max_digits=10 ,decimal_places=0)
    issues=models.TextField()
    isuue_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return   ' Issues from ' + self.name +' - '+self.email 
