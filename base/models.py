from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField(upload_to='myBlogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
