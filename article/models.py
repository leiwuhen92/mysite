#coding:utf-8
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


#文章栏目模型
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name='article_column',on_delete=models.CASCADE)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


#发布与显示文章模型
class  ArticlePost(models.Model):
    author =models.ForeignKey(User,related_name="article",on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,related_name="article_column",on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User,related_name="articles_like" ,blank=True)

    class Meta:
        ordering = ("title",)  #排序
        index_together = (('id','slug'),) #索引

    def __str__(self):
        return  self.title

    def save(self,*args,**kargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args,**kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])

    def get_url_path(self):
        return reverse("article:list_article_detail",args=[self.id,self.slug])




