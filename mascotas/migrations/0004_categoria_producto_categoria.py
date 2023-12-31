# Generated by Django 4.2.1 on 2023-06-18 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_alter_producto_descripcion_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(default='10', primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, default='Sin Categoria', max_length=50, verbose_name='Nombre de categoria')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='mascotas.categoria', verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
