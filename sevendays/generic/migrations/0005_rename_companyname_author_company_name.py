# Generated by Django 4.0.5 on 2022-06-23 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='companyName',
            new_name='company_name',
        ),
    ]
