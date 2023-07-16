# Generated by Django 4.2.2 on 2023-07-13 08:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="seller",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("location", models.TextField(blank=True)),
            ],
        ),
    ]