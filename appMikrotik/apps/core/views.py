from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('login')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            render(request, 'login.html', {'form':form}, {'error':'Formulario no valido'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def mostrar_logs(request):
    # Aquí puedes agregar la lógica para obtener los logs desde tu base de datos o cualquier otra fuente
    logs = [
        {'tipo': 'atipico', 'actividad': 'Fallo de conexión con Mikrotik', 'modulo': 'Interno', 'fecha': '2024-06-01 12:00:00'},
        {'tipo': 'tipico', 'actividad': 'Jose alejos actualizo su correo electronico', 'modulo': 'Clientes', 'fecha': '2024-06-01 13:00:00'},
        {'tipo': 'tipico', 'actividad': 'Jose alejos cancelo su mensualidad', 'modulo': 'Pagos', 'fecha': '2024-06-01 14:00:00'},
    ]
    return render(request, 'logs.html', {'logs': logs})
