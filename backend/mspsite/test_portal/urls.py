from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='test_login'),
    path('logout', views.logout, name='test_logout'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('register', views.register, name = 'register'),
    path('', views.welcome, name='welcome'),
    path('login/test', views.test1, name='test'),
    path('question/<slug:id>/<int:pk>/', views.question_list, name='post_list'),
    path('response_save/<int:pk>/<slug:id>/$', views.response_save, name='response_save'),
]