from django.db import models

# Create your models here.

class Banner(models.Model):
    img = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    video = models.FileField(upload_to='banner2/')
    malumot = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Speakers(models.Model):
    img = models.ImageField(upload_to='speakers/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category_days(models.Model):
    day = models.CharField(max_length=255)


class Jadval(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='teacher/')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Confirens(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery/')


class Hotels(models.Model):
    img = models.ImageField(upload_to='hotels/')
    hotel_number = models.CharField(max_length=255)
    joyan_yaqin = models.CharField(max_length=255)

    def __str__(self):
        return self.hotel_number

class Gallery1(models.Model):
    img = models.ImageField(upload_to="gallery/")


class Sponcers(models.Model):
    img = models.ImageField(upload_to='sponcers')


class F_a_q(models.Model):
    quations = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.quations

