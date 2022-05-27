# Generated by Django 4.0.3 on 2022-03-31 08:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BilanAnnuel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_Save', models.DateField(auto_now=True)),
                ('file_Bilan', models.FileField(upload_to=None, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='BilanCycle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_Save', models.DateField(auto_now=True)),
                ('file_Bilan', models.FileField(upload_to=None, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=200)),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dataviz.groupe')),
            ],
        ),
        migrations.CreateModel(
            name='Moyenne',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('moy', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rattrapage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_Save', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistique',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date_Save', models.DateField(auto_now=True)),
                ('file_Stat', models.FileField(upload_to=None, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('matricule', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('mot_de_passe', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('note', models.IntegerField(max_length=200)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dataviz.matiere')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dataviz.student')),
            ],
        ),
    ]
