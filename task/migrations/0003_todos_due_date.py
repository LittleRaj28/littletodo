# Generated by Django 4.2.4 on 2023-09-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_todos_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
