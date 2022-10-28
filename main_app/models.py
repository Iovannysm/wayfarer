# import models from django
from django.db import models

from django.contrib.auth.models import User

# model imports from django 
from django.db.models import Model, CharField, ForeignKey, TextField, DateTimeField, SlugField, OneToOneField

#Pretty URL with reverse and slugify
from django.urls import reverse
from django.template.defaultfilters import slugify

# User email must be unique
    # Use sub-class meta: Check email in user and make sure it's unique
    # Reference: https://stackoverflow.com/questions/1160030/how-to-make-email-field-unique-in-model-user-from-contrib-auth-in-django

User._meta.get_field('email')._unique = True

# Create your models here.
class Profile (Model):
    user = OneToOneField(User, on_delete=models.CASCADE, unique=True)
    join_date = DateTimeField(auto_now_add=True)
    name = CharField(max_length=100)
    slug = SlugField(max_length=100, default='no_slugs', unique=False)
    current_city = CharField(max_length=200)
    profile_picture = CharField(max_length=2000, default="https://media1.thehungryjpeg.com/thumbs2/ori_3686943_09tpyqe6r67ba765aheypmgvqo0vltfraf4ru77u_plane-icon.jpg")

    def __str__(self):
        return self.name

class City (Model):
    name = CharField(max_length=250)
    slug = SlugField(max_length=100, default='no_slugs', unique=False)
    country = CharField(max_length=250)
    picture = CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Post (Model): 
    title = CharField(max_length = 200)
    content = TextField(max_length=10000, blank=False)
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    city = ForeignKey(City, on_delete=models.CASCADE, related_name="posts")
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) 

    # NOTE could make a model method that would get the time from posting to the current time for display 

    class Meta:
        ordering = ['created_at']

class Comment (Model):
    content = TextField(max_length = 10000)
    profile = ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)
