<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InstaDan</title>

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        /* Custom styles */
        .hero {
            background-image: url('https://via.placeholder.com/1920x1080');
            background-size: cover;
            background-position: center;
            height: 100vh;
        }
    </style>
</head>
<body class="font-roboto">

    <!-- Navbar -->
    <nav class="bg-gray-900 text-white p-4 fixed w-full top-0 left-0 z-50">
        <div class="container mx-auto flex justify-between items-center">
            <div class="text-lg font-bold">
                <a href="#" class="text-white">InstaDan</a>
            </div>
            <div class="space-x-4">
                <a href="{{ route('login') }}" class="bg-blue-500 px-4 py-2 rounded hover:bg-blue-600">Inicia sessió</a>
                <a href="{{ route('register') }}" class="bg-green-500 px-4 py-2 rounded hover:bg-green-600">Registra't</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero flex justify-center items-center text-center text-white">
        <div class="bg-black bg-opacity-50 p-10 rounded-lg">
            <h1 class="text-4xl sm:text-5xl font-bold mb-4">Benvingut a InstaDan</h1>
            <p class="text-lg sm:text-xl mb-6">Un lloc per connectar, compartir i descobrir moments increïbles.</p>
            <a href="{{ route('register') }}" class="bg-yellow-500 text-gray-900 px-6 py-3 rounded-lg text-lg font-semibold hover:bg-yellow-600">Comença ara</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white p-4 mt-10 text-center">
        <p>© 2025 InstaDan. Tots els drets reservats.</p>
    </footer>

</body>
</html>
