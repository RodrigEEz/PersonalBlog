from applications.Entry.models import Category
from django.contrib import admin
from .models import Entry, Tag, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)