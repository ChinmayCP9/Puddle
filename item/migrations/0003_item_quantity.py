# Generated by Django 5.0.7 on 2024-07-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_catagory_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]