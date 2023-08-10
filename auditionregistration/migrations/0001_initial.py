# Generated by Django 4.1.6 on 2023-07-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditionRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('img', models.FileField(default=None, null=True, upload_to='auditionregi/')),
            ],
        ),
    ]