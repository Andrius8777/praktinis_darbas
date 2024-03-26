from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about_page, name='about_page'),
    path('shop/', views.shop_page, name='shop'),
    path('services/', views.services_page, name='services'),
    path('accounts/logout/', RedirectView.as_view(url='/'), name='logout'),
]