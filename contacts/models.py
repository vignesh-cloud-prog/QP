from django.db import models
from datetime import datetime

# Create your models here.
class Issue(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.DecimalField(max_digits=10 ,decimal_places=0)
    issues=models.TextField()
    isuue_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return   ' Issues from ' + self.name +' - '+self.email 