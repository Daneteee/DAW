export function drawGrid(ctx, camera, gridSize, mapWidth, mapHeight) {
    const startX = Math.floor(camera.x / gridSize) * gridSize;
    const startY = Math.floor(camera.y / gridSize) * gridSize;

    const endX = startX + ctx.canvas.width + gridSize;
    const endY = startY + ctx.canvas.height + gridSize;

    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;

    for (let x = startX; x < endX; x += gridSize) {
        ctx.beginPath();
        ctx.moveTo(x - camera.x, 0);
        ctx.lineTo(x - camera.x, ctx.canvas.height);
        ctx.stroke();
    }

    for (let y = startY; y < endY; y += gridSize) {
        ctx.beginPath();
        ctx.moveTo(0, y - camera.y);
        ctx.lineTo(ctx.canvas.width, y - camera.y);
        ctx.stroke();
    }

    // Bordes del mapa
    ctx.strokeStyle = '#ff0000';
    ctx.lineWidth = 2;
    ctx.strokeRect(-camera.x, -camera.y, mapWidth, mapHeight);
}

/**
 * Dibuja un jugador (puede ser el principal o un oponente).
 */
export function drawPlayer(ctx, player, camera) {
    ctx.beginPath();
    ctx.arc(player.x - camera.x, player.y - camera.y, player.radius, 0, Math.PI * 2);

    // Cambiar color según estado
    if (player.isDashing) {
        ctx.fillStyle = '#00ff00'; // Verde si está haciendo dash
    } else if (player.isAttacking) {
        ctx.fillStyle = '#ff0000'; // Rojo si está atacando
    } else {
        ctx.fillStyle = 'white'; // Blanco por defecto
    }
    ctx.fill();
}

/**
 * Dibuja todos los jugadores (excepto el principal).
 */
export function drawPlayers(ctx, players, camera, radius) {
    players.forEach(player => {
        ctx.beginPath();
        ctx.arc(player.x - camera.x, player.y - camera.y, radius, 0, Math.PI * 2);
        ctx.fillStyle = '#888'; // Color para otros jugadores
        ctx.fill();

        if (player.isAttacking) {
            ctx.beginPath();
            ctx.moveTo(player.x - camera.x, player.y - camera.y);
            ctx.arc(
                player.x - camera.x,
                player.y - camera.y,
                radius + 30,
                player.attackAngle - Math.PI / 4,
                player.attackAngle + Math.PI / 4
            );
            ctx.lineTo(player.x - camera.x, player.y - camera.y);
            ctx.fillStyle = 'rgba(136, 136, 136, 0.5)';
            ctx.fill();
        }
    });
}

/**
 * Dibuja un ataque del jugador principal.
 */
export function drawAttack(ctx, player, camera) {
    if (player.isAttacking) {
        ctx.beginPath();
        ctx.moveTo(player.x - camera.x, player.y - camera.y);
        ctx.arc(
            player.x - camera.x,
            player.y - camera.y,
            player.radius + 30,
            player.attackAngle - Math.PI / 4,
            player.attackAngle + Math.PI / 4
        );
        ctx.lineTo(player.x - camera.x, player.y - camera.y);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.fill();
    }
}