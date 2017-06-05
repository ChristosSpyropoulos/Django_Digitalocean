from django.shortcuts import render

# Create your views here.


def view_home(request):
    return render(request, 'home/homepage.html')
