from django.urls import path
from AppCorreccion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.inicio, name='inicio'),
        path('nosotrxs',views.nosotrxs, name= "Nosotrxs"),
        
        path('clase/', views.clase, name='clase'),
        path('mostrar_clases/', views.mostrar_clases, name='mostrar_clases'),
        path('buscar_clase/', views.buscar_clase, name="buscar_clase"),
        path('eliminar_clase/<id>/', views.eliminar_clase, name="eliminar_clase"),
        path('clase_detalle/<pk>/', views.ClaseDetalle.as_view(), name="clase_detalle"),

        path('login/', views.login_request, name='login'),
        path('register/', views.register, name='register'),
        path('logout/', views.Logout.as_view(), name='logout'),
        
]

#
#