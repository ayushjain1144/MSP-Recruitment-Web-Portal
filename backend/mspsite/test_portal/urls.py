from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='test_login'),
    path('logout', views.logout, name='test_logout'),
    path('register', views.register, name = 'register'),
    path('', views.welcome, name='welcome'),
    path('question/<slug:id>/', views.question_list, name='question_list'),
    path('question/<slug:id>/<int:pk>/', views.question_list, name='question_list'),
    path('response_save/<int:pk>/<slug:id>/$', views.response_save, name='response_save'),
]