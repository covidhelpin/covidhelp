# Generated by Django 3.2 on 2021-04-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210427_0801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.category'),
            preserve_default=False,
        ),
    ]
