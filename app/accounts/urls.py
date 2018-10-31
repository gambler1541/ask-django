from django.urls import path
from .views import auth_login, profile

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('profile/', profile, name='profile'),

]
