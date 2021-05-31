from django.db import models
from froala_editor.fields import FroalaField
from base.utils import generate_slug

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null= True, blank= True)
    image = models.ImageField(upload_to='blog', blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)
