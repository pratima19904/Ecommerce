# Generated by Django 4.0 on 2022-02-17 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0011_remove_order_status_order_statusf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='statusf',
            new_name='status_changed',
        ),
    ]
