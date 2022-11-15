from django.db import models
import sys
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
	first_name = models.CharField(max_length=256)
	email = models.EmailField(max_length=256, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='cat_img', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Post(models.Model):

    sta = (
        ('published', 'published'),
        ('draft', 'draft'),
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='title')
    image_1 = models.ImageField(null=True)
    excerpt = models.TextField(null=True, blank=True)

    content = RichTextUploadingField(config_name='portal_config')
    date_created = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, choices=sta, default='published')
    # objects  = PostManager()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.image_1)
        self.image_1 = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, profile_pic):
        print(profile_pic)
        img = Image.open(profile_pic)
        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=profile_pic.name)
        return new_image

class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.post.title

class ContactUs(models.Model):
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    whatsapp = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    email = models.EmailField()
    address = models.CharField(max_length=500)


class NewsLetter(models.Model):
    email = models.EmailField(null=True, blank=True)