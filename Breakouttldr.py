# Let's create a new build of the Breakout game based on the provided specifications.
# I will modify the game code to integrate features from the uploaded image,
# including an updated layout, color pattern, and an initial start prompt.

import pygame
import sys
import random
import numpy as np

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)  # Mixer settings for sound

# ----------------------------- Constants --------------------------------- #

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BRICK_COLORS = [RED, BLACK, GREEN, BLUE]

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_COLOR = WHITE
PADDLE_SPEED = 7

# Ball properties
BALL_RADIUS = 10
BALL_COLOR = RED
BALL_SPEED = 5

# Brick properties
BRICK_ROWS = 4
BRICK_COLUMNS = 8
BRICK_WIDTH = (SCREEN_WIDTH - (BRICK_COLUMNS + 1) * 10) / BRICK_COLUMNS
BRICK_HEIGHT = 30
BRICK_PADDING = 10
BRICK_OFFSET_TOP = 50

# Font
FONT_NAME = pygame.font.match_font('arial')

# ----------------------------- Sound Generation -------------------------- #

def generate_tone(frequency, duration, volume=0.5):
    """Generate a tone at the given frequency (Hz), duration (seconds), and volume (0-1)."""
    sample_rate = 22050  # Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * frequency * t)
    audio = (wave * 32767).astype(np.int16)  # Convert to 16-bit PCM
    stereo_sound = np.repeat(audio[:, np.newaxis], 2, axis=1)  # Duplicate for stereo
    return pygame.sndarray.make_sound(stereo_sound)

# Generate sound effects
paddle_hit_sound = generate_tone(440, 0.1)    # 440 Hz for paddle hit
brick_hit_sound = generate_tone(880, 0.1)     # 880 Hz for brick hit
game_over_sound = generate_tone(220, 0.5)     # 220 Hz for game over
win_sound = generate_tone(660, 0.5)           # 660 Hz for victory

# ----------------------------- Classes ----------------------------------- #

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed = PADDLE_SPEED

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep paddle within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        diameter = BALL_RADIUS * 2
        self.image = pygame.Surface([diameter, diameter], pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS - 10
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = -BALL_SPEED

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off left and right walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1

        # Bounce off top
        if self.rect.top <= 0:
            self.speed_y *= -1

    def bounce(self, diff):
        """Bounce the ball, changing its angle based on the difference."""
        self.speed_y *= -1
        self.speed_x += diff * 2  # Adjust multiplier as needed for effect

        # Limit the speed_x to prevent it from getting too fast
        max_speed = BALL_SPEED * 2
        if self.speed_x > max_speed:
            self.speed_x = max_speed
        elif self.speed_x < -max_speed:
            self.speed_x = -max_speed

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([BRICK_WIDTH, BRICK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# ----------------------------- Helper Functions --------------------------- #

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def create_bricks():
    bricks = pygame.sprite.Group()
    for row in range(BRICK_ROWS):
        for column in range(BRICK_COLUMNS):
            x = 10 + column * (BRICK_WIDTH + BRICK_PADDING)
            y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            brick = Brick(x, y, color)
            bricks.add(brick)
    return bricks

# ----------------------------- Main Game Function ------------------------ #

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout Game")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    bricks = create_bricks()
    all_sprites.add(bricks)

    paddle = Paddle()
    all_sprites.add(paddle)

    ball = Ball()
    all_sprites.add(ball)

    # Game variables
    score = 0
    lives = 3
    running = True
    game_over = False
    victory = False
    game_started = False

    while running:
        clock.tick(60)  # 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_started = True

        if not game_started:
            # Draw the start screen
            screen.fill(BLACK)
            draw_text(screen, "Press space to start!", 36, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, WHITE)
            pygame.display.flip()
            continue

        if not game_over and not victory:
            keys_pressed = pygame.key.get_pressed()
            paddle.update(keys_pressed)
            ball.update()

            # Collision between ball and paddle
            if pygame.sprite.collide_rect(ball, paddle):
                paddle_hit_sound.play()

                # Calculate the difference between ball center and paddle center
                diff = (ball.rect.centerx - paddle.rect.centerx) / (paddle.width / 2)
                ball.bounce(diff)

                # Adjust ball position to prevent sticking
                ball.rect.bottom = paddle.rect.top - 1

            # Collision between ball and bricks
            collided_bricks = pygame.sprite.spritecollide(ball, bricks, True)
            if collided_bricks:
                brick_hit_sound.play()
                ball.speed_y *= -1
                score += len(collided_bricks)

            # Check for victory
            if not bricks:
                win_sound.play()
                victory = True

            # Check if ball falls below the paddle
            if ball.rect.top > SCREEN_HEIGHT:
                lives -= 1
                if lives > 0:
                    # Reset ball and paddle positions
                    ball.reset_position()
                    paddle.rect.centerx = SCREEN_WIDTH / 2
                else:
                    game_over_sound.play()
                    game_over = True

        # Drawing
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Draw score and lives
        draw_text(screen, f"Score: {score}", 18, SCREEN_WIDTH / 2, 10)
        draw_text(screen, f"Lives: {lives}", 18, SCREEN_WIDTH - 60, 10)

        # Draw game over or victory message
        if game_over:
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 32, (255, 0, 0))
            draw_text(screen, "Press ESC to exit", 24, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 32, WHITE)
        elif victory:
            draw_text(screen, "YOU WIN!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 32, (0, 255, 0))
            draw_text(screen, "Press ESC to exit", 24, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 32, WHITE)

        pygame.display.flip()

        # Exit the game if ESC is pressed
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
