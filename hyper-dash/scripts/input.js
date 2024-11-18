export function handlePlayerInput(player, deltaTime) {
    const keys = {};
    window.addEventListener('keydown', (e) => {
        keys[e.key] = true;
    });
    window.addEventListener('keyup', (e) => {
        keys[e.key] = false;
    });

    let dx = 0;
    let dy = 0;

    if (keys['w']) dy -= player.speed;
    if (keys['s']) dy += player.speed;
    if (keys['a']) dx -= player.speed;
    if (keys['d']) dx += player.speed;

    if (dx !== 0 && dy !== 0) {
        dx *= Math.SQRT1_2;
        dy *= Math.SQRT1_2;
    }

    player.x += dx * deltaTime;
    player.y += dy * deltaTime;
}
