# Generated by Django 3.2.9 on 2021-12-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='produits',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]