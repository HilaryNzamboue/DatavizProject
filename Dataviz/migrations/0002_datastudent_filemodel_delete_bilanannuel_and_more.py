# Generated by Django 4.0.3 on 2022-04-05 15:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Dataviz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataStudent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('annee', models.CharField(max_length=10)),
                ('filiere', models.CharField(max_length=10)),
                ('cycle', models.CharField(max_length=10)),
                ('niveau', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dataviz.student')),
            ],
            options={
                'ordering': ['annee'],
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_save', models.DateField(auto_now_add=True)),
                ('file_model', models.FileField(max_length=200, upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='BilanAnnuel',
        ),
        migrations.DeleteModel(
            name='BilanCycle',
        ),
        migrations.DeleteModel(
            name='Rattrapage',
        ),
        migrations.DeleteModel(
            name='Statistique',
        ),
        migrations.RenameField(
            model_name='groupe',
            old_name='name',
            new_name='libelle',
        ),
        migrations.RemoveField(
            model_name='moyenne',
            name='moy',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note',
        ),
        migrations.AddField(
            model_name='matiere',
            name='decision',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='moyenne',
            name='annee',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='moyenne',
            name='moy_annuelle',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='moyenne',
            name='moy_s1',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='moyenne',
            name='moy_s2',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='moyenne',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dataviz.student'),
        ),
        migrations.AddField(
            model_name='note',
            name='note_cc',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='note_moy',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='note_sn',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='note',
            name='note_tp',
            field=models.FloatField(default=0.0, max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='matiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dataviz.matiere'),
        ),
        migrations.AlterField(
            model_name='note',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dataviz.student'),
        ),
    ]
