# Generated by Django 2.0.3 on 2018-11-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aves', '0003_fieldguide_mainimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ave',
            name='taxa',
            field=models.CharField(default='nombre cientifico ejemplo', max_length=100),
            preserve_default=False,
        ),
    ]
