from datetime import datetime

dades_tasques = [
    {
        "descripcio": "Estudiar per l'examen de matemàtiques",
        "datalimit": datetime(2024, 3, 15, 12, 0),  # data límit: 15 de març de 2024 a les 12:00
        "usuari": "Joan",
        "durada": 2,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Preparar presentació per la reunió",
        "datalimit": datetime(2024, 3, 18, 15, 30),  # data límit: 18 de març de 2024 a les 15:30
        "usuari": "Maria",
        "durada": 3,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Comprar ingredients per al sopar",
        "datalimit": datetime(2024, 3, 12, 18, 0),  # data límit: 12 de març de 2024 a les 18:00
        "usuari": "Pere",
        "durada": 1,  # durada en hores
        "prioritat": "Baixa"
    },
    # Afegir més tasques aquí...
    {
        "descripcio": "Fer la neteja general de la casa",
        "datalimit": datetime(2024, 3, 20, 10, 0),  # data límit: 20 de març de 2024 a les 10:00
        "usuari": "Anna",
        "durada": 4,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Planificar les vacances d'estiu",
        "datalimit": datetime(2024, 4, 1, 12, 0),  # data límit: 1 d'abril de 2024 a les 12:00
        "usuari": "Pau",
        "durada": 2,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Fer la compra setmanal",
        "datalimit": datetime(2024, 3, 10, 17, 0),  # data límit: 10 de març de 2024 a les 17:00
        "usuari": "Marta",
        "durada": 1,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Revisar els informes de vendes",
        "datalimit": datetime(2024, 3, 25, 9, 30),  # data límit: 25 de març de 2024 a les 9:30
        "usuari": "Jordi",
        "durada": 2,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Entrenar per a la marató",
        "datalimit": datetime(2024, 3, 22, 8, 0),  # data límit: 22 de març de 2024 a les 8:00
        "usuari": "Lola",
        "durada": 3,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Preparar proposta de projecte",
        "datalimit": datetime(2024, 3, 28, 16, 0),  # data límit: 28 de març de 2024 a les 16:00
        "usuari": "Carlos",
        "durada": 4,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Organitzar festa d'aniversari",
        "datalimit": datetime(2024, 3, 14, 20, 0),  # data límit: 14 de març de 2024 a les 20:00
        "usuari": "Laura",
        "durada": 3,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Configurar nova impressora",
        "datalimit": datetime(2024, 3, 9, 11, 0),  # data límit: 9 de març de 2024 a les 11:00
        "usuari": "David",
        "durada": 2,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Escoltar la nova conferència sobre IA",
        "datalimit": datetime(2024, 3, 16, 14, 0),  # data límit: 16 de març de 2024 a les 14:00
        "usuari": "Eva",
        "durada": 1,  # durada en hores
        "prioritat": "Baixa"
    },
    {
        "descripcio": "Fer el manteniment del jardí",
        "datalimit": datetime(2024, 3, 19, 9, 0),  # data límit: 19 de març de 2024 a les 9:00
        "usuari": "Marc",
        "durada": 2,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Redactar informe sobre el projecte",
        "datalimit": datetime(2024, 3, 23, 17, 0),  # data límit: 23 de març de 2024 a les 17:00
        "usuari": "Sara",
        "durada": 3,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Reunir-se amb el client per aclarir dubtes",
        "datalimit": datetime(2024, 3, 29, 10, 30),  # data límit: 29 de març de 2024 a les 10:30
        "usuari": "Pablo",
        "durada": 2,  # durada en hores
        "prioritat": "Alta"
    },
    {
        "descripcio": "Fer el seguiment de les activitats del club",
        "datalimit": datetime(2024, 3, 13, 16, 0),  # data límit: 13 de març de 2024 a les 16:00
        "usuari": "Núria",
        "durada": 1,  # durada en hores
        "prioritat": "Baixa"
    },
    {
        "descripcio": "Instal·lar les actualitzacions del sistema",
        "datalimit": datetime(2024, 3, 17, 10, 0),  # data límit: 17 de març de 2024 a les 10:00
        "usuari": "Aleix",
        "durada": 2,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Investigar noves tecnologies",
        "datalimit": datetime(2024, 3, 21, 14, 0),  # data límit: 21 de març de 2024 a les 14:00
        "usuari": "Clàudia",
        "durada": 3,  # durada en hores
        "prioritat": "Mitjana"
    },
    {
        "descripcio": "Preparar el guió del vídeo promocional",
        "datalimit": datetime(2024, 3, 26, 9, 0),  # data límit: 26 de març de 2024 a les 9:00
        "usuari": "Aina",
        "durada": 2,  # durada en hores
        "prioritat": "Alta"
    }
]