# Generated by Django 5.1.1 on 2024-10-16 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comentarios_options_alter_comentarios_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='posts.posts'),
        ),
    ]
