# Generated by Django 5.1.7 on 2025-05-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regno', models.IntegerField(verbose_name='Regno')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('departmnet', models.CharField(default='BCA', max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
