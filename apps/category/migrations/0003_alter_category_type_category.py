# Generated by Django 4.1.2 on 2022-11-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_type_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type_category',
            field=models.SmallIntegerField(),
        ),
    ]
