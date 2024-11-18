export function getRandomSpawnPosition(mapWidth, mapHeight) {
    return {
        x: Math.random() * (mapWidth - 100) + 50,
        y: Math.random() * (mapHeight - 100) + 50,
    };
}
