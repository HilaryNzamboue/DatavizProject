# Generated by Django 4.0.3 on 2022-04-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dataviz', '0006_groupe_libelle_matiere_libelle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AddField(
            model_name='filemodel',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='filepv',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
