# Generated by Django 5.1.1 on 2024-10-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_is_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
    ]
