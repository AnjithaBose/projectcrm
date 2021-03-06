# Generated by Django 3.2.7 on 2021-09-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_type',
            field=models.CharField(choices=[('Operations', 'Operations'), ('Sales', 'Sales'), ('Trainer', 'Trainer'), ('Admin', 'Admin')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True),
        ),
    ]
