# Generated by Django 4.1.6 on 2023-07-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0003_remove_audition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='img',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
