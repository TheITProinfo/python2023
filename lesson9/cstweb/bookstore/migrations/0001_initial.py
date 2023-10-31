# Generated by Django 2.2.28 on 2023-10-30 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('age', models.IntegerField(default=20, verbose_name='age')),
                ('phone', models.CharField(max_length=16, verbose_name='phone')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='addtime')),
            ],
        ),
    ]
