# Generated by Django 5.1.1 on 2024-09-08 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_link_id_alter_link_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='hash',
            new_name='short_hash',
        ),
    ]
