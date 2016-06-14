from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from theleakycauldron.settings import AUTH_USER_MODEL


class Article(models.Model):  # The Model for the posts in the blog
    author = models.ForeignKey(AUTH_USER_MODEL)
    title = models.CharField(max_length=140)
    tags = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', default='uploads/theleakycauldron.jpg')
    content = models.TextField()
    style = models.CharField(max_length=6, default='style3')
    published_date = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.last_edited = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=timezone.now)

    def connect(self):
        self.contact_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    display_picture = models.ImageField(upload_to='uploads', default='uploads/vaibhav.jpg')
    dob = models.DateField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=140, default='Computer Science Student')
    expertise = models.TextField(blank=True, null=True)
    resume = models.URLField(
        default='https://onedrive.live.com/redir?resid=15B77C3F05089AE3!29124&authkey=!AP_w7US1JtUoSDo&ithint=file%2cpdf')
    last_edited = models.DateTimeField(default=timezone.now)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            About.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def create(self):
        self.last_edited = timezone.now()
        self.save()

    def __str__(self):
        return self.user.get_full_name()
