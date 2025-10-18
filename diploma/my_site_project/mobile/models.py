from django.db import models
from django.contrib.auth.models import User  # класс из таблицы auth


# создание таблицы
class Mobile(models.Model):
    title = models.CharField(max_length=200, blank=True)  # марка авто
    text = models.CharField(max_length=2000, blank=True)  # цвет авто
    description = models.TextField(blank=True)  # многострочное текстовое поле
    date = models.DateField(auto_now_add=True)  # дата
    image = models.ImageField(upload_to='mobile/images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)  # делаем связь
    telephone = models.CharField(max_length=2000, blank=True)  # телефон заказчика
    created = models.DateTimeField(auto_now_add=True)  # время создания
    name = models.CharField(max_length=200, null=True, blank=True)  # имя заказчика
    email = models.EmailField(max_length=500, null=True, blank=True)  # эл.почта заказчика
    year = models.CharField(max_length=200, null=True, blank=True)  # год выпуска авто
    url = models.URLField(blank=True)

# возвращаем строковое представление обьекта (после создания модели регистрируем в админ.ру)
    def __str__(self):
        return self.title

