<x-app-layout>
    <div class="max-w-2xl mx-auto px-4 py-6">
        <div class="mb-6 border rounded-lg p-4 shadow bg-white dark:bg-gray-200">
            <!-- User info and buttons section - unchanged -->
            <div class="flex items-center justify-between">
                <div>
                    <strong>{{ $image->user->name }} {{ $image->user->surname }}</strong>
                    <span class="text-gray-500 text-sm">· {{ $image->created_at->diffForHumans() }}</span>
                </div>

                @if ($image->user_id == auth()->id())
                    <div class="flex space-x-2">
                        <!-- Edit button - unchanged -->
                        <a href="{{ route('images.edit', $image) }}" class="inline-flex items-center justify-center bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-md px-4 py-2 transition-colors duration-200">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                            </svg>
                            Edit
                        </a>

                        <!-- Delete button - unchanged -->
                        <form action="{{ route('images.destroy', $image) }}" method="POST" class="inline-block">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="inline-flex items-center justify-center bg-red-500 hover:bg-red-600 text-white font-medium rounded-md px-4 py-2 transition-colors duration-200" onclick="return confirm('Are you sure you want to delete this image?')">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                </svg>
                                Delete
                            </button>
                        </form>
                    </div>
                @endif
            </div>

            <!-- Image section - unchanged -->
            <div class="mt-4">
                <img src="{{ asset('storage/' . $image->image_path) }}" alt="Image" class="w-full rounded mx-auto">
            </div>

            <p class="mt-2 text-gray-800">{{ $image->description }}</p>

            <!-- Interaction stats - unchanged -->
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


            <!-- Enhanced Comments Section -->
            <div class="mt-6 pt-4 border-t border-gray-200">
                <h3 class="text-xl font-semibold text-gray-800 flex items-center mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                    </svg>
                    Comentaris
                </h3>

                <!-- Comment form - beautified -->
                <form action="{{ route('comments.store', $image->id) }}" method="POST" class="mb-6 bg-gray-50 rounded-lg p-4 border border-gray-200">
                    @csrf
                    <div class="flex flex-col">
                        <textarea 
                            name="content" 
                            rows="2" 
                            class="w-full rounded-lg border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 resize-none" 
                            placeholder="Escriu un comentari..." 
                            required
                        ></textarea>
                        <button 
                            type="submit" 
                            class="self-end mt-3 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors duration-200 flex items-center"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                            </svg>
                            Afegir Comentari
                        </button>
                    </div>
                </form>

                <!-- Comments list - beautifully styled -->
                <div class="space-y-4">
                    @forelse ($image->comments as $comment)
                        <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200">
                            <div class="flex justify-between items-center mb-2">
                                <div class="flex items-center">
                                    <!-- Avatar placeholder - adds visual appeal -->
                                    <div class="w-8 h-8 rounded-full bg-blue-100 text-blue-500 flex items-center justify-center mr-2 font-bold">
                                        {{ substr($comment->user->name, 0, 1) }}
                                    </div>
                                    <span class="font-medium text-gray-800">{{ $comment->user->name }}</span>
                                </div>
                                <span class="text-xs text-gray-500">{{ $comment->created_at->diffForHumans() }}</span>
                            </div>
                            
                            <!-- Comment content -->
                            <div class="pl-10"> <!-- Align with user avatar -->
                                <p class="text-gray-800 mb-3">{{ $comment->content }}</p>
                            </div>

                            @if ($comment->user_id === auth()->id())
                                <div class="pt-2 mt-2 border-t border-gray-100 pl-10">
                                    <div class="flex items-center justify-end space-x-3">
                                        <!-- Simplified edit/delete with cleaner buttons -->
                                        <button 
                                            onclick="toggleEditForm('comment-{{ $comment->id }}')" 
                                            class="text-blue-500 text-xs font-medium hover:text-blue-700 flex items-center"
                                        >
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                            </svg>
                                            Editar
                                        </button>
                                        
                                        <form action="{{ route('comments.destroy', $comment) }}" method="POST">
                                            @csrf
                                            @method('DELETE')
                                            <button 
                                                type="submit" 
                                                class="text-red-500 text-xs font-medium hover:text-red-700 flex items-center" 
                                                onclick="return confirm('Vols eliminar aquest comentari?')"
                                            >
                                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                                </svg>
                                                Eliminar
                                            </button>
                                        </form>
                                    </div>
                                    
                                    <!-- Hidden edit form - toggled by JavaScript -->
                                    <div id="comment-{{ $comment->id }}" class="hidden mt-2">
                                        <form action="{{ route('comments.update', $comment) }}" method="POST" class="flex flex-col">
                                            @csrf
                                            @method('PUT')
                                            <textarea 
                                                name="content" 
                                                class="w-full text-sm border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 resize-none"
                                                rows="2"
                                            >{{ $comment->content }}</textarea>
                                            <div class="flex justify-end space-x-2 mt-2">
                                                <button 
                                                    type="button" 
                                                    onclick="toggleEditForm('comment-{{ $comment->id }}')" 
                                                    class="px-3 py-1 text-xs text-gray-600 hover:text-gray-800"
                                                >
                                                    Cancel·lar
                                                </button>
                                                <button 
                                                    type="submit" 
                                                    class="bg-blue-500 hover:bg-blue-600 text-white text-xs font-medium px-3 py-1 rounded-md"
                                                >
                                                    Actualitzar
                                                </button>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            @endif
                        </div>
                    @empty
                        <div class="bg-gray-50 rounded-lg p-6 text-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-400 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                            </svg>
                            <p class="text-gray-500 font-medium">Encara no hi ha comentaris.</p>
                            <p class="text-gray-400 text-sm mt-1">Sigues el primer en comentar!</p>
                        </div>
                    @endforelse
                </div>
            </div>
        </div>

        <div class="mt-6">
            <a href="{{ route('home') }}" class="inline-flex items-center text-blue-500 hover:text-blue-700 font-medium">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
                Back to Home
            </a>
        </div>
    </div>

    <!-- Això per els formularis d'edició -->
    <script>
        function toggleEditForm(id) {
            const form = document.getElementById(id);
            if (form.classList.contains('hidden')) {
                form.classList.remove('hidden');
            } else {
                form.classList.add('hidden');
            }
        }

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