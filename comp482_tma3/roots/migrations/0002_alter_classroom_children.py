# Generated by Django 3.2.9 on 2021-12-06 04:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='children',
            field=models.ManyToManyField(limit_choices_to={'role': 'CHILD'}, to=settings.AUTH_USER_MODEL),
        ),
    ]