# Generated by Django 4.1.2 on 2022-11-15 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrpanel', '0011_interview_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='result',
            field=models.CharField(choices=[('pending', 'pending'), ('selected', 'selected'), ('rejetected', 'rejected')], default='pending', max_length=20),
        ),
    ]