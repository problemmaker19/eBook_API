# Generated by Django 4.0.4 on 2022-05-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False, help_text='Designates which fields the user can add/change/delete', verbose_name='teacher status'),
        ),
    ]
