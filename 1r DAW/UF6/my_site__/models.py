from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=50, validators=[MinLengthValidator(1), MaxLengthValidator(50)])

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1), MaxLengthValidator(200)])
    excerpt = models.TextField(validators=[MinLengthValidator(10)])
    image_name = models.CharField(max_length=100, validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    date = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True,
                            validators=[MinLengthValidator(1), MaxLengthValidator(50)])
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title