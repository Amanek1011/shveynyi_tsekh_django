from django.urls import path

from apps.zakroi import views

urlpatterns = [
    path('',views.zakroi_home),
]