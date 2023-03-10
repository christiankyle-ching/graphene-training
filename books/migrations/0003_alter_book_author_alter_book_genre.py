# Generated by Django 4.1.5 on 2023-01-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_alter_book_author_alter_book_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="books.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="books",
                to="books.bookgenre",
            ),
        ),
    ]
