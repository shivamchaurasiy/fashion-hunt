# Generated by Django 4.1.6 on 2023-07-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditionregistration', '0004_studentmodel_delete_auditionregistrationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='nimg',
            field=models.FileField(default=None, max_length=255, null=True, upload_to=''),
        ),
    ]
