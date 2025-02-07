from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject= models.TextField()


class Service(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(max_length=100)
  content = models.TextField()    


class Testimonial(models.Model):
  name = models.CharField(max_length=100)
  destination = models.CharField(max_length=100)
  img = models.ImageField(upload_to='images/')
  content = models.TextField()    

  