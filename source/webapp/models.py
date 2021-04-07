from django.db import models

# Create your models here.

STATUS_COLOR = 'color'
COLOR_BLUE = 'blue'
COLOR_RED = 'red'
STATUS_CHOICES = [
    (STATUS_COLOR, 'Цвет спортсмена'),
    (COLOR_BLUE, 'Синий'),
    (COLOR_RED, 'Красный'),
]


class Athletes(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    lastname = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='Город')
    weight = models.CharField(max_length=25, verbose_name='Вес')
    club = models.CharField(max_length=255, verbose_name='Клуб')

    def __str__(self):
        return "{}.{}.{}".format(self.name, self.lastname, self.patronymic)

    class Meta:
        verbose_name = 'Табло'
        verbose_name_plural = 'Табло'


class Scramble(models.Model):
    fighter = models.ForeignKey('webapp.Info_fit', related_name='scrambles1',
                                on_delete=models.CASCADE, verbose_name='Схватка')
    fighter2 = models.ForeignKey('webapp.Info_fit', related_name='scrambles2',
                                on_delete=models.CASCADE, verbose_name='Схватка')
    data = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return "{}. {}".format( self.fighter, self.fighter2)

    class Meta:
        verbose_name = 'Схватка'
        verbose_name_plural = 'Схватки'


class Info_fit(models.Model):
    fighter = models.ForeignKey('webapp.Athletes', related_name='scrambles',
                                on_delete=models.CASCADE, verbose_name='Схватка')
    color = models.CharField(choices=STATUS_CHOICES, default=STATUS_COLOR, max_length=255,
                             verbose_name='Цвет спортсмена')
    score_1 = models.CharField(max_length=255, null=True,blank=True, verbose_name='Счет')

    Adv = models.PositiveIntegerField(default=0, verbose_name='Приемущество')

    def __str__(self):
        return "{}".format(self.fighter)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


