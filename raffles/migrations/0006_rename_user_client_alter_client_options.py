# Generated by Django 4.2.20 on 2025-05-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raffles', '0005_alter_ticket_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
