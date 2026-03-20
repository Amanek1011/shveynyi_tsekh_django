from django.urls import path

from apps.shveya import views

urlpatterns = [
    path('', views.home, name='shveya_home'),
    path('four_x/<int:material_id>/', views.four_x_view, name='four_x'),
    path('raspash/<int:material_id>/', views.raspash_view, name='raspash'),
    path('beika/<int:material_id>/', views.beika_view, name='beika'),
    path('strochka/<int:material_id>/', views.strochka_view, name='strochka'),
    path('gorlo/<int:material_id>/', views.gorlo_view, name='gorlo'),
    path('ytyg/<int:material_id>/', views.ytyg_view, name='ytyg'),
    path('otk/<int:material_id>/', views.otk_view, name='otk'),
    path('ypakovka/<int:material_id>/', views.ypakovka_view, name='ypakovka'),
]