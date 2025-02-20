import pygame

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
circle_speed = 2

target_x, target_y = 300, 180

moving_forward = True  # Direction control

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw target object (static image)
    screen.blit(target_image, (target_x, target_y))
    
    # Draw moving object (image)
    screen.blit(circle_image, (circle_x, circle_y))
    
    # Move the image towards the target
    if moving_forward:
        circle_x += circle_speed
        if circle_x + 40 >= target_x:
            moving_forward = False  # Change direction when touching
    else:
        circle_x -= circle_speed
        if circle_x <= 100:
            moving_forward = True  # Reset position after moving away
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()