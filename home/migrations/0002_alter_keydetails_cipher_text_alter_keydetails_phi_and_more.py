# Generated by Django 4.1.5 on 2023-02-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keydetails',
            name='cipher_text',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='keydetails',
            name='phi',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='keydetails',
            name='prime_multiple',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='keydetails',
            name='public_key',
            field=models.TextField(default=False),
        ),
    ]