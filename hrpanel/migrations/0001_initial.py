# Generated by Django 4.1.2 on 2022-10-31 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpanel', '0002_alter_user_domain_alter_user_emp_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminpanel.domain')),
                ('interviewers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminpanel.position')),
            ],
        ),
    ]
