from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
def about_me_view(request):
    if request.method == "GET":
            return HttpResponse("Я, Карыбаев Нурадил, родился 20 февраля 2008 года, любитель латяо и ютубчека",
                                "Достижения: 1500 часов в доте, не плакал когда ходил в поликлинику без мамы. Все")
def fvrt_writers_view(request):
      if request.method == "GET":
            return HttpResponse("Лев Толстой, Уильям Шекспир, Джордж Оруэлл, Марк Твэн, "
            "Джейн Остин, Эрнест Хеммингуэй, Агата Кристи, А. С. Пушкин, "
            "Чынгыз Айтматов, Федор Достоевский")
def datetime_view(date):

    return HttpResponse(f'сейчас - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
# Create your views here.
