# Generated by Django 3.1.6 on 2021-02-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20210210_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='tasks.Tag'),
        ),
    ]
