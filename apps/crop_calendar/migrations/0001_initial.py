# Generated by Django 4.1.2 on 2022-11-07 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crop', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropCalendar',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('crop_start_date', models.DateField(auto_now_add=True, null=True, verbose_name='Inicio del cultivo')),
                ('crop_end_date', models.DateField(null=True, verbose_name='Cosecha el cultivo')),
                ('id_crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.crop')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
