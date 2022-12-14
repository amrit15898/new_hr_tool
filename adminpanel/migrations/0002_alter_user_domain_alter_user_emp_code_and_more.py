# Generated by Django 4.1.2 on 2022-10-31 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.domain'),
        ),
        migrations.AlterField(
            model_name='user',
            name='emp_code',
            field=models.IntegerField(default=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.position'),
        ),
    ]
