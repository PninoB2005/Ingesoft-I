# Generated by Django 5.1.6 on 2025-02-27 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id_examen', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_aplicacion', models.DateTimeField(blank=True, null=True)),
                ('tiempo_limite', models.IntegerField(blank=True, null=True)),
                ('aplicada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('enunciado', models.TextField()),
                ('tipo', models.CharField(choices=[('opcion-multiple', 'Opción múltiple'), ('abierta', 'Abierta')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluaciones.examen')),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.grupo')),
            ],
            options={
                'unique_together': {('id_examen', 'id_grupo')},
            },
        ),
        migrations.AddField(
            model_name='examen',
            name='grupos',
            field=models.ManyToManyField(through='evaluaciones.ExamenGrupo', to='academico.grupo'),
        ),
        migrations.CreateModel(
            name='ExamenPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluaciones.examen')),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluaciones.pregunta')),
            ],
            options={
                'unique_together': {('id_examen', 'id_pregunta')},
            },
        ),
        migrations.AddField(
            model_name='examen',
            name='preguntas',
            field=models.ManyToManyField(through='evaluaciones.ExamenPregunta', to='evaluaciones.pregunta'),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('id_usuario', models.IntegerField()),
                ('num_opcion', models.IntegerField(blank=True, null=True)),
                ('respuesta_abierta', models.TextField(blank=True, null=True)),
                ('calificacion_parcial', models.FloatField(default=0.0)),
                ('id_examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluaciones.examen')),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluaciones.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_opcion', models.PositiveIntegerField()),
                ('texto_opcion', models.TextField()),
                ('es_correcta', models.BooleanField(default=False)),
                ('peso_calificacion', models.FloatField(default=0.0)),
                ('id_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='evaluaciones.pregunta')),
            ],
            options={
                'unique_together': {('id_pregunta', 'num_opcion')},
            },
        ),
    ]
