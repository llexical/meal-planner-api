# Generated by Django 3.2.12 on 2022-03-21 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinglist',
            old_name='note',
            new_name='name',
        ),
    ]
