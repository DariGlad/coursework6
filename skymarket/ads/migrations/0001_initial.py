# Generated by Django 3.2.6 on 2022-12-02 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='введите название товара', max_length=200, verbose_name='название товара')),
                ('price', models.PositiveIntegerField(help_text='укажите цену товара', verbose_name='цена товара')),
                ('description', models.CharField(blank=True, help_text='опишите ваш товар', max_length=1000, null=True, verbose_name='описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('author', models.ForeignKey(help_text='укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, help_text='введите текст комментария', max_length=1000, null=True, verbose_name='текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('ad', models.ForeignKey(help_text='объявление,к которому относится комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.ad', verbose_name='объявление')),
                ('author', models.ForeignKey(help_text='укажите автора', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ('-created_at',),
            },
        ),
    ]
