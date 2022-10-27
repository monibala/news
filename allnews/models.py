
from django.db import models
from traitlets import default
from category.models import category, subcategory
from .models import *
# Create your models here.
class news(models.Model):
    News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
    News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)
    date = models.DateField(null=True)
    writer_name = models.CharField(max_length=100)
    writer_image= models.ImageField()
    about_writer = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=300)
    desc = models.TextField()
    content = models.TextField(null=True,blank=True)
    slug = models.SlugField(max_length=255, default=1)
# class business(models.Model):
   
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(null=True)
#     date = models.DateTimeField(blank=True,null=True)
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     about_writer = models.TextField(null=True,blank=True)
#     title = models.CharField(max_length=300)
#     desc = models.TextField()
#     content = models.TextField(null=True,blank=True)


    # def __str__(self):
    #     return self.News_category
    # def __str__(self):
    #     return self.News_subcategory

class news_second(models.Model):
    News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
    News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
    image = models.FileField( upload_to='media',null=True,default=None,blank=True)
    date = models.DateField()
    writer_name = models.CharField(max_length=100)
    writer_image= models.ImageField()
    title = models.CharField(max_length=300)   
#     slug = models.SlugField(blank=True)
    # def __str__(self):
    #     return self.head1


# class entertain(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class entertain_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)

    
# class food(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class food_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)


# class life(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class life_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)



# class pets(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class pets_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)



# class sports(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class sports_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)    



# class techs(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class techs_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)    


# class travels(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class travels_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)    


# class urbans(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     head3 = models.CharField(max_length=100,null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)
#     desc = models.TextField()    


# class urbans_second(models.Model):
#     News_category = models.ForeignKey(category , on_delete=models.CASCADE , null=True)
#     News_subcategory = models.ForeignKey(subcategory, on_delete=models.CASCADE, null=True)
#     image = models.FileField( upload_to='media',null=True,default=None,blank=True)
#     date = models.DateField()
#     writer_name = models.CharField(max_length=100)
#     writer_image= models.ImageField()
#     title = models.CharField(max_length=300)    



