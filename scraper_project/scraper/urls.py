from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_search, name='job_search'),
    path('offers/', views.job_list, name='job_list'),
    path('reset/', views.reset_search_data, name='reset_search_data'),
    path('error/', views.error_page, name='error_page'),
]