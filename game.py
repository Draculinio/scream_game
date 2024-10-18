import pygame
import time

def transition(screen, duracion):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))  # Pantalla negra
    screen.blit(fade_surface, (0, 0))
    pygame.display.flip()
    time.sleep(duracion)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
hero_image = pygame.image.load('hero.png')
hero_rect = hero_image.get_rect(center=(player_pos.x,player_pos.y))
actual_room = 1
font = pygame.font.Font(None, 36)


#paredes
brick_image = pygame.image.load('brick.png')
room_1 = [
    brick_image.get_rect(topleft=(400, 300)),
    brick_image.get_rect(topleft=(400, 364)),
    brick_image.get_rect(topleft=(800, 300)),
    brick_image.get_rect(topleft=(800, 364)),

    brick_image.get_rect(topleft=(0, 64)),
    brick_image.get_rect(topleft=(64, 64)),
    brick_image.get_rect(topleft=(128, 64)),
    brick_image.get_rect(topleft=(192, 64)),
    brick_image.get_rect(topleft=(256, 64)),
    brick_image.get_rect(topleft=(320, 64)),
    brick_image.get_rect(topleft=(384, 64)),
    brick_image.get_rect(topleft=(448, 64)),
    brick_image.get_rect(topleft=(512, 64)),
    brick_image.get_rect(topleft=(576, 64)),
    brick_image.get_rect(topleft=(640, 64)),
    brick_image.get_rect(topleft=(704, 64)),
    brick_image.get_rect(topleft=(768, 64)),
    brick_image.get_rect(topleft=(832, 64)),
    brick_image.get_rect(topleft=(896, 64)),
    brick_image.get_rect(topleft=(960, 64)),
    brick_image.get_rect(topleft=(1024, 64)),
    brick_image.get_rect(topleft=(1088, 64)),
    brick_image.get_rect(topleft=(1152, 64)),
    brick_image.get_rect(topleft=(1216, 64)),
    brick_image.get_rect(topleft=(0, 656)),
    brick_image.get_rect(topleft=(64, 656)),
    brick_image.get_rect(topleft=(128, 656)),
    brick_image.get_rect(topleft=(192, 656)),
    brick_image.get_rect(topleft=(256, 656)),
    brick_image.get_rect(topleft=(320, 656)),
    brick_image.get_rect(topleft=(384, 656)),
    brick_image.get_rect(topleft=(448, 656)),
    brick_image.get_rect(topleft=(512, 656)),
    brick_image.get_rect(topleft=(576, 656)),
    brick_image.get_rect(topleft=(640, 656)),
    brick_image.get_rect(topleft=(704, 656)),
    brick_image.get_rect(topleft=(768, 656)),
    brick_image.get_rect(topleft=(832, 656)),
    brick_image.get_rect(topleft=(896, 656)),
    brick_image.get_rect(topleft=(960, 656)),
    brick_image.get_rect(topleft=(1024, 656)),
    brick_image.get_rect(topleft=(1088, 656)),
    brick_image.get_rect(topleft=(1152, 656)),
    brick_image.get_rect(topleft=(1216, 656)),

    brick_image.get_rect(topleft=(0, 128)),
    brick_image.get_rect(topleft=(0, 192)),
    brick_image.get_rect(topleft=(0, 256)),
    brick_image.get_rect(topleft=(0, 320)),
    brick_image.get_rect(topleft=(0, 384)),
    brick_image.get_rect(topleft=(0, 448)),
    brick_image.get_rect(topleft=(0, 512)),

    brick_image.get_rect(topleft=(1216, 128)),
    brick_image.get_rect(topleft=(1216, 192)),
    brick_image.get_rect(topleft=(1216, 256)),
    #brick_image.get_rect(topleft=(1216, 320)),
    #brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]

room_2 = [
    brick_image.get_rect(topleft=(200, 300)),
    brick_image.get_rect(topleft=(200, 364)),
    brick_image.get_rect(topleft=(500, 300)),
    brick_image.get_rect(topleft=(500, 364)),

    brick_image.get_rect(topleft=(0, 64)),
    brick_image.get_rect(topleft=(64, 64)),
    brick_image.get_rect(topleft=(128, 64)),
    brick_image.get_rect(topleft=(192, 64)),
    brick_image.get_rect(topleft=(256, 64)),
    brick_image.get_rect(topleft=(320, 64)),
    brick_image.get_rect(topleft=(384, 64)),
    brick_image.get_rect(topleft=(448, 64)),
    brick_image.get_rect(topleft=(512, 64)),
    brick_image.get_rect(topleft=(576, 64)),
    brick_image.get_rect(topleft=(640, 64)),
    brick_image.get_rect(topleft=(704, 64)),
    brick_image.get_rect(topleft=(768, 64)),
    brick_image.get_rect(topleft=(832, 64)),
    brick_image.get_rect(topleft=(896, 64)),
    brick_image.get_rect(topleft=(960, 64)),
    brick_image.get_rect(topleft=(1024, 64)),
    brick_image.get_rect(topleft=(1088, 64)),
    brick_image.get_rect(topleft=(1152, 64)),
    brick_image.get_rect(topleft=(1216, 64)),
    brick_image.get_rect(topleft=(0, 656)),
    brick_image.get_rect(topleft=(64, 656)),
    brick_image.get_rect(topleft=(128, 656)),
    brick_image.get_rect(topleft=(192, 656)),
    brick_image.get_rect(topleft=(256, 656)),
    brick_image.get_rect(topleft=(320, 656)),
    brick_image.get_rect(topleft=(384, 656)),
    brick_image.get_rect(topleft=(448, 656)),
    brick_image.get_rect(topleft=(512, 656)),
    brick_image.get_rect(topleft=(576, 656)),
    brick_image.get_rect(topleft=(640, 656)),
    brick_image.get_rect(topleft=(704, 656)),
    brick_image.get_rect(topleft=(768, 656)),
    brick_image.get_rect(topleft=(832, 656)),
    brick_image.get_rect(topleft=(896, 656)),
    brick_image.get_rect(topleft=(960, 656)),
    brick_image.get_rect(topleft=(1024, 656)),
    brick_image.get_rect(topleft=(1088, 656)),
    brick_image.get_rect(topleft=(1152, 656)),
    brick_image.get_rect(topleft=(1216, 656)),

    brick_image.get_rect(topleft=(0, 128)),
    brick_image.get_rect(topleft=(0, 192)),
    brick_image.get_rect(topleft=(0, 256)),
    brick_image.get_rect(topleft=(0, 320)),
    brick_image.get_rect(topleft=(0, 384)),
    brick_image.get_rect(topleft=(0, 448)),
    brick_image.get_rect(topleft=(0, 512)),

    brick_image.get_rect(topleft=(1216, 128)),
    brick_image.get_rect(topleft=(1216, 192)),
    brick_image.get_rect(topleft=(1216, 256)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]
rooms = {
    1: room_1,
    2: room_2
}

portals = {
    1: {'position':pygame.Rect(1216,320,64,128), 'destination': 2},
    2: {'position':pygame.Rect(0,576,64,128), 'destination': 1},
}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    hcr = hero_rect.copy()
    if keys[pygame.K_w]:
        hcr.y -= 300 * dt
        if not any(hcr.colliderect(brick_rect) for brick_rect in rooms[actual_room]):
            player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        hcr.y += 300 * dt
        if not any(hcr.colliderect(brick_rect) for brick_rect in rooms[actual_room]):
            player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        hcr.x -= 300 * dt
        if not any(hcr.colliderect(brick_rect) for brick_rect in rooms[actual_room]):
            player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        hcr.x += 300 * dt
        if not any(hcr.colliderect(brick_rect) for brick_rect in rooms[actual_room]):
            player_pos.x += 300 * dt

    #verify room change
    if hero_rect.colliderect(portals[actual_room]['position']):
        transition(screen, 1)
        actual_room = portals[actual_room]['destination']
        if actual_room == 1:
            player_pos.x = 1140
            player_pos.y = 320
        if actual_room == 2:
            player_pos.x = 65
            player_pos.y = 576
        hero_rect.topleft = (int(player_pos.x), int(player_pos.y))
    hero_rect.topleft = (int(player_pos.x),int(player_pos.y))

    screen.fill("black")
    text_surface = font.render(f"Room: {actual_room}", True, (255,255,255))
    screen.blit(text_surface, (10,10))
    screen.blit(hero_image, hero_rect.topleft)
    for brick_rect in rooms[actual_room]:
        screen.blit(brick_image, brick_rect)

    pygame.display.flip()
    dt = clock.tick(60) /1000 

pygame.quit()