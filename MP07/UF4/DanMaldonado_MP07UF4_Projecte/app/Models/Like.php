<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Like extends Model
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
    ];

    /**
     * Obtener el usuario que dio el like.
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    /**
     * Obtener la imagen a la que se le dio el like.
     */
    public function image(): BelongsTo
    {
        return $this->belongsTo(Image::class);
    }
}
