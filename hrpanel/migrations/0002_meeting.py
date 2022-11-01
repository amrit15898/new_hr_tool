# Generated by Django 4.1.2 on 2022-11-01 00:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('with_us', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
