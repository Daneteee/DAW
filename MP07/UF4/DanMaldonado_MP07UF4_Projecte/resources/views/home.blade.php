<x-app-layout>
    <div class="max-w-2xl mx-auto px-4 py-6">
        @foreach ($images as $image)
            <div class="mb-6 border rounded-lg p-4 shadow bg-white dark:bg-gray-200 relative">
                <!-- Enlace "Ver Post" en la esquina superior derecha -->
                <a href="{{ route('images.show', $image->id) }}" class="absolute top-4 right-4 text-blue-500 text-sm font-semibold hover:text-blue-700">
                    Ver Post
                </a>

                <div class="flex items-center justify-between">
                    <div>
                        <strong>{{ $image->user->name }} {{ $image->user->surname }}</strong>
                        <span class="text-gray-500 text-sm">· {{ $image->created_at->diffForHumans() }}</span>
                    </div>
                </div>

                <div class="mt-4">
                    <img src="{{ asset('storage/' . $image->image_path) }}" alt="Image" class="w-[500px] rounded mx-auto">
                </div>

                <p class="mt-2 text-gray-800">{{ $image->description }}</p>

                <div class="flex items-center gap-4 mt-3 text-gray-600">
                    <button onclick="toggleLike({{ $image->id }})" id="like-button-{{ $image->id }}">
                        @php
                            $liked = $image->likes->contains('user_id', auth()->id());
                        @endphp
                        <i class="fa-heart fa-regular {{ $liked ? 'fa-solid text-red-500' : '' }}"></i>
                        <span id="like-count-{{ $image->id }}">{{ $image->likes->count() }}</span>
                    </button>

                    <span><i class="fa-regular fa-comment"></i> {{ $image->comments->count() }}</span>
                </div>
            </div>
        @endforeach

        <div class="mt-6">
            {{ $images->links() }}
        </div>
    </div>

    <script>
        function toggleLike(imageId) {
            fetch(`/images/${imageId}/like`, {
                method: 'POST',
                headers: {
                    'X-CSRF-TOKEN': '{{ csrf_token() }}',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            })
            .then(res => res.json())
            .then(data => {
                const heartIcon = document.querySelector(`#like-button-${imageId} i`);
                const likeCount = document.getElementById(`like-count-${imageId}`);

                if (data.liked) {
                    heartIcon.classList.add('fa-solid', 'text-red-500');
                } else {
                    heartIcon.classList.remove('fa-solid', 'text-red-500');
                }

                likeCount.textContent = data.likes_count;
            });
        }
    </script>
</x-app-layout>
