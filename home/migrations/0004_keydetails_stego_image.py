# Generated by Django 4.1.5 on 2023-02-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_keydetails_cipher_text_alter_keydetails_phi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='keydetails',
            name='stego_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
