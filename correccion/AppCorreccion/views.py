from django.shortcuts import render, redirect
from .models import Clase
from .forms import BuscaClaseForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from AppCorreccion import forms
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView

# Create your views here.
def inicio(request): 
    return render(request, "AppCorreccion/inicio.html")

def nosotrxs(request):    
    return render(request, "AppCorreccion/nosotrxs.html")


def clase(request):
      
      if request.method == 'POST':
        clase =  Clase(nombre=request.POST['nombre'])
        clase.save()
        return render(request, "AppCorreccion/clase_bien.html")
      return render(request,"AppCorreccion/clase.html")

def buscar_clase(request):
    if request.method == "POST":
        busca_clase = BuscaClaseForm(request.POST)

        if busca_clase.is_valid():
            info = busca_clase.cleaned_data
            clases = Clase.objects.filter(nombre=info["clase"])
            return render(request, "AppCorreccion/lista_clase.html", {"clases": clases})
    else:
        busca_clase = BuscaClaseForm()
        return render(request, "AppCorreccion/buscar_clase.html", {"miFormulario": busca_clase})

def mostrar_clases(request):
    clases = Clase.objects.all()
    contexto= {"clases":clases} 
    return render(request, "AppCorreccion/mostrar_clases.html",contexto)

def eliminar_clase(request, id):
    clase = Clase.objects.get(id=id)
    clase.delete()
    clase = Clase.objects.all()
    contexto = {"clases": clase}
    return render (request, "AppCorreccion/mostrar_clases.html", contexto)

class ClaseDetalle(DetailView):
    model = Clase
    template_name = "AppEntrega/clase_detalle.html"



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

