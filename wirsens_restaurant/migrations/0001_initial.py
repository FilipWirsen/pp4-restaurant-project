# Generated by Django 3.2.13 on 2022-05-29 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('TableID', models.AutoField(primary_key=True, serialize=False)),
                ('table_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_size', models.IntegerField()),
                ('book_date', models.DateField(default=django.utils.timezone.now)),
                ('book_time', models.IntegerField(choices=[(1050, '17:30'), (1065, '17:45'), (1080, '18:00'), (1095, '18:15'), (1110, '18:30'), (1125, '18:45'), (1140, '19:00'), (1155, '19:15'), (1170, '19:30'), (1185, '19:45'), (1200, '20:00'), (1215, '20:15'), (1230, '20:30'), (1245, '20:45'), (1260, '21:00'), (1275, '21:15'), (1290, '21:30'), (1305, '21:45'), (1320, '22:00')])),
                ('end_time', models.IntegerField(blank=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wirsens_restaurant.table')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]