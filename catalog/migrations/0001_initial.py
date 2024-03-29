# Generated by Django 4.1.7 on 2023-07-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=150, verbose_name='Категория')),
                ('purchase_price', models.IntegerField(verbose_name='Цена за покупку')),
                ('creation_date', models.DateField(verbose_name='Дата создания')),
                ('last_mode_date', models.DateField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]