# Generated by Django 3.2.6 on 2022-12-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, help_text='разместите фото для объявления', null=True, upload_to='ads/photos/', verbose_name='фото объявления'),
        ),
    ]
