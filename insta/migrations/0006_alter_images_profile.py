# Generated by Django 4.0.5 on 2022-06-05 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_images_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='insta.profile'),
        ),
    ]
