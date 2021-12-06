# Generated by Django 3.2.9 on 2021-12-06 19:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roots', '0007_auto_20211206_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='children',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'CHILD'}, to=settings.AUTH_USER_MODEL),
        ),
    ]
