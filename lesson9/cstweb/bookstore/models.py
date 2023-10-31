from datetime import datetime
from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name=models.CharField('name',max_length=50)
    age=models.IntegerField('age',default=20)
    phone=models.CharField('phone',max_length=16)
    addtime=models.DateTimeField('addtime',default=datetime.now())
