# Generated by Django 4.0.2 on 2022-03-06 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_status_order_payment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='today_date',
            new_name='date',
        ),
    ]
