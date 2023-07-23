from django.contrib import admin
from .models import Clase, Account
#from .models import acá ira cada clase que cree en los modelos


# Register your models here.
admin.site.register(Clase)
admin.site.register(Account)
