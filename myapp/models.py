from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    def __str__(self) -> str:
        return self.name
    
    
    
class employe(models.Model):
    name =models.CharField(max_length=50)
    id = models.CharField(max_length=10, primary_key=True)
    salary = models.IntegerField()
    address = models.TextField(null=True,blank=True)
    contact_number =models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
