from django.urls import path
from AppCorreccion import views

urlpatterns = [
        path('',views.inicio, name='inicio')
]