# Generated by Django 3.2.9 on 2023-10-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_addfolder'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='parent_folder',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
