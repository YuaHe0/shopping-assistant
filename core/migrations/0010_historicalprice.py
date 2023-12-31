# Generated by Django 4.2 on 2023-05-19 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_merge_20230514_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_prices', to='core.product')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
