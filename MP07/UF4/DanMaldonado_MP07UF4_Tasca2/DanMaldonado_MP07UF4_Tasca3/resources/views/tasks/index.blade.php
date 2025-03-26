@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Llista de Tasques</h1>
        <ul class="list-group">
            @forelse ($tasks as $task)
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>
                            <a href="{{ route('tasks.show', ['id' => $task->id]) }}">
                                {{ $task->title }}
                            </a>
                        </strong> - {{ $task->description }}
                        @if ($task->long_description)
                            <br><small>{{ $task->long_description }}</small>
                        @endif
                    </div>
                    <span class="badge bg-{{ $task->completed ? 'success' : 'warning' }}">
                        {{ $task->completed ? 'Completa' : 'Pendent' }}
                    </span>
                </li>
            @empty
                <li class="list-group-item text-center">No hi ha tasques disponibles.</li>
            @endforelse
        </ul>
    </div>
@endsection


