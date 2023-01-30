import pygame

class Snake:

    def __init__(self, color, x, y, size, speed):
        self.SIZE = size
        self.COLOR = color
        self.SPEED = speed
        self.X = x
        self.Y = y
        self.DISPLAY = pygame.display.set_mode((self.X, self.Y))

    cord_x,cord_y = (100, 350)
    list_value = [False, False, False, False]

    def set_value(self, number):
        for num in range(0, len(self.list_value) - 1): self.list_value[num] = False
        self.list_value[number] = True

    def update(self):
        snake_surface = pygame.Surface((self.SIZE, self.SIZE))
        snake_cords = snake_surface.get_rect(center=(self.cord_x, self.cord_y))

        if self.list_value[0]:
            self.cord_x -= self.SPEED
        elif self.list_value[1]:
            self.cord_y -= self.SPEED
        elif self.list_value[2]:
            self.cord_y += self.SPEED
        elif self.list_value[3]:
            self.cord_x += self.SPEED

        self.DISPLAY.fill('black')

        snake_surface.fill('green')
        self.DISPLAY.blit(snake_surface, snake_cords)

snake = Snake((0, 0, 200), 700, 700, 50, 20)
time = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.set_value(1)
            elif event.key == pygame.K_DOWN:
                snake.set_value(2)
            elif event.key == pygame.K_LEFT:
                snake.set_value(0)
            elif event.key == pygame.K_RIGHT:
                snake.set_value(3)

    snake.update()

    time.tick(60)
    pygame.display.update()

pygame.quit()