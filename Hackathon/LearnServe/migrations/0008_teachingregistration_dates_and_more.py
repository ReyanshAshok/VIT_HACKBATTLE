# Generated by Django 4.0.2 on 2023-09-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnServe', '0007_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingregistration',
            name='dates',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teachingregistration',
            name='days_available',
            field=models.IntegerField(null=True),
        ),
    ]