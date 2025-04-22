<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">Edit Post</h2>
    </x-slot>

    <div class="py-6">
        <div class="max-w-3xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white p-8 rounded-lg shadow-md">
                <!-- Botón para volver al post -->
                <a href="{{ route('images.show', $image) }}" class="text-blue-600 hover:text-blue-800 mb-4 inline-block">← Back to Post</a>

                <form action="{{ route('images.update', $image) }}" method="POST" enctype="multipart/form-data" class="space-y-6">
                    @csrf
                    @method('PUT')

                    <div>
                        <x-input-label for="image" value="Image" />
                        <x-text-input id="image" name="image" type="file" class="mt-1 block w-full" onchange="previewImage(event)" />
                        <x-input-error :messages="$errors->get('image')" class="mt-2" />
                    </div>

                    <!-- Vista previa de la imagen -->
                    <div id="image-preview-container" class="mt-4">
                        @if($image->image_path)
                            <img id="image-preview" src="{{ asset('storage/' . $image->image_path) }}" alt="Image preview" class="w-full h-auto">
                        @else
                            <img id="image-preview" src="" alt="Image preview" class="w-full h-auto hidden" />
                        @endif
                    </div>

                    <div>
                        <x-input-label for="description" value="Description" />
                        <textarea id="description" name="description" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm" rows="3">{{ old('description', $image->description) }}</textarea>
                        <x-input-error :messages="$errors->get('description')" class="mt-2" />
                    </div>

                    <x-primary-button>Update</x-primary-button>
                </form>
            </div>
        </div>
    </div>

    <script>
        function previewImage(event) {
            const file = event.target.files[0];
            const preview = document.getElementById('image-preview');
            const previewContainer = document.getElementById('image-preview-container');

            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.classList.remove('hidden'); // Mostrar la imagen
                };
                reader.readAsDataURL(file);
            } else {
                preview.classList.add('hidden'); // Ocultar si no hay archivo
            }
        }
    </script>
</x-app-layout>
