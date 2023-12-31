# Generated by Django 4.0.2 on 2023-09-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearnServe', '0010_remove_education_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachingregistration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='volenteerregistration',
            name='user',
        ),
        migrations.AddField(
            model_name='teachingregistration',
            name='name_of_person',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='volenteerregistration',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='cool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnServe.testmodel'),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volenteerregistration',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
    ]
