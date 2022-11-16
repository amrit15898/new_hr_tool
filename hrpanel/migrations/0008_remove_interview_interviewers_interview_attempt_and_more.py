# Generated by Django 4.1.2 on 2022-11-14 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrpanel', '0007_alter_interview_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='interviewers',
        ),
        migrations.AddField(
            model_name='interview',
            name='attempt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='interview',
            name='cv',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='interview',
            name='email',
            field=models.EmailField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]