# Generated by Django 4.0.2 on 2022-03-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_categories_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='start',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
