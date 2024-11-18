export function createPlayer(id, x, y) {
    return {
        id,
        x,
        y,
        radius: 20,
        speed: 2.5,
        dashSpeed: 15,
        isDashing: false,
        dashCooldown: 2000,
        dashCooldownTimer: 0,
        kills: 0,
        attackAngle: 0,
        isAttacking: false,
        attackCooldown: 750,
        attackCooldownTimer: 0,
    };
}
