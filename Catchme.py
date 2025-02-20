import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Touch and Move Away")

# Define colors
WHITE = (255, 255, 255)

# Load images
circle_image = pygame.image.load("circle.png")  # Replace with your image file
circle_image = pygame.transform.scale(circle_image, (40, 40))

target_image = pygame.image.load("target.png")  # Replace with your image file
target_image = pygame.transform.scale(target_image, (40, 40))

# Object properties
circle_x, circle_y = 100, 200

target_x, target_y = 300, 180

def move_target():
    global target_x, target_y
    while True:
        new_x = random.randint(0, WIDTH - 40)
        new_y = random.randint(0, HEIGHT - 40)
        if abs(new_x - target_x) > 50 or abs(new_y - target_y) > 50:  # Ensure it moves away
            target_x, target_y = new_x, new_y
            break

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    circle_x = mouse_x - 20  # Center the image on the cursor
    circle_y = mouse_y - 20  # Allow full movement with cursor
    
    # Check for collision
    if (circle_x < target_x + 40 and circle_x + 40 > target_x and
        circle_y < target_y + 40 and circle_y + 40 > target_y):
        move_target()
    
    # Draw target object (moving image)
    screen.blit(target_image, (target_x, target_y))
    
    # Draw moving object (image)
    screen.blit(circle_image, (circle_x, circle_y))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
