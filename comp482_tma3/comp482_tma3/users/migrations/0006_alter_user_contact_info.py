# Generated by Django 3.2.9 on 2021-12-06 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roots', '0009_auto_20211206_1221'),
        ('users', '0005_user_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roots.contactinfo'),
        ),
    ]
