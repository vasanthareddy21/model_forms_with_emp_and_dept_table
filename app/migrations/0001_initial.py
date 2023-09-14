# Generated by Django 4.2.3 on 2023-09-13 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_no', models.IntegerField()),
                ('dept_name', models.CharField(max_length=100)),
                ('dept_loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('emp_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.CharField(max_length=4)),
                ('comm', models.IntegerField(null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
