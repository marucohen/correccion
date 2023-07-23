from django.shortcuts import render, redirect
from .models import Curso
from .forms import BuscaCursoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from AppCorreccion import forms
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView

# Create your views here.
def inicio(request): 
    return render(request, "AppCorreccion/inicio.html")

def curso(request):
      
      if request.method == 'POST':
        curso =  Curso(nombre=request.POST['nombre'])
        curso.save()
        return render(request, "AppCorreccion/curso_bien.html")
      return render(request,"AppCorreccion/curso.html")

def buscar_curso(request):
    if request.method == "POST":
        busca_curso = BuscaCursoForm(request.POST)

        if busca_curso.is_valid():
            info = busca_curso.cleaned_data
            cursos = Curso.objects.filter(nombre=info["curso"])
            return render(request, "AppCorreccion/lista_curso.html", {"cursos": cursos})
    else:
        busca_curso = BuscaCursoForm()
        return render(request, "AppCorreccion/buscar_curso.html", {"miFormulario": busca_curso})

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto= {"cursos":cursos} 
    return render(request, "AppCorreccion/mostrar_cursos.html",contexto)

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    contexto = {"cursos": curso}
    return render (request, "AppCorreccion/mostrar_cursos.html", contexto)

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppEntrega/curso_detalle.html"



def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'AppCorreccion/registro.html', {'form':form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'AppCorreccion/registro.html', {'form':form})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "AppCorreccion/login.html", {"mensaje": "Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, "AppCorreccion/login.html", {"form": form})

class Logout(LogoutView):
    template_name = 'AppCorreccion/logout.html'

#def clases(request):


#def nosotros(request):


#def blog(request):

