# Generated by Django 2.1.3 on 2018-11-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloDjangoApp', '0003_auto_20181114_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.TextField(default='Nov 14, 2018 at 09:48 AM'),
        ),
    ]
