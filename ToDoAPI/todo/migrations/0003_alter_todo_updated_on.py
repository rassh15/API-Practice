# Generated by Django 4.0.4 on 2022-05-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_id_todo_tid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_on',
            field=models.DateTimeField(editable=False),
        ),
    ]