# Generated by Django 4.0.4 on 2022-05-18 13:38

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("buyer", models.TextField()),
                ("description", models.TextField()),
                ("unit_price", models.FloatField()),
                ("quantity", models.PositiveIntegerField()),
                ("address", models.TextField()),
                ("provider", models.TextField()),
            ],
        ),
    ]
