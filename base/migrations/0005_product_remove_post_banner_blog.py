# Generated by Django 5.0.6 on 2024-05-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_blogpage_post_banner_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reviews', models.PositiveIntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('fuel_type', models.CharField(max_length=50)),
                ('mileage', models.DecimalField(decimal_places=1, max_digits=6)),
                ('transmission', models.CharField(max_length=50)),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='banner_blog',
        ),
    ]
