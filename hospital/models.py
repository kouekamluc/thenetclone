from django.db import models

# Create your models here.

class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=122)
    image = models.ImageField(upload_to='sliders/')
    
    def __str__(self):
        return self.caption[:20]
    
    class Meta:
        verbose_name_plural = 'Slider'
    
    
class Service(models.Model):
    title = models.CharField(max_length=122)
    description = models.TextField()
    items = models.ManyToManyField(to='Item')
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    image1 = models.ImageField(upload_to='services/')
    image2 = models.ImageField(upload_to='services/')
    
    
    def __str__(self):
        return self.title
    

class Item(models.Model):
    title = title=models.CharField(max_length=122)
    
    def __str__(self):
        return self.title


class Mentor(models.Model):
    name = models.CharField(max_length=122)     
    speciality = models.CharField(max_length=122)
    picture = models.ImageField(upload_to='mentors/')
    detail = models.TextField()
    experience = models.TextField()
    expertize = models.ManyToManyField(to='Expertize' , related_name='mentor')
    twitter = models.CharField(max_length=122 , blank=True , null=True)
    facebook = models.CharField(max_length=122 , blank=True , null=True)
    instagram = models.CharField(max_length=122 , blank=True , null=True)
    
    


class Expertize(models.Model):
    name = models.CharField(max_length=122)
    
    def __str__(self):
        return self.name
    
    
class Faq(models.Model):
    question = models.CharField(max_length=122)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
class Gallery(models.Model):
    title = models.CharField(max_length=122)
    image = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Galleries"   