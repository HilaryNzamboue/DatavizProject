# Generated by Django 4.0.3 on 2022-05-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dataviz', '0022_alter_classe_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
