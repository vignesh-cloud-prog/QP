from django.db import models
from django.utils.text import slugify 


class ExaminationType(models.Model): 
    PAPER_CHOICES=[('board','board'),('university','university')]
    paper_type=models.SlugField(max_length=12,choices=PAPER_CHOICES,help_text="Different levels of schools and colleges like Board and University")
    name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ExaminationType, self).save(*args, **kwargs)
    def __str__(self):
        return  f"{self.name}"

class GoverningBody(models.Model):
    education=models.ManyToManyField(ExaminationType)
    name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GoverningBody, self).save(*args, **kwargs)
    def __str__(self):
        return  f"{self.name}"

class Course(models.Model):
    governing_body=models.ManyToManyField(GoverningBody)
    name=models.CharField(max_length=100,unique=True)  
    slug = models.SlugField(blank=True,unique=True)    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)
    def __str__(self):
        return  f"{self.name}" 

class Period(models.Model): 
    examination_type=models.ForeignKey(ExaminationType,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Period, self).save(*args, **kwargs)
    def __str__(self):
        return  f"{self.name}"

class Subject(models.Model):
    course=models.ManyToManyField(Course)
    name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(blank=True,unique=True)    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)
    def __str__(self):
        return  f"{self.name}" 