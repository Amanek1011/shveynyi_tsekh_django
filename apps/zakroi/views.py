
from django.shortcuts import render


def zakroi_home(request):
    return render(request, "zakroi/zakroi_home.html")