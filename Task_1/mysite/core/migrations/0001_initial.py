# Generated by Django 3.2 on 2021-05-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=2000)),
                ('date', models.DateField(null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
