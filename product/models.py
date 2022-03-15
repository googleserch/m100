from http.client import METHOD_NOT_ALLOWED
from locale import currency
from pyexpat import model
from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


import string
import random
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class categories(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.SlugField(max_length = 250, null = True, blank = True)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
     return format_html('<ima src="/media/{}"   />'.format(self.image))
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(rand_slug() + "-" + self.title)
        super(categories, self).save(*args, **kwargs) 


class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    deals=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    location=models.CharField(max_length=100)
    category=models.ForeignKey(categories,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class order(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=250)
    payment_status=models.BooleanField(default=False)
    start=models.DateTimeField(auto_now_add=True,null=True)
    date=models.DateTimeField(auto_now_add=False,null=True)
    
    
class amount(models.Model):
    s_amount=models.IntegerField() 




