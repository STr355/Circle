import pygame
import random

pygame.init()
windowWidth = 2560
windowHeight = 1380
BLACK = [0, 0, 0]
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window.fill(BLACK)
pygame.display.flip()
pygame.display.set_caption("Snake")
run = True


class Circle:
    def __init__(self, window, xPos, yPos, radius):
        self.window = window
        self.xPos = xPos
        self.yPos = yPos
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.radius = radius
        self.xDir = 0
        self.yDir = 0
        self.velocity = 0
        self.generateDirection()

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.xPos, self.yPos), self.radius)

    def generateNewColor(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.color = [red, green, blue]

    def increaseRadius(self):
        if self.radius < windowHeight / 8:
            self.radius += 5

    def reduceRadius(self):
        if self.radius > 20:
            self.radius -= 5

    def generateDirection(self):
        self.xDir = random.randint(-2, 2)
        self.yDir = random.randint(-2, 2)
        self.vel = self.xDir * self.yDir
        if self.xDir == 0 and self.yDir == 0:
            self.generateDirection()

    def move(self):
        self.xPos += self.xDir
        self.yPos += self.yDir
        if self.xPos - self.radius <= 0:
            self.bounceOffWall(0)
        if self.xPos + self.radius >= windowWidth:
            self.bounceOffWall(2)
        if self.yPos - self.radius <= 0:
            self.bounceOffWall(1)
        if self.yPos + self.radius >= windowHeight:
            self.bounceOffWall(3)

    def bounceOffWall(self, border):
        if border == 0:
            self.xDir = random.randint(1, 2)
            self.yDir = random.randint(-2, 2)
        elif border == 1:
            self.yDir = random.randint(1, 2)
            self.xDir = random.randint(-2, 2)
        elif border == 2:
            self.xDir = random.randint(-2, -1)
            self.yDir = random.randint(-2, 2)
        elif border == 3:
            self.yDir = random.randint(-2, -1)
            self.xDir = random.randint(-2, 2)
        self.generateNewColor()

    def bounceOffCircle(self):
        pass


circles = []
circle = Circle(window, windowWidth / 2, windowHeight / 2, random.randint(10, 50))
circles.append(circle)
while run:
    if random.randint(1, 1000) > 990:
        circles.append(
            Circle(window, random.randint(0, windowWidth), random.randint(0, windowHeight), random.randint(10, 150)))
        if len(circles) > 200:
            circles.pop()
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        circle.generateNewColor()
    elif keys[pygame.K_UP]:
        circle.increaseRadius()
    elif keys[pygame.K_DOWN]:
        circle.reduceRadius()
    elif keys[pygame.K_ESCAPE]:
        run = False
    window.fill(BLACK)
    for circle in circles:
        circle.draw()
        circle.move()
    pygame.display.update()

pygame.quit()
