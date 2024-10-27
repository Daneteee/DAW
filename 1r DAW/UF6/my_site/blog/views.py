from django.shortcuts import render, get_object_or_404

from .models import Author, Tag, Post

# Dades fake
all_posts = {
    "autors": [
        {"first_name": "Carlos", "last_name": "González", "email": "carlos.gonzalez@example.com"},
        {"first_name": "Laura", "last_name": "Martínez", "email": "laura.martinez@example.com"},
        {"first_name": "Pedro", "last_name": "Rodríguez", "email": "pedro.rodriguez@example.com"},
        {"first_name": "María", "last_name": "Pérez", "email": "maria.perez@example.com"},
        {"first_name": "David", "last_name": "Sánchez", "email": "david.sanchez@example.com"}
    ],
    "tags": [
        {"caption": "Programación"},
        {"caption": "Seguridad"},
        {"caption": "Desarrollo Web"},
        {"caption": "Bases de Datos"},
        {"caption": "Inteligencia Artificial"}
    ], "posts": [
        {
            "slug": "introduccion-algoritmos",
            "image": "img1.jpg",
            "author": "Carlos González",
            "date": "2024-05-15",
            "title": "Introducción a los algoritmos",
            "excerpt": "Conceptos básicos sobre algoritmos y su importancia en la programación.",
            "content": "Los algoritmos son instrucciones paso a paso para resolver un problema o realizar una tarea. "
                       "Son fundamentales en la programación y se utilizan en todo tipo de aplicaciones, "
                       "desde ordenar datos hasta buscar información en una base de datos. En este post, "
                       "proporcionaremos una introducción a los algoritmos y discutiremos su importancia en el mundo "
                       "de la programación.",
            "tags": ["Programación", "Desarrollo Web"]
        },
        {
            "slug": "principios-seguridad-informatica",
            "image": "img2.jpg",
            "author": "Laura Martínez",
            "date": "2024-05-12",
            "title": "Principios básicos de seguridad informática",
            "excerpt": "Consejos esenciales para proteger tu información y tus sistemas contra amenazas de seguridad.",
            "content": "La seguridad informática es un aspecto crítico en el mundo digital actual. Con el aumento de "
                       "ciberataques y brechas de seguridad, es importante comprender los principios básicos de la "
                       "seguridad informática y cómo proteger tus sistemas y datos. En este post, exploraremos "
                       "algunos consejos esenciales para mejorar la seguridad informática en tus proyectos y sistemas.",
            "tags": ["Seguridad"]
        },
        {
            "slug": "desarrollo-web-moderno",
            "image": "img3.jpg",
            "author": "Pedro Rodríguez",
            "date": "2024-05-10",
            "title": "Desarrollo web moderno: tendencias y tecnologías",
            "excerpt": "Exploración de las últimas tendencias y tecnologías en el desarrollo web moderno.",
            "content": "El desarrollo web ha evolucionado rápidamente en los últimos años con la introducción de "
                       "nuevas tecnologías y prácticas. Desde frameworks frontend como React y Angular hasta "
                       "herramientas de automatización de tareas como Webpack y Gulp, hay mucho que explorar en el "
                       "mundo del desarrollo web moderno. En este post, discutiremos algunas de las tendencias y "
                       "tecnologías más importantes en el desarrollo web actual.",
            "tags": ["Desarrollo Web"]
        },
        {
            "slug": "optimizacion-bases-datos",
            "image": "img4.jpg",
            "author": "María Pérez",
            "date": "2024-05-08",
            "title": "Optimización de bases de datos: mejores prácticas",
            "excerpt": "Consejos para optimizar el rendimiento y la eficiencia de las bases de datos en tus "
                       "aplicaciones.",
            "content": "Las bases de datos son componentes fundamentales de muchas aplicaciones modernas, "
                       "y su rendimiento y eficiencia son críticos para el éxito del proyecto. En este post, "
                       "compartiremos algunas mejores prácticas para optimizar bases de datos, incluyendo la "
                       "indexación adecuada, la normalización de datos y la optimización de consultas.",
            "tags": ["Bases de Datos"]
        },
        {
            "slug": "inteligencia-artificial-futuro",
            "image": "img1.jpg",
            "author": "David Sánchez",
            "date": "2024-05-06",
            "title": "Inteligencia artificial: el futuro de la tecnología",
            "excerpt": "Exploración del impacto de la inteligencia artificial en nuestra sociedad y el futuro de la "
                       "tecnología.",
            "content": "La inteligencia artificial (IA) está transformando rápidamente la forma en que interactuamos "
                       "con la tecnología y el mundo que nos rodea. Desde asistentes virtuales hasta sistemas de "
                       "recomendación y vehículos autónomos, la IA está presente en una amplia variedad de "
                       "aplicaciones. En este post, discutiremos el impacto de la inteligencia artificial en nuestra "
                       "sociedad y exploraremos el emocionante futuro de esta tecnología.",
            "tags": ["Inteligencia Artificial"]
        },
        {
            "slug": "conceptos-basicos-machine-learning",
            "image": "img1.jpg",
            "author": "Laura Martínez",
            "date": "2024-05-20",
            "title": "Conceptos básicos de machine learning",
            "excerpt": "Introducción a los fundamentos del aprendizaje automático y sus aplicaciones.",
            "content": "El aprendizaje automático es una rama de la inteligencia artificial que se centra en el "
                       "desarrollo de algoritmos y modelos que permiten a las computadoras aprender a realizar tareas "
                       "sin ser programadas explícitamente para cada una de ellas. En este post, exploraremos los "
                       "conceptos"
                       "básicos del aprendizaje automático y algunas de sus aplicaciones más comunes.",
            "tags": ["Inteligencia Artificial"]
        },
        {
            "slug": "consejos-trucos-python",
            "image": "img2.jpg",
            "author": "Pedro Rodríguez",
            "date": "2024-05-18",
            "title": "Consejos y trucos de Python",
            "excerpt": "Consejos prácticos para mejorar tu programación en Python.",
            "content": "Python es uno de los lenguajes de programación más populares y versátiles, utilizado en una "
                       "amplia gama de aplicaciones, desde desarrollo web hasta análisis de datos y aprendizaje "
                       "automático. En este post, compartiré algunos consejos y trucos útiles para mejorar tu fluidez y"
                       "eficiencia en Python.",
            "tags": ["Programación"]
        },
        {
            "slug": "mejores-practicas-ciberseguridad",
            "image": "img3.jpg",
            "author": "Laura Martínez",
            "date": "2024-05-16",
            "title": "Mejores prácticas de ciberseguridad",
            "excerpt": "Consejos esenciales para proteger tus sistemas y datos contra amenazas cibernéticas.",
            "content": "La ciberseguridad es una preocupación cada vez mayor en el mundo digital actual. Con el aumento"
                       "de los ciberataques y las brechas de seguridad, es fundamental implementar medidas sólidas de "
                       "ciberseguridad para proteger tus sistemas y datos. En este post, discutiré algunas mejores "
                       "prácticas de ciberseguridad que puedes implementar para proteger tus activos digitales.",
            "tags": ["Seguridad"]
        },
        {
            "slug": "comparacion-frameworks-frontend",
            "image": "img4.jpg",
            "author": "Carlos González",
            "date": "2024-05-14",
            "title": "Comparación de frameworks frontend",
            "excerpt": "Análisis comparativo de los principales frameworks frontend: React, Angular y Vue.",
            "content": "Los frameworks frontend son herramientas fundamentales para el desarrollo de aplicaciones web "
                       "modernas. React, Angular y Vue son tres de los frameworks más populares en la actualidad, "
                       "cada uno con sus propias fortalezas y debilidades. En este post, compararé estos tres "
                       "frameworks"
                       "en términos de rendimiento, facilidad de uso, comunidad de desarrollo y más.",
            "tags": ["Desarrollo Web"]
        },
        {
            "slug": "diseno-bases-datos-sql",
            "image": "img1.jpg",
            "author": "María Pérez",
            "date": "2024-05-12",
            "title": "Diseño de bases de datos SQL",
            "excerpt": "Principios y mejores prácticas para el diseño eficiente de bases de datos SQL.",
            "content": "El diseño de bases de datos SQL es una parte crucial del desarrollo de aplicaciones que "
                       "dependen"
                       "de bases de datos relacionales. Un diseño eficiente puede mejorar el rendimiento, "
                       "la escalabilidad y la facilidad de mantenimiento de tu aplicación. En este post, compartiré "
                       "algunos principios y mejores prácticas para el diseño de bases de datos SQL que te ayudarán a "
                       "construir sistemas robustos y eficientes.",
            "tags": ["Bases de Datos"]
        },
        {
            "slug": "redes-neuronales-explicadas",
            "image": "img2.jpg",
            "author": "David Sánchez",
            "date": "2024-05-10",
            "title": "Redes neuronales explicadas",
            "excerpt": "Introducción a la arquitectura y funcionamiento de las redes neuronales.",
            "content": "Las redes neuronales son un componente clave del aprendizaje profundo y la inteligencia "
                       "artificial. Están inspiradas en la estructura y función del cerebro humano y se utilizan en una"
                       "amplia variedad de aplicaciones, desde reconocimiento de imágenes hasta procesamiento del "
                       "lenguaje natural. En este post, explicaré la arquitectura y el funcionamiento básico de las "
                       "redes"
                       "neuronales.",
            "tags": ["Inteligencia Artificial"]
        },
        {
            "slug": "diseno-web-adaptable",
            "image": "img3.jpg",
            "author": "Laura Martínez",
            "date": "2024-05-08",
            "title": "Diseño web adaptable",
            "excerpt": "Principios y técnicas para crear sitios web que se adapten a diferentes dispositivos y "
                       "pantallas.",
            "content": "El diseño web adaptable es una técnica que permite que un sitio web se adapte y se vea bien en "
                       "una variedad de dispositivos y tamaños de pantalla. En este post, exploraremos los principios "
                       "básicos del diseño web adaptable y algunas técnicas comunes para implementarlo en tus "
                       "proyectos.",
            "tags": ["Desarrollo Web"]
        },
        {
            "slug": "herramientas-visualizacion-datos",
            "image": "img4.jpg",
            "author": "Carlos González",
            "date": "2024-05-06",
            "title": "Herramientas de visualización de datos",
            "excerpt": "Una guía de las mejores herramientas para visualizar datos de manera efectiva.",
            "content": "La visualización de datos es una parte fundamental del análisis de datos y la comunicación de "
                       "información. Existen diversas herramientas disponibles para crear visualizaciones impactantes "
                       "y significativas. En este post, exploraremos algunas de las mejores herramientas de "
                       "visualización de datos y discutiremos sus características y casos de uso.",
            "tags": ["Programación", "Bases de Datos"]
        },
        {
            "slug": "conceptos-basicos-computacion-nube",
            "image": "img1.jpg",
            "author": "María Pérez",
            "date": "2024-05-04",
            "title": "Conceptos básicos de computación en la nube",
            "excerpt": "Una introducción a los fundamentos de la computación en la nube y sus beneficios.",
            "content": "La computación en la nube ha revolucionado la forma en que las empresas gestionan sus "
                       "recursos informáticos y ofrecen servicios digitales. En este post, exploraremos los conceptos "
                       "básicos de la computación en la nube, incluyendo modelos de servicio, "
                       "tipos de implementaciones y beneficios clave que ofrece esta tecnología.",
            "tags": ["Tecnología"]
        },
        {
            "slug": "mejores-practicas-seguridad-web",
            "image": "img2.jpg",
            "author": "David Sánchez",
            "date": "2024-05-02",
            "title": "Mejores prácticas de seguridad web",
            "excerpt": "Consejos esenciales para proteger tus aplicaciones web contra vulnerabilidades de seguridad.",
            "content": "La seguridad web es una preocupación crítica para cualquier sitio web o aplicación en línea. "
                       "Con el aumento de los ataques cibernéticos y las brechas de seguridad, es importante "
                       "implementar medidas sólidas de seguridad para proteger tus datos y la privacidad de tus "
                       "usuarios. En este post, discutiré algunas mejores prácticas de seguridad web que puedes "
                       "aplicar para fortalecer la seguridad de tus aplicaciones.",
            "tags": ["Seguridad", "Desarrollo Web"]
        }
    ]
}

# Afegim els autors a la base de dades
for autor_data in all_posts["autors"]:
    autor, created = Author.objects.get_or_create(
        first_name=autor_data["first_name"],
        last_name=autor_data["last_name"],
        email=autor_data["email"]
    )

# Afegim els tags a la base de dades
for tag_data in all_posts["tags"]:
    tag, created = Tag.objects.get_or_create(
        caption=tag_data["caption"]
    )

# Afegim els posts a la base de dades
for post_data in all_posts["posts"]:
    autor = Author.objects.get(first_name=post_data["author"].split()[0], last_name=post_data["author"].split()[1])

    tags = [Tag.objects.get_or_create(caption=tag_caption)[0] for tag_caption in post_data["tags"]]

    slug = post_data["slug"]

    post, created = Post.objects.get_or_create(
        title=post_data["title"],
        excerpt=post_data["excerpt"],
        image_name=post_data["image"],
        date=post_data["date"],
        slug=slug,
        content=post_data["content"],
        author=autor
    )
    post.tags.add(*tags)


# Vista principal
def starting_page(request):
    # Ordenem els posts per data i li passem a la vista
    sorted_posts = Post.objects.all().order_by('-date')
    return render(request, 'my_site/index.html', {'posts': sorted_posts})


# Vista per mostrar tots els posts
def posts(request):
    posts_objects = Post.objects.all()
    return render(request, 'my_site/all_posts.html', {'posts': posts_objects})


# Vista per mostrar un post en concret
def post_detail(request, slug_):
    post_ = get_object_or_404(Post, slug=slug_)
    return render(request, 'my_site/post_detail.html', {'post': post_})


# Vista per mostrar tots els autors
def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'my_site/all_authors.html', {'authors': authors})


# Vista per mostrar un autor en concret
def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'my_site/author_detail.html', {'author': author})


# Vista per mostrar tots els tags
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'my_site/all_tags.html', {'tags': tags})


# Vista per mostrar un tag en concret
def tag_posts(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    return render(request, 'my_site/tag_posts.html', {'tag': tag})


#  Vista per mostrar la pàgina 404
def custom_404_page(request, exception):
    return render(request, '404.html', status=404)
