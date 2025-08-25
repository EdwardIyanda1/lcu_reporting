from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_form, name='report_form'),
    path('login/', views.admin_login, name='admin_login'), 
    path('logout/', views.admin_logout, name='admin_logout'),  
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'), 
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('delete-report/<int:report_id>/', views.delete_report, name='delete_report'),
]