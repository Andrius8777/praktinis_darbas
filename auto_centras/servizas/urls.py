from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_client_data/', views.create_client_data, name='create_client_data'),
    path('create_mechanic/', views.create_mechanic, name='create_mechanic'),
    path('created_data_list/', views.created_data_list, name='created_data_list'),
    path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('created_client_detail/<int:client_id>/', views.created_client_detail, name='created_client_detail'),
    path('delete_mechanic/<int:mechanic_id>/', views.delete_mechanic, name='delete_mechanic'),
    path('mechanic_list/', views.mechanic_list, name='mechanic_list'),
]