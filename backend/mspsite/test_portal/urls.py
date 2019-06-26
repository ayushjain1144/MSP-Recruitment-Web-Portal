from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.welcome, name='welcome'),
    path('login/test', views.test1, name='test'),
    path('question/<slug:id>/', views.question_list, name='post_list'),
    path('response_save/<int:id>/<int:question>/', views.response_save, name='responsesave'),
]