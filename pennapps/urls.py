from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view, name='signup')
]
