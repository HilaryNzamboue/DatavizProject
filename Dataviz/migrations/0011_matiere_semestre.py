# Generated by Django 4.0.3 on 2022-04-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dataviz', '0010_filebilan_filerattrapage_moyennes1_moyennes2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='semestre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]