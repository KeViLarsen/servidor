# Generated by Django 3.2.7 on 2022-02-23 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0002_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodpay',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
