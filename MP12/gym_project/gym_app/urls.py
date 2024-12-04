from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/editar', views.profile_edit, name='profile_edit'),
    path('admin/', admin.site.urls),
    path('entrenador/inici', views.home, name='home'),
    path('entrenador/crear_rutina', views.create_routine, name='create_routine'),
    path('rutines/', views.assign_schedule, name='assign_schedule'),
    path('routines/<int:routine_id>/edit/', views.edit_routine, name='edit_routine'),
    path('routines/<int:routine_id>/delete/', views.delete_routine, name='delete_routine'),
    path('routines/delete/schedule/', views.delete_schedule, name='delete_schedule'),
    # path('test-create/', views.test_create_user, name='test-create'),
]
