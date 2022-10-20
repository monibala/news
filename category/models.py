from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class category(models.Model):
    category_name = models.CharField(max_length=50)
    
    slug = models.SlugField(max_length=255, default=1)
    def __str__(self):
        return self.category_name

class subcategory(models.Model):
    subcategory_name = models.CharField(max_length=50)
    category_name = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=255, default=1)
    def __str__(self):
        return self.subcategory_name

