# Generated by Django 4.1.3 on 2022-11-09 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=15),
        ),
    ]