from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='test_login'),
    path('logout', views.logout, name='test_logout'),
    path('register', views.register, name = 'register'),
    path('', views.welcome, name='welcome'),
    path('question/<slug:id>/', views.question_list, name='question_list'),
    path('question/<slug:id>/<int:ques_no>/', views.question_list, name='question_list'),
    path('response_save/<int:pk>/<slug:id>/$', views.response_save, name='response_save'),
    path('response_savem/<int:pk>/<slug:id>/$', views.response_savem, name='response_savem'),
    path('response_savei/<int:pk>/<slug:id>/$', views.response_savei, name='response_savei'),
    path('ques_detail/<slug:id>/<int:pk>/',views.ques_detail,name='ques_detail'),
    path('ques_detail2/<slug:id>/<int:pk>/',views.ques_detail2,name='ques_detail2'),
    path('round2', views.round2, name='round2'),
    path('proceed', views.proceed, name='proceed'),
]
