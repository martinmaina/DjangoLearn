# Generated by Django 4.1.5 on 2023-01-12 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230112_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip',
        ),
    ]
