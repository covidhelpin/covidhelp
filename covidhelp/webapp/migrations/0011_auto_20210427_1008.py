# Generated by Django 3.2 on 2021-04-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20210427_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['category', 'name']},
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
