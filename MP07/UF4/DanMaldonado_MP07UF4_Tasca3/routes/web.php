<?php
use App\Http\Controllers\TasksController;
use Illuminate\Support\Facades\Route;
use Illuminate\Http\Response;
use Illuminate\Http\Request;
use Carbon\Carbon;

class Task
{
  public function __construct(
    public int $id,
    public string $title,
    public string $description,
    public ?string $long_description,
    public bool $completed,
    public string $created_at,
    public string $updated_at
  ) {
  }
}

$tasks = [
  new Task(
    1,
    'Buy groceries',
    'Task 1 description',
    'Task 1 long description',
    false,
    '2023-03-01 12:00:00',
    '2023-03-01 12:00:00'
  ),
  new Task(
    2,
    'Sell old stuff',
    'Task 2 description',
    null,
    false,
    '2023-03-02 12:00:00',
    '2023-03-02 12:00:00'
  ),
  new Task(
    3,
    'Learn programming',
    'Task 3 description',
    'Task 3 long description',
    true,
    '2023-03-03 12:00:00',
    '2023-03-03 12:00:00'
  ),
  new Task(
    4,
    'Take dogs for a walk',
    'Task 4 description',
    null,
    false,
    '2023-03-04 12:00:00',
    '2023-03-04 12:00:00'
  ),
];


Route::get('/', function () {
    return redirect()->route('tasks.index');
});


Route::get('/tasks', function () use ($tasks) {
    return view('tasks.index', [
        'tasks' => $tasks
    ]);
})->name('tasks.index');


Route::get('/tasks/{id}', function ($id) use ($tasks){
    $task = collect($tasks)->firstWhere('id', $id);

    if (!$task) {
        abort(Response::HTPP_NOT_FOUND);
    }

    return view('/tasks/show', [
        'task' => $task
    ]);
})->name('tasks.show');

Route::prefix('tasca3')->group(function () use($tasks) {
  
  Route::get('/resposta', function (Request $request) use ($tasks) {
    // Obtenim el titol de les tasques
    $titles = collect($tasks)->pluck('title');
  
    // Creem la resposta JSON amb codi d'estat 201
    $response = response()->json($titles, 201);
  
    // Afegim la cookie
    return $response->cookie('tasca1', $tasks[0]->title, 2);
  })->name('tasca3.resposta');
  
  Route::get('/redirigeix', function () {
    return redirect('/');
  });
  
  Route::get('/torna', function () {
    return back();
  });
  
  Route::get('/alaruta', function () {
    return redirect()->route('tasks.index');
  });
  
  Route::get('/porai', function () {
    return redirect()->away('https://www.youtube.com');
  });
  
  Route::get('/json', function () use ($tasks) {
    // Filtrem tasques no completades
    $filteredTasks = collect($tasks)
        ->where('completed', false)
        ->map(fn($task) => [
            'title' => $task->title,
            'description' => $task->description
        ]);
  
    return response()->json($filteredTasks);
  });
  
  Route::get('/baixa', function () {
    $path = public_path('img/radar.jpg');
    $filename = 'radar_' . Carbon::now()->format('Y-m-d') . '.jpg'; 
  
    if (!file_exists($path)) {
        abort(404, 'Imatge no trobada');
    }
  
    return response()->download($path, $filename);
  });

  Route::get('/controlmajors', function () {
    $edat = request()->query('edat', 'No especificada');
    return view('tasks.controlmajors', compact('edat'));
  })->middleware('majors');  
});  



