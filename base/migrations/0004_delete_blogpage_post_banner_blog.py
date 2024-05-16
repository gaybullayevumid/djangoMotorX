# Generated by Django 5.0.6 on 2024-05-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_blogpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.AddField(
            model_name='post',
            name='banner_blog',
            field=models.FileField(null=True, upload_to='blog-page-images'),
        ),
    ]