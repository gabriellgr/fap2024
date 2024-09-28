# Generated by Django 5.1.1 on 2024-09-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('data_disponivel', models.DateField()),
                ('telefone', models.TextField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
                ('cpf', models.TextField()),
                ('data_consulta', models.DateField()),
                ('telefone', models.TextField(max_length=15)),
            ],
        ),
    ]
