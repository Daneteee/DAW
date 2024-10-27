from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
horari_primer_DAW = {
    'dilluns': {
        'classes': [
            {'hora_inici': '15:00', 'hora_fi': '15:55', 'modul': 'Entorns de desenvolupament'},
            {'hora_inici': '16:25', 'hora_fi': '17:20', 'modul': 'Entorns de desenvolupament'},
            {'hora_inici': '17:50', 'hora_fi': '18:45', 'modul': 'Sistemes informàtics'},
            {'hora_inici': '19:15', 'hora_fi': '20:10', 'modul': 'Sistemes informàtics'},
        ]
    },
    'dimarts': {
        'classes': [
            {'hora_inici': '15:00', 'hora_fi': '15:55', 'modul': 'Bases de dades'},
            {'hora_inici': '16:25', 'hora_fi': '17:20', 'modul': 'Bases de dades'},
            {'hora_inici': '17:50', 'hora_fi': '18:45', 'modul': 'Programació'},
            {'hora_inici': '19:15', 'hora_fi': '20:10', 'modul': 'Programació'},
        ]
    },
    'dimecres': {
        'classes': [
            {'hora_inici': '15:00', 'hora_fi': '15:55', 'modul': 'Llenguatge de marques'},
            {'hora_inici': '16:25', 'hora_fi': '17:20', 'modul': 'Llenguatge de marques'},
            {'hora_inici': '17:50', 'hora_fi': '18:45', 'modul': 'Entorns de desenvolupament'},
            {'hora_inici': '19:15', 'hora_fi': '20:10', 'modul': 'Entorns de desenvolupament'},
        ]
    },
    'dijous': {
        'classes': [
            {'hora_inici': '15:00', 'hora_fi': '15:55', 'modul': 'Sistemes informàtics'},
            {'hora_inici': '16:25', 'hora_fi': '17:20', 'modul': 'Sistemes informàtics'},
            {'hora_inici': '17:50', 'hora_fi': '18:45', 'modul': 'Programació'},
            {'hora_inici': '19:15', 'hora_fi': '20:10', 'modul': 'Programació'},
        ]
    },
    'divendres': {
        'classes': [
            {'hora_inici': '15:00', 'hora_fi': '15:55', 'modul': 'Bases de dades'},
            {'hora_inici': '16:25', 'hora_fi': '17:20', 'modul': 'Bases de dades'},
            {'hora_inici': '17:50', 'hora_fi': '18:45', 'modul': 'Llenguatge de marques'},
            {'hora_inici': '19:15', 'hora_fi': '20:10', 'modul': 'Llenguatge de marques'},
        ]
    }
}


def index(request):
    days = ["dilluns", "dimarts", "dimecres", "dijous", "divendres"]
    return render(request, template_name='primer_daw/index.html', context={'days': days})


def show_calendar(request, day):
    try:
        horari_dia = {'day_schedule': horari_primer_DAW[day], 'day': day,
                        "days": ["dilluns", "dimarts", "dimecres", "dijous", "divendres"]}
        return render(request, template_name='primer_daw/horari_dia.html', context=horari_dia)
    except KeyError:
        return HttpResponse(f"El día <b>{day}</b> no existe.")


