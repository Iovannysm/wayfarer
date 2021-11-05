from django.db import models
# import models from django

from django.contrib.auth.models import User

# model imports from django 
from django.db.models import Model, CharField, ForeignKey, TextField, DateTimeField
# Create your models here.
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = DateTimeField(auto_now_add=True)
    name = CharField(max_length=100)
    current_city = CharField(max_length=200)
    profile_picture = CharField(max_length=2000, default="https://media1.thehungryjpeg.com/thumbs2/ori_3686943_09tpyqe6r67ba765aheypmgvqo0vltfraf4ru77u_plane-icon.jpg")

class City (Model):
    name = CharField(max_length=250)
    country = CharField(max_length=250)
    picture = CharField(max_length = 1000)
    user = ForeignKey(User, on_delete=models.CASCADE,related_name="cities")

class Post (Model): 
    title = CharField(max_length = 500)
    content = TextField(max_length=10000)
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    city = ForeignKey(City, on_delete=models.CASCADE, related_name="posts")
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user     
    class Meta:
        ordering = ['created_at']


  


