from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<str:day>/", views.show_calendar, name="show_calendar")
]

