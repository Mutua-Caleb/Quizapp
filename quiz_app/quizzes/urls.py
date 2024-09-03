from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='login'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
]
