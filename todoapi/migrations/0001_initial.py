# Generated by Django 4.1.7 on 2023-02-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(blank=True, max_length=200, null=True)),
                ('task_status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
