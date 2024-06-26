# Generated by Django 5.0.6 on 2024-05-27 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_de_usuario',
            name='tipo',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='cantidad_estacionamientos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo_de_usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inmuebles.tipo_de_usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_de_usuario',
            name='tipo_de_usuario',
            field=models.CharField(choices=[('Arrendador', 'Arrendador'), ('Arrendatario', 'Arrendatario')], default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='cantidad_baños',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='cantidad_habitaciones',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='region',
            name='region',
            field=models.TextField(choices=[('Region I', 'Region I')]),
        ),
        migrations.AlterField(
            model_name='tipo_de_inmueble',
            name='tipo_de_inmueble',
            field=models.TextField(choices=[('Departamento', 'Departamento'), ('Casa', 'Casa'), ('Parcela', 'Parcela')], unique=True),
        ),
    ]
