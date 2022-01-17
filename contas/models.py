from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=150, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitle = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', blank=True)
    text = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_table(self):
        if self.image:
            return mark_safe('<img src ="{}" height = "50"/>'.format(self.image.url))
        else:
            return mark_safe('<p> sem imagem </p>')

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.name