# Generated by Django 4.2 on 2023-05-04 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latlon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(default='DEFAULT', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('retailer', models.CharField(max_length=100)),
                ('retailer_code', models.CharField(max_length=150)),
                ('description', models.TextField(default='DEFAULT')),
                ('category', models.CharField(default='DEFAULT', max_length=100)),
                ('image_url', models.CharField(default='DEFAULT', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('itemCount', models.IntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.user')),
                ('watchlistProduct', models.ManyToManyField(to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.location')),
                ('product', models.ManyToManyField(to='core.product')),
                ('retailerID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.retailer')),
            ],
        ),
    ]
