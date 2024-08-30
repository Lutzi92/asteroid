import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        for item in updatable:
            item.update(dt)
        for obj in asteroids:
            if obj.collide(player):
                print("Game over!")
                return
        for obj in asteroids:
            for shot in shots:
                if obj.collide(shot):
                    shot.kill()
                    obj.split()
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()