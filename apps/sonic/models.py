from django.db import models

# Create your models here.


class SonicUser(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    # poster = models.ImageField(upload_to='poster')

    def __repr__(self):
        return self.first_name


class Interest(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    rate = models.PositiveIntegerField(default=0)
    sonic = models.ManyToManyField(SonicUser, through='Profile')


class Profile(models.Model):
    sonic = models.ForeignKey(SonicUser, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100, null=True, blank=True)




'''


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()


'''


