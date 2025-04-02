<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Comment extends Model
{
    use HasFactory;

    /**
     * Los atributos que son asignables en masa.
     *
     * @var array<string>
     */
    protected $fillable = [
        'user_id',
        'image_id',
        'content',
    ];

    /**
     * Obtener el usuario que hizo el comentario.
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    /**
     * Obtener la imagen a la que pertenece el comentario.
     */
    public function image(): BelongsTo
    {
        return $this->belongsTo(Image::class);
    }
}
