# Generated by Django 4.1.6 on 2023-07-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0004_alter_audition_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='img',
            field=models.FileField(default=None, null=True, upload_to='audition/'),
        ),
    ]
