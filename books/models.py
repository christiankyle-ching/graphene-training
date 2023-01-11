from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class GenderEnum(models.TextChoices):
    MALE = 'MALE', _("Male")
    FEMALE = 'FEMALE', _("Female")


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GenderEnum.choices)

    def __str__(self):
        return self.name


class BookGenre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE)
    genre = models.ForeignKey(
        BookGenre, related_name="books", on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.genre})"
