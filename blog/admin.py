from django.contrib import admin
from .models import Article, Contact, About

# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(About)
