# Generated by Django 3.0.3 on 2021-05-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_crousel_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.CharField(default=' ', max_length=100)),
                ('Order', models.IntegerField(default=0)),
                ('Image', models.ImageField(upload_to='gallery/')),
            ],
        ),
    ]