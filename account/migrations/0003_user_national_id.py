# Generated by Django 3.1 on 2020-09-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد ملی'),
        ),
    ]
