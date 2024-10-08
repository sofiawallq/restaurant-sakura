# Generated by Django 5.1 on 2024-09-03 18:18

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_bookatable_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookatable',
            options={'ordering': ['-date', '-time'], 'verbose_name': 'Table Booking', 'verbose_name_plural': 'Table Bookings'},
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='guests',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='bookatable',
            name='time',
            field=models.CharField(choices=[('15:00', '3 PM'), ('16:00', '4 PM'), ('17:00', '5 PM'), ('18:00', '6 PM'), ('19:00', '7 PM'), ('20:00', '8 PM')], max_length=5),
        ),
        migrations.AddConstraint(
            model_name='bookatable',
            constraint=models.UniqueConstraint(fields=('date', 'time', 'user'), name='unique_booking_per_user_per_time'),
        ),
    ]
