# Generated by Django 4.1.3 on 2022-11-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email_user',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name_user',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname_user',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=10),
        ),
    ]
