# Generated by Django 3.2.2 on 2021-05-13 18:39

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
            name='Regoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, unique=True, verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата поступления')),
                ('inspection_type', models.CharField(choices=[('RPN', 'Роспотребнадзор'), ('POLICE', 'Полиция'), ('PROSECUTOR', 'Прокуратура'), ('LABORE', 'ГИТ'), ('ATI', 'Ати/Администрация'), ('OTHERS', 'Иные контролирующие органы')], max_length=100, verbose_name='Тип проверки')),
                ('inspector', models.CharField(max_length=150, verbose_name='Проверяющий орган')),
                ('adress', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('event', models.TextField(blank=True, verbose_name='Собития в рамках проверки')),
                ('result', models.CharField(default='В процессе', max_length=200, verbose_name='Результат')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='regions', to='tasks.regoin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspecions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]