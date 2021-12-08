# Generated by Django 3.2.9 on 2021-12-08 19:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('roots', '0019_auto_20211208_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='toileting',
            name='activity',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('none', 'None'), ('pee', 'Pee'), ('poo', 'Poo')], default='none', max_length=12),
        ),
    ]
