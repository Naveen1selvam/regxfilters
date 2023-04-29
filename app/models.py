from django.db import models
from django.core import validators
# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(10)])
    def __str__(self)->str:
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(validators=[validators.RegexValidator('[A-Za-z0-9]+@[gmail.com]')])
    def __str__(self)->str:
        return self.name
    
class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    url=models.URLField(validators=[validators.RegexValidator('((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]')])
    date=models.DateField()
    def __str__(self) -> str:
        return self.author