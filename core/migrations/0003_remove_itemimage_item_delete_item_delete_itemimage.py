# Generated by Django 4.1 on 2024-07-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_itemimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ItemImage',
        ),
    ]
