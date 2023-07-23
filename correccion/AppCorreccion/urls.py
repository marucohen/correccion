from django.urls import path
from AppCorreccion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.inicio, name='inicio'),
        
        path('curso/', views.curso, name='curso'),
        path('mostrar_cursos/', views.mostrar_cursos, name='mostrar_cursos'),
        path('buscar_curso/', views.buscar_curso, name="buscar_curso"),
        path('eliminar-curso/<id>/', views.eliminar_curso, name="eliminar_curso"),
        path('curso_detalle/<pk>/', views.CursoDetalle.as_view(), name="curso_detalle"),

        path('login/', views.login_request, name='login'),
        path('register/', views.register, name='register'),
        path('logout/', views.Logout.as_view(), name='logout'),
        
]

#
#