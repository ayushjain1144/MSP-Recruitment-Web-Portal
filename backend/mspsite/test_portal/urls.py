from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.welcome, name='welcome'),
    path('login/test', views.test1, name='test'),
    path('question/<slug:id>/<int:pk>/', views.question_list, name='post_list'),
    path('response_save/<int:pk>/<slug:id>/$', views.response_save, name='response_save'),
]