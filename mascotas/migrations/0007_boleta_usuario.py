# Generated by Django 4.2.1 on 2023-07-12 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mascotas', '0006_producto_stock_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
