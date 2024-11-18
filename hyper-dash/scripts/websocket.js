export function setupWebSocket(playerId, spawnPos, updatePlayers) {
    const ws = new WebSocket(WS_URL);

    ws.onopen = () => {
        console.log('Connected to server');
        ws.send(JSON.stringify({
            type: 'join',
            player: { id: playerId, x: spawnPos.x, y: spawnPos.y },
        }));
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        updatePlayers(data);
    };

    ws.onclose = () => {
        console.log('Disconnected from server');
    };

    return ws;
}
