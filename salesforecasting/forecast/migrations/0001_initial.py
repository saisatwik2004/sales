# Generated by Django 5.0.1 on 2024-03-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField()),
                ('age', models.DecimalField(decimal_places=5, max_digits=10)),
                ('category', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=10)),
                ('payment_method', models.IntegerField()),
                ('shopping_mall', models.IntegerField()),
                ('Sales', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
