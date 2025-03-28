# Generated by Django 5.1.7 on 2025-03-22 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lostfound", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lostitem",
            name="image",
        ),
        migrations.CreateModel(
            name="ItemImage",
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
                ("image", models.ImageField(upload_to="lost_items/")),
                (
                    "lost_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="lostfound.lostitem",
                    ),
                ),
            ],
        ),
    ]
