# Generated by Django 5.0.1 on 2024-01-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mente_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data Limite'),
        ),
    ]
