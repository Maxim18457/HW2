# Generated by Django 4.2.6 on 2023-10-22 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_lesson_4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=0, upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте, если торг будет уместен', verbose_name='Торг'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisement',
        ),
    ]
