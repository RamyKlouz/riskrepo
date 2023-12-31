# Generated by Django 4.2 on 2023-05-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_avis_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=255)),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
