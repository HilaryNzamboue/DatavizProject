# Generated by Django 4.0.3 on 2022-04-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dataviz', '0019_remove_filebilan_name_remove_filepv_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebilan',
            name='date_save',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='filepv',
            name='date_save',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='filerattrapage',
            name='date_save',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
