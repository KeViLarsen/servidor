# Generated by Django 3.2.7 on 2022-02-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapunto', '0003_alter_methodpay_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]