from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from mobile.models import Mobile
from mobile.models import UserForm  # модель обратная связь
from mobile.models import CarForm  # модель заказ авто
from .forms import RegisterUserForm, CallForm, OrdercarForm  # импортируем форму
from telebot.send_message import send_telegram, send_telegram2
from django.contrib import messages


# регистрация и автоматическая авторизация
# def signup_user(request):
#     if request.method == "GET":
#         return render(request, 'mobile/signupuser.html', {'form': RegisterUserForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:  # создать нового  пользователя
#
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()                                         # сохраняем нового пользователя
#                 login(request, user)
#                 messages.info(request, "Вы прошли регистрацию!")
#                 return redirect('index')  # перенаправляем пользователя на главную страницу
#             except IntegrityError:
#                 return render(request, 'mobile/signupuser.html',
#                               {'form': RegisterUserForm(),
#                                'error': 'Такое имя пользователя уже существует. Задайте другое'})
#         else:
#             return render(request, 'mobile/signupuser.html',
#                           {'form': RegisterUserForm(), 'error': 'Пароли не совпадают'})


def signup_user(request):
    if request.method == "GET":
        return render(request, 'mobile/signupuser.html', {'form': RegisterUserForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:  # создать нового  пользователя

            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()   # сохраняем нового пользователя
                login(request, user)
                messages.info(request, 'Вы прошли регистрацию!')
                return redirect('index')  # перенаправляем пользователя на главную страницу
            except IntegrityError:
                messages.error(request, 'Такое имя пользователя уже существует. Задайте другое')
                return render(request, 'mobile/signupuser.html', {'form': RegisterUserForm()})
        else:
            messages.error(request, 'Пароли не совпадают')
            return render(request, 'mobile/signupuser.html', {'form': RegisterUserForm()})


def index(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/index.html', {'projects': projects, 'form': CallForm()})


def detail(request, pk):
    detail_obj = Mobile.objects.get(id=pk)
    # print(detail_obj)
    return render(request, 'mobile/details.html', {'detail': detail_obj})


def company(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/company.html', {'projects': projects})


def condition_page(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/condition.html', {'projects': projects})


def contact(request):
    projects = Mobile.objects.all()
    return render(request, 'mobile/contact.html', {'projects': projects, 'form': CallForm()})


def zakaz(request, pk):
    zakaz_obj = Mobile.objects.get(id=pk)
    return render(request, 'mobile/zakaz.html', {'zakaz': zakaz_obj, 'form': OrdercarForm()})


def thanks_page(request):  # форма заказ модели авто
    if request.POST:
        name = request.POST['name']  # забираем данные пользователя из полей формы
        telephone = request.POST['telephone']
        car_name = request.POST['car_name']
        car_color = request.POST['car_color']
        car_year = request.POST['car_year']
        element = CarForm(name=name, telephone=telephone, car_name=car_name, car_color=car_color,
                          car_year=car_year)
        element.save()
        send_telegram2(tg_name=name, tg_phone=telephone, tg_car_name=car_name, tg_color=car_color, tg_year=car_year)
        return render(request, 'mobile/thanks.html', {'name': name})
    else:
        return render(request, 'mobile/index.html')


def thank_page(request):  # форма обратная связь
    if request.POST:
        name = request.POST['name']           # забираем данные пользователя из полей формы
        telephone = request.POST['telephone']
        element = UserForm(name=name, telephone=telephone)
        element.save()
        send_telegram(tg_name=name, tg_phone=telephone)
        return render(request, 'mobile/thank.html', {'name': name})
    else:
        return render(request, 'mobile/index.html')


# def thanks_register(request):  # форма регистр. и авториз.
#     if request.POST:
#         username = request.POST['username']           # забираем данные пользователя из полей формы
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         element = RegisterUserForm(username=username, email=email, password1=password1, password2=password2)
#         element.save()
#         return render(request, 'mobile/thanks_register.html')
#     else:
#         return render(request, 'mobile/index.html')
