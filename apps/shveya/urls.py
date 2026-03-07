from django.urls import path

from apps.shveya import views

urlpatterns = [
    path('',views.home),
]