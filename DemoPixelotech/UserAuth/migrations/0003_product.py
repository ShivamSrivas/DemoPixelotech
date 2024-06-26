# Generated by Django 5.0.5 on 2024-05-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserAuth", "0002_alter_emailverification_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "UniqueNumber",
                    models.CharField(
                        max_length=4, unique=True, verbose_name="Unique Number"
                    ),
                ),
                ("Url", models.URLField(verbose_name="URL")),
            ],
        ),
    ]
