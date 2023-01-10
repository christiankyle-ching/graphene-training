from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Gender
GENDER_MALE = "MALE"
GENDER_FEMALE = "FEMALE"
GENDER_CHOICES = [
    (GENDER_MALE, _("Male")),
    (GENDER_FEMALE, _("Female")),
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)


class BookGenre(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE)
    genre = models.ForeignKey(
        BookGenre, related_name="books", on_delete=models.SET_NULL, null=True)
