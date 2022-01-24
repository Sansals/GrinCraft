from django.shortcuts import render

def ShowHomePage(request):
    return render(request, 'home/home_page.html')