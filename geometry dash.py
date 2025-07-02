import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 400             
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Genius Vivaan") 
clock = pygame.time.Clock()

BLUE =  (0, 100, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TRIANGLE_COLOR = (0, 255, 0)

font = pygame.font.SysFont(None, 48)

# Player and obstacle bottom aligned at ground (HEIGHT)
player_height = 40
player = pygame.Rect(100, HEIGHT - player_height, 40, player_height)
obstacle = pygame.Rect(WIDTH, HEIGHT - 40, 40, 40)
obstacle_speed = 6

gravity = 0
jumping = False

game_state = "playing"

triangle_positions = [300, 500, 700]
triangle_width = 40
triangle_height = 40
triangle_speed = obstacle_speed

def draw_triangle(x):
    points = [
        (x, HEIGHT),  # base left on ground
        (x + triangle_width // 2, HEIGHT - triangle_height),  # peak top
        (x + triangle_width, HEIGHT)  # base right on ground
    ]
    pygame.draw.polygon(screen, TRIANGLE_COLOR, points)
    return points

def point_in_triangle(pt, v1, v2, v3):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0])*(p2[1] - p3[1]) - (p2[0] - p3[0])*(p1[1] - p3[1])
    b1 = sign(pt, v1, v2) < 0.0
    b2 = sign(pt, v2, v3) < 0.0
    b3 = sign(pt, v3, v1) < 0.0
    return ((b1 == b2) and (b2 == b3))

def rect_triangle_collision(rect, tri):
    corners = [
        (rect.left, rect.top),
        (rect.right, rect.top),
        (rect.left, rect.bottom),
        (rect.right, rect.bottom)
    ]
    for c in corners:
        if point_in_triangle(c, *tri):
            return True
    for v in tri:
        if rect.collidepoint(v):
            return True
    return False

def show_death_screen():
    screen.fill(BLACK)
    death_text = font.render("Game Over!", True, RED)
    retry_text = font.render("Press R to Retry or Q to Quit", True, RED)
    screen.blit(death_text, (WIDTH // 2 - death_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()

def reset_game():
    global player, obstacle, gravity, jumping, game_state, triangle_positions
    player.topleft = (100, HEIGHT - player_height)
    obstacle.x = WIDTH
    gravity = 0
    jumping = False
    game_state = "playing"
    triangle_positions = [300, 500, 700]

running = True
while running:
    clock.tick(60)

    if game_state == "playing":
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not jumping:
            gravity = -15
            jumping = True

        gravity += 1
        player.y += gravity

        # Keep player on ground
        if player.y >= HEIGHT - player_height:
            player.y = HEIGHT - player_height
            jumping = False

        # Move obstacle
        obstacle.x -= obstacle_speed
        if obstacle.x < -40:
            obstacle.x = WIDTH + 100

        # Move spikes
        for i in range(len(triangle_positions)):
            triangle_positions[i] -= triangle_speed
            if triangle_positions[i] < -triangle_width:
                triangle_positions[i] = WIDTH + 100

        # Collision with red square (allow landing on top)
        if player.colliderect(obstacle):
            if player.bottom <= obstacle.top + 10 and gravity >= 0:
                player.bottom = obstacle.top
                gravity = 0
                jumping = False
            else:
                game_state = "dead"

        # Collision with spikes
        for x in triangle_positions:
            tri_points = [
                (x, HEIGHT),  # base left
                (x + triangle_width // 2, HEIGHT - triangle_height),  # peak
                (x + triangle_width, HEIGHT)  # base right
            ]
            if rect_triangle_collision(player, tri_points):
                game_state = "dead"
                break

        pygame.draw.rect(screen, BLUE, player)
        pygame.draw.rect(screen, RED, obstacle)
        for x in triangle_positions:
            draw_triangle(x)

        pygame.display.flip()

    elif game_state == "dead":
        show_death_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                elif event.key == pygame.K_q:
                    running = False

pygame.quit()
sys.exit()
