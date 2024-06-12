from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('create/', views.create_transaction, name='create_transaction'),
    path('update/<int:pk>/', views.update_transaction, name='update_transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]
