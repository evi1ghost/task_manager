# Generated by Django 3.2.2 on 2021-05-14 22:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_auto_20210514_2246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Claims',
            new_name='Claim',
        ),
    ]
