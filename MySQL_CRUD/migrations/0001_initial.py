# Generated by Django 4.2.13 on 2024-05-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'datas',
            },
        ),
    ]
