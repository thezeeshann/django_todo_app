# Generated by Django 4.0.6 on 2022-07-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]