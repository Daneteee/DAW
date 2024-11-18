export function updateCamera(camera, player, canvas) {
    const targetX = player.x - canvas.width / 2;
    const targetY = player.y - canvas.height / 2;

    camera.x += (targetX - camera.x) * 0.1;
    camera.y += (targetY - camera.y) * 0.1;

    camera.x = Math.max(0, Math.min(MAP_WIDTH - canvas.width, camera.x));
    camera.y = Math.max(0, Math.min(MAP_HEIGHT - canvas.height, camera.y));
}
