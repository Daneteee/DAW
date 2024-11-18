import { GRID_SIZE, MAP_WIDTH, MAP_HEIGHT } from './constants.js';
import { initializeGameState, gameState } from './gameState.js';
import { updateCamera } from './camera.js';
import { setupWebSocket } from './websocket.js';
import { handlePlayerInput } from './input.js';
import { drawGrid, drawPlayers, drawPlayer, drawAttack } from './rendering.js';

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const dashCooldownFill = document.getElementById('dashCooldownFill');
const scoreElement = document.getElementById('score');
const playerCountElement = document.getElementById('playerCount');

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const playerId = Math.random().toString(36).substr(2, 9);
initializeGameState(playerId);

const ws = setupWebSocket(playerId, gameState.player, (data) => {
    // Actualizar el estado del juego con datos del servidor
    if (data.type === 'gameState') {
        gameState.otherPlayers = data.players.filter(p => p.id !== playerId);
        playerCountElement.textContent = `Players Online: ${data.players.length}`;
    } else if (data.type === 'playerUpdate') {
        const player = gameState.otherPlayers.find(p => p.id === data.player.id);
        if (player) {
            Object.assign(player, data.player);
        } else {
            gameState.otherPlayers.push(data.player);
        }
    }
});

let lastTime = 0;
function gameLoop(timestamp) {
    const deltaTime = timestamp - lastTime;
    lastTime = timestamp;

    // Limpiar el canvas
    ctx.fillStyle = '#1a1a1a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Actualizar cámara
    updateCamera(gameState.camera, gameState.player, canvas);

    // Dibujar la cuadrícula
    drawGrid(ctx, gameState.camera, GRID_SIZE, MAP_WIDTH, MAP_HEIGHT);

    // Manejar entrada del jugador
    handlePlayerInput(gameState.player, deltaTime);

    // Dibujar jugadores (otros y principal)
    drawPlayers(ctx, gameState.otherPlayers, gameState.camera, gameState.player.radius);
    drawPlayer(ctx, gameState.player, gameState.camera);

    // Dibujar ataques
    drawAttack(ctx, gameState.player, gameState.camera);

    // Actualizar barra de cooldown del dash
    if (gameState.player.dashCooldownTimer > 0) {
        gameState.player.dashCooldownTimer -= deltaTime;
    }
    const cooldownPercent = (gameState.player.dashCooldownTimer / gameState.player.dashCooldown) * 100;
    dashCooldownFill.style.width = `${100 - cooldownPercent}%`;

    // Actualizar elementos del HUD (puntuación)
    scoreElement.textContent = `Score: ${gameState.score}`;

    // Continuar el ciclo del juego
    requestAnimationFrame(gameLoop);
}
requestAnimationFrame(gameLoop);
