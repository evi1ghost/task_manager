from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def get_last_name(self):
    return self.last_name


User.add_to_class("__str__", get_last_name)


User = get_user_model()


INSPECTION_TYPE = [
    ('RPN', 'Роспотребнадзор'),
    ('POLICE', 'Полиция'),
    ('PROSECUTOR', 'Прокуратура'),
    ('LABORE', 'ГИТ'),
    ('ATI', 'Ати/Администрация'),
    ('OTHERS', 'Иные контролирующие органы')
]


CLAIMS_TYPE = [
    ('COUNTERPARTY', 'В адрес контрагента'),
    ('SELF', 'В адрес Компании')
]


class Region(models.Model):
    region = models.CharField(
        verbose_name='Регион', max_length=100, unique=True
    )

    def __str__(self):
        return self.region


class Inspection(models.Model):
    INSPECTION_TYPE = [
        ('RPN', 'Роспотребнадзор'),
        ('POLICE', 'Полиция'),
        ('PROSECUTOR', 'Прокуратура'),
        ('LABORE', 'ГИТ'),
        ('ATI', 'Ати/Администрация'),
        ('OTHERS', 'Иные контролирующие органы')
    ]
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='inspecions',
        verbose_name='Ответсвенный'
    )
    date = models.DateField(verbose_name='Дата поступления')
    inspection_type = models.CharField(
        verbose_name='Тип проверки', choices=INSPECTION_TYPE, max_length=100
    )
    inspector = models.CharField(
        verbose_name='Проверяющий орган', max_length=150
    )
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, related_name='regions',
        verbose_name='Регион'
    )
    adress = models.CharField(
        verbose_name='Адрес', max_length=200, blank=True
    )
    description = models.TextField(verbose_name='Описание')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    event = models.TextField(
        verbose_name='Собития в рамках проверки', blank=True
    )
    result = models.CharField(
        verbose_name='Результат', default='В работе', max_length=200
    )

    def __str__(self):
        return ', '.join([self.inspector, self.adress, str(self.date)])

    class Meta:
        ordering = ['-date']


class Claim(models.Model):
    CLAIMS_TYPE = [
        ('COUNTERPARTY', 'В адрес контрагента'),
        ('SELF', 'В адрес Компании')
    ]
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='claims',
        verbose_name='Ответственный'
    )
    date = models.DateField(verbose_name='Дата принятия в работу')
    type = models.CharField(
        verbose_name='Тип претензии', choices=CLAIMS_TYPE, max_length=100
    )
    counterparty = models.CharField(verbose_name='Контрагент', max_length=200)
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, related_name='claims',
        verbose_name='Регион'
    )
    adress = models.CharField(
        verbose_name='Адрес', max_length=200, blank=True
    )
    description = models.TextField(verbose_name='Описание')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    result = models.CharField(
        verbose_name='Результат', default='В работе', max_length=200
    )

    def __str__(self):
        return ', '.join([self.type, self.counterparty, str(self.date)])


class Trial(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='trials',
        verbose_name='Ответственный'
    )
    initial_date = models.DateField(
        verbose_name='Дата принятия принятия к производству'
    )
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, related_name='trials',
        verbose_name='Регион'
    )
    court = models.CharField(
        verbose_name='Наименования судов', max_length=300
    )
    case_number = models.CharField(verbose_name='Номер дела', max_length=200)
    plaintiff = models.CharField(verbose_name='Истец', max_length=200)
    defendant = models.CharField(verbose_name='Ответчик', max_length=200)
    amount = models.FloatField(
        verbose_name='Сумма требования', null=True, blank=True
    )
    subject = models.TextField(verbose_name='Предмет иска')
    comment = models.TextField(verbose_name='Комментарии', blank=True)
    posible_result = models.IntegerField(
        verbose_name='Вероятность удовлетворения требований истка, %',
    )
    result = models.CharField(
        verbose_name='Результат', default='Рассматривается', max_length=300
    )

    def __str__(self):
        return ', '.join([self.plaintiff, self.defendant, self.case_number])
