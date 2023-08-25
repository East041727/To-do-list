from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Date_time_for_task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    






class Task(Date_time_for_task):

    STATUS = (
        ('High', 'High degree'),
        ('Middle', 'Middel degree'),
        ('Low', 'Low degree')
    )


    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True,blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS, default='Low')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task,self).save(*args, **kwargs)




    def __str__(self):
        return self.name



