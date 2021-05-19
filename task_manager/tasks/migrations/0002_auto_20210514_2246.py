# Generated by Django 3.2.2 on 2021-05-14 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='result',
            field=models.CharField(default='В работе', max_length=200, verbose_name='Результат'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inspecions', to=settings.AUTH_USER_MODEL, verbose_name='Ответсвенный'),
        ),
        migrations.RenameModel(
            old_name='Regoin',
            new_name='Region',
        ),
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата принятия в работу')),
                ('type', models.CharField(choices=[('COUNTERPARTY', 'В адрес контрагента'), ('SELF', 'В адрес Компании')], max_length=100, verbose_name='Тип претензии')),
                ('adress', models.CharField(blank=True, max_length=200, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('result', models.CharField(default='В работе', max_length=200, verbose_name='Результат')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='claims', to='tasks.region', verbose_name='Регион')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
            ],
        ),
    ]
