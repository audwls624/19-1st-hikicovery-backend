# Generated by Django 3.2 on 2021-04-16 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone_number', models.CharField(max_length=45)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('product', models.ManyToManyField(through='reviews.Wishlist', to='products.Product')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
