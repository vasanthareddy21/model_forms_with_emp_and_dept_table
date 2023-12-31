# Generated by Django 4.2.3 on 2023-09-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dept',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='mgr',
        ),
        migrations.AlterField(
            model_name='dept',
            name='dept_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emp',
            name='comm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='emp_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
