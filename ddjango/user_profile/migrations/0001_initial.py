# Generated by Django 2.2.5 on 2020-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('purchased_cards', models.ManyToManyField(to='card_info.CardInfo')),
            ],
        ),
    ]
