# Generated by Django 4.2.3 on 2023-08-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ironrecipeuser',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='employee status'),
        ),
    ]