# Generated by Django 3.0.3 on 2021-05-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='DG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='dg/')),
            ],
        ),
    ]
