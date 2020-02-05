from django.db import models


class Photograher(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image')
    contact = models.IntegerField()

    def __str__(self):
        return self.name[:5]


class Model(models.Model):
    Name = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    icon = models.ImageField(upload_to='image/')
    votes_total= models.IntegerField(default=1)

    def __str__(self):
        return self.Name

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Main(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name[:5]


class Album(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:5]
