from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth import get_user_model as user_model
# User = user_model()


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

    class Meta:
      db_table = 'customuser'


class PublicPost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    content = models.TextField()
    createdon = models.DateTimeField(db_column="created_on", auto_now_add=True)
    modifiedon = models.DateTimeField(db_column="modified_on", blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'public_posts'
        ordering = ['-createdon']

class UserPost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    content = models.TextField()
    userid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    createdon = models.DateTimeField(db_column="created_on", auto_now_add=True)
    modifiedon = models.DateTimeField(db_column="modified_on", blank=True, null=True)
    createdby = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, db_column="created_by",related_name='post_createdby')
    modifiedby = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, db_column="modified_by", related_name='post_modifiedby')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'user_posts'
        ordering = ['-createdon']