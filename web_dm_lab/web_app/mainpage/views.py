from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'mainpage/welcome.html')


def about(request):
    return render(request, 'mainpage/about.html')
