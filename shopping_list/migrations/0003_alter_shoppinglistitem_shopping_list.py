# Generated by Django 3.2.12 on 2022-03-25 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0002_rename_note_shoppinglist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglistitem',
            name='shopping_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_list.shoppinglist'),
        ),
    ]
