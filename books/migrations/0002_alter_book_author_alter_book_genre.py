# Generated by Django 4.1.5 on 2023-01-10 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_query_name="book",
                to="books.author",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_query_name="book",
                to="books.bookgenre",
            ),
        ),
    ]
