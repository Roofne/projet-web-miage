# Generated by Django 3.2.9 on 2021-11-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('adresse_postale', models.CharField(max_length=255)),
            ],
        ),
    ]
