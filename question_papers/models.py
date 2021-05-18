from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Question_papers(models.Model):
    provider=models.ForeignKey(User, on_delete=models.SET_DEFAULT,default=1,blank=True,null=True)
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=12,choices=PAPER_CHOICES,blank=True,null=True)
    college = models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    examination=models.CharField(max_length=100)
    paper = models.FileField(upload_to='preqps')
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
    PAPER_CHOICES=[('board','Board'),('university','University')]
    paper_type=models.CharField(max_length=12,choices=PAPER_CHOICES,blank=True,null=True) 
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
