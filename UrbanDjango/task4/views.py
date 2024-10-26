from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def main_page(request):
    return render(request, 'third_task/main_page.html')

def page_2(request):
    title = 'Новые автомобили'
    list_car = ['Автомобили российских марок', 'Автомобили зарубежных марок', 'Автомобили ручной сборки']
    context = {
        'title': title,
        'list_car': list_car,
    }
    return render(request, 'third_task/additional_page_1.html', context)

def page_3(request):
    title = 'Подержанные автомобили'
    list_car2 = ['Автомобили от собственников', 'Автомобили под заказ', 'Автомобили из автосалонов']
    context = {
        'title': title,
        'list_car2': list_car2,
    }
    return render(request, 'third_task/additional_page_2.html', context)

def button(request):
    return render(request, 'third_task/main_page.html')