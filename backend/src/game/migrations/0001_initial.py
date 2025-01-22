# Generated by Django 4.2.17 on 2025-01-14 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('privateRoom', models.BooleanField(default=False)),
                ('points_limit', models.IntegerField(default=5)),
                ('player1_ready', models.BooleanField(default=False)),
                ('player2_ready', models.BooleanField(default=False)),
                ('player1_color', models.CharField(default='color-player-default', max_length=50)),
                ('player2_color', models.CharField(default='color-player-default', max_length=50)),
                ('is_full', models.BooleanField(default=False)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosted_rooms', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default='default_room', max_length=255)),
                ('player1_score', models.PositiveIntegerField(default=0)),
                ('player2_score', models.PositiveIntegerField(default=0)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_player2', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games_won', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
