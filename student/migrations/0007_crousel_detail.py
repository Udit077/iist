# Generated by Django 3.0.3 on 2021-05-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_remove_collaboration_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='crousel',
            name='Detail',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
