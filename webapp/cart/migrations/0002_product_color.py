# Generated by Django 4.2.6 on 2023-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Default Color', max_length=20),
        ),
    ]