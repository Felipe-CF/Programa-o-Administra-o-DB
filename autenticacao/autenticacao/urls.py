from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/registro', RegistroUsuarioView.as_view(), name='registro'),
    path('api/auth/login', LoginUsuarioView.as_view(), name='login'),
    path('api/auth/logout', LogoutUsuarioView.as_view(), name='logout'),
]
