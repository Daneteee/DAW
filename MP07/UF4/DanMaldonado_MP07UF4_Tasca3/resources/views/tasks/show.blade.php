@extends('layouts.app')

@section('title', 'Detall de la Tasca')

@section('content')
    <div class="container">
        <h1>{{ $task->title }}</h1>
        <p><strong>Descripció:</strong> {{ $task->description }}</p>

        @if ($task->long_description)
            <p><strong>Descripció llarga:</strong> {{ $task->long_description }}</p>
        @endif

        <p><strong>Estat:</strong>
            <span class="badge bg-{{ $task->completed ? 'success' : 'warning' }}">
                {{ $task->completed ? 'Completa' : 'Pendent' }}
            </span>
        </p>

        <p><strong>Data de creació:</strong> {{ $task->created_at }}</p>
        <p><strong>Última actualització:</strong> {{ $task->updated_at }}</p>

        <a href="{{ route('tasks.index') }}" class="btn btn-primary">Tornar a la llista</a>
    </div>
@endsection

