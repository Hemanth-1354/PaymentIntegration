from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('failed/', views.failed, name='failed'),
]