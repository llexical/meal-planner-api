# Generated by Django 3.2.12 on 2022-03-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220325_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug', max_length=255),
            preserve_default=False,
        ),
    ]
