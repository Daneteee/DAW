from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Routine, Schedule
from django.contrib import messages
from .forms import *

@login_required
def home(request):
    context = {}
    if request.user.role == 'trainer':
        return redirect('assign_schedule') 
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registre completat amb èxit!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Has iniciat sessió correctament!')
                return redirect('home')
            else:
                messages.error(request, 'ERROR: Credencials incorrectes.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'El perfil s\'ha actualitzat correctament.')
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)
        
    return render(request, 'profile_edit.html', {'form': form, 'active_tab': "profile"})


# Comprobar si el usuario tiene el rol de entrenador
def is_trainer(user):
    return user.role == 'trainer'

@login_required
@user_passes_test(is_trainer)
def create_routine(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.trainer = request.user
            routine.save()
            messages.success(request, 'Rutina creada amb èxit!')
            return redirect('home')
    else:
        form = RoutineForm()
    return render(request, 'trainer/create_routine.html', {'form': form, 'active_tab': 'create_routine'})

def success_page(request):
    return render(request, 'success_page.html')

@login_required
@user_passes_test(is_trainer)
def assign_schedule(request):
    routines = Routine.objects.all()
    days_of_week = ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres']
    hours = ['16', '17', '18', '19', '20', '21']
    schedule_data = {}

    for day in days_of_week:
        for hour in hours:
            schedule_entry = Schedule.objects.filter(day=day, time=f"{hour}:00").first()
            schedule_data[f"{day}_{hour}"] = schedule_entry.routine.id if schedule_entry else None

    if request.method == 'POST':
        for key in schedule_data.keys():
            routine_id = request.POST.get(key)
            if routine_id:
                day, hour = key.split('_')
                Schedule.objects.update_or_create(
                    day=day,
                    time=f"{hour}:00",
                    defaults={'routine_id': routine_id}
                )

        messages.success(request, 'Les rutines han sigut assignades correctament.')

        return redirect('assign_schedule')

    return render(request, 'trainer/assign_schedule.html', {
        'routines': routines,
        'days_of_week': days_of_week,
        'hours': hours,
        'schedule_data': schedule_data,
    })

@login_required
@user_passes_test(is_trainer)
def edit_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rutina actualitzada amb èxit.')
            return redirect('assign_schedule')
    else:
        form = RoutineForm(instance=routine)
    return render(request, 'trainer/edit_routine.html', {'form': form, 'routine': routine})

@login_required
@user_passes_test(is_trainer)
def delete_schedule(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        time = request.POST.get('time')

        # Eliminar la entrada del horario correspondiente
        Schedule.objects.filter(day=day, time=time).delete()

        messages.success(request, 'La rutina ha sido eliminada del horario.')
        return redirect('assign_schedule')  # Redirige a la página de asignación de horarios

    return redirect('assign_schedule')  # Redirige si no es un POST

@login_required
@user_passes_test(is_trainer)
def delete_routine(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    if request.method == 'POST':
        routine.delete()
        messages.success(request, 'Rutina eliminada con éxito.')
        return redirect('assign_schedule')
    return redirect('home')