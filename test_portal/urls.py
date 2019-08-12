from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='test_login'),
    path('logout/', views.logout, name='test_logout'),
    path('register/', views.register, name = 'register'),
    path('', views.welcome, name='welcome'),
    path('loaderio-158ef98a841f6e5ef17fb5d0b83a3992/', views.test, name = 'test'), 

    path('question/<slug:id>/', views.question_list, name='question_list'),
    path('question/<slug:id>/<int:ques_no>/', views.question_list, name='question_list'),

    path('response_save/<int:pk>/<slug:id>/$', views.response_save, name='response_save'),
    path('response_save/<int:pk>/<slug:id>/<int:next>/$', views.response_save, name='response_save'),

    path('response_savem/<int:pk>/<slug:id>/<int:next>/$', views.response_savem, name='response_savem'),
    path('response_savem/<int:pk>/<slug:id>/$', views.response_savem, name='response_savem'),

    path('ques_detail_mcq/<slug:id>/',views.ques_detail_mcq,name='ques_detail_mcq'),
    path('ques_detail_mcq/<slug:id>/<int:ques_no>/',views.ques_detail_mcq,name='ques_detail_mcq'),
]
