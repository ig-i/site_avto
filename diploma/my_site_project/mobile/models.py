from django.db import models
from django.contrib.auth.models import User  # класс из таблицы auth


# создание таблицы
class Mobile(models.Model):
    title = models.CharField(max_length=200, blank=True)  # марка авто
    text = models.CharField(max_length=2000, blank=True)  # цвет авто
    description = models.TextField(blank=True)  # многострочное текстовое поле
    image = models.ImageField(upload_to='mobile/images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # делаем связь
    name_user = models.CharField(max_length=200, blank=True)  # имя заказчика
    telephone_user = models.CharField(max_length=200, blank=True)  # телефон заказчика
    name_car = models.CharField(max_length=200, blank=True)
    color_car = models.CharField(max_length=200, blank=True)
    year_car = models.CharField(max_length=200, blank=True)

    # возвращаем строковое представление обьекта (после создания модели регистрируем в админ.ру)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class UserForm(models.Model):
    name = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'


class CarForm(models.Model):
    name = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    car_name = models.CharField(max_length=200, blank=True)
    car_color = models.CharField(max_length=200, blank=True)
    car_year = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заказ автомобиля'
        verbose_name_plural = 'заказ автомобилей'

