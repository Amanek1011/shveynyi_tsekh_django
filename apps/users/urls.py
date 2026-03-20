from django.urls import path

from apps.users import views

urlpatterns = [
    path('', views.users_home, name='users_home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]