# Generated by Django 5.0.4 on 2024-05-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', max_length=500),
        ),
    ]
