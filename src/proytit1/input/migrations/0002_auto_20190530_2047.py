# Generated by Django 2.2.1 on 2019-05-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='root',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]