# Generated by Django 3.1 on 2020-09-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200906_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]
