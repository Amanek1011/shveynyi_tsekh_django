from django.urls import path

from apps.zakroi import views

urlpatterns = [
    path('', views.zakroi_home, name='zakroi_home'),
    path('create-party/', views.create_party, name='create_party'),
    path('create-material/<int:party_id>/', views.create_material, name='create_material'),
    path('create-user/', views.create_user, name='create_user'),
    path('party-stats/', views.party_stats, name='party_stats'),
    path('material/<int:material_id>/', views.material_detail, name='material_detail'),
]