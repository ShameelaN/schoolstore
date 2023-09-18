from django.db import models

# Create your models here.
class Students(models.Model):
     name=models.CharField(max_length=250)
     date=models.DateField(null=True,blank=True)
     age=models.IntegerField()
     gender=models.CharField(max_length=250)
     number=models.IntegerField()
     mailid=models.EmailField()
     address=models.TextField()
     department=models.CharField(max_length=250)
     courses=models.CharField(max_length=250)
     purpose=models.CharField(max_length=250)
     materials=models.CharField(max_length=250)

     def __str__(self):
         return self.name
