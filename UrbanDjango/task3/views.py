from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def main_page(request):
    return render(request, 'third_task/main_page.html')

def page_2(request):
    return render(request, 'third_task/additional_page_1.html')

def page_3(request):
    return render(request, 'third_task/additional_page_2.html')

def button(request):
    return render(request, 'third_task/main_page.html')