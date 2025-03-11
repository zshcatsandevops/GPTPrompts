#include <stdio.h>

#define COINS_FOR_EXTRA_LIFE 100

// Structure to encapsulate the game state
typedef struct {
    int coins;
    int lives;
} GameState;

// Function to initialize the game state
void initGame(GameState *game) {
    game->coins = 0;
    game->lives = 3; // Starting with 3 lives
    printf("Game initialized. Coins: %d, Lives: %d\n", game->coins, game->lives);
}

// Function to add a coin and check for extra life rewards
void collectCoin(GameState *game) {
    game->coins++;
    printf("Coin collected! Total coins: %d\n", game->coins);

    // Award an extra life every 100 coins
    if (game->coins % COINS_FOR_EXTRA_LIFE == 0) {
        game->lives++;
        printf("Congratulations! You've earned an extra life. Total lives: %d\n", game->lives);
    }
}

// Function to display the current coins and lives
void displayGame(const GameState *game) {
    printf("Total coins collected: %d\n", game->coins);
    printf("Total lives: %d\n", game->lives);
}

// Function to reset only the coin counter
void resetCoins(GameState *game) {
    game->coins = 0;
    printf("Coin counter reset. You have collected %d coins.\n", game->coins);
}

int main() {
    GameState game;
    initGame(&game);

    // Simulate collecting 150 coins
    for (int i = 0; i < 150; i++) {
        collectCoin(&game);
    }
    displayGame(&game);

    // Reset coins (while lives persist) and display the updated state
    resetCoins(&game);
    displayGame(&game);

    return 0;
}
