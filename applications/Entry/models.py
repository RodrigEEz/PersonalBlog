from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager

class Category(TimeStampedModel):

    short_name = models.CharField('short name', max_length=50, unique=True)

    full_name = models.CharField('full name', max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "category"

    def __str__(self):
        return self.short_name
        

class Tag(TimeStampedModel):

    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "tag"

    def __str__(self):
        return self.name


class Entry(TimeStampedModel):

    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tag = models.ManyToManyField(Tag)
    title = models.CharField('Title', max_length=50, unique=True)
    resume = models.TextField("Resume")
    content = RichTextUploadingField('content')
    public = models.BooleanField(default=False)
    image = models.ImageField('Image',upload_to='Entry')
    cover_page = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=100)

    objects = EntryManager()

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        db_table = "entry"

    def __str__(self):
        return self.title
