import { createPlayer } from './player.js';
import { getRandomSpawnPosition } from './utilities.js';

export const gameState = {
    player: null,
    score: 0,
    otherPlayers: [],
};

export function initializeGameState(playerId) {
    const spawnPos = getRandomSpawnPosition(MAP_WIDTH, MAP_HEIGHT);
    gameState.player = createPlayer(playerId, spawnPos.x, spawnPos.y);
}
