#coding:utf-8

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="images")
    title = models.CharField(max_length=300)
    url = models.URLField()
    slug = models.SlugField(max_length=500,blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,db_index=True) #db_index意味用此字段做索引
    image = models.ImageField(upload_to='images/%Y/%m/%d')#规定了所上传图片的存储位置

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Image,self).save(*args,**kwargs)

