import pygame
import time

def transition(screen, duracion):
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill((0, 0, 0))  # Pantalla negra
    screen.blit(fade_surface, (0, 0))
    pygame.display.flip()
    time.sleep(duracion)

def game_over():
    game_over_running = True
    while game_over_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return
        screen.fill("black")
        screen.blit(font.render("GAME OVER (R-restart/Q-quit)", True, (255,255,255)), (screen.get_width() // 2 - 200, screen.get_height() //2))
        pygame.display.flip()

def restart_game():
    global player_pos, hero_rect, actual_room
    player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
    hero_rect.topleft = (int(player_pos.x), int(player_pos.y))
    actual_room = 1


class Alien:
    def __init__(self,x,y):
        self.rect = red_alien_image.get_rect(topleft=(x,y))
        self.direction = 1
    def move(self, dt, room):
        self.rect.x += self.direction * 100 * dt
        for brick_rect in room:
            if self.rect.colliderect(brick_rect):
                self.rect.x -= self.direction * 100 * dt
                self.direction *= -1
                break

class Yellow_Alien:
    def __init__(self,x,y):
        self.rect = yellow_alien_image.get_rect(topleft=(x,y))
        self.direction = 1
    def move(self, dt, room):
        self.rect.y += self.direction * 100 * dt
        for brick_rect in room:
            if self.rect.colliderect(brick_rect):
                self.rect.y -= self.direction * 100 * dt  # Wall? RETREAT!
                self.direction *= -1
                break

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
items = 0
player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
hero_image = pygame.image.load('hero.png')
hero_rect = hero_image.get_rect(center=(player_pos.x,player_pos.y))
actual_room = 1
font = pygame.font.Font(None, 36)

#malosos
red_alien_image = pygame.image.load('red_alien.png')
yellow_alien_image = pygame.image.load('yellow_alien.png')

aliens_2 = [
    Alien(300,192), Yellow_Alien(200, 256)
]
aliens_1 = []
aliens_3 =[Alien(600,320), Yellow_Alien(300, 256),Alien(300,512), Yellow_Alien(500, 256),Yellow_Alien(900, 256)]

#pieces
part_one = pygame.image.load('ship_part_1.png')
pieces_3 =  [part_one.get_rect(topleft=(128,128))]
pieces_1 = [part_one.get_rect(topleft=(128,128))]
pieces_2 = []

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

room_3 = [
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
    #brick_image.get_rect(topleft=(512, 656)),
    #brick_image.get_rect(topleft=(576, 656)),
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
    brick_image.get_rect(topleft=(0, 576)),
    brick_image.get_rect(topleft=(0, 640)),

    brick_image.get_rect(topleft=(1216, 128)),
    brick_image.get_rect(topleft=(1216, 192)),
    brick_image.get_rect(topleft=(1216, 256)),
    brick_image.get_rect(topleft=(1216, 320)),
    brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
]


rooms = {
    1: room_1,
    2: room_2,
    3: room_3,
}

aliens = {
    1: aliens_1,
    2: aliens_2,
    3: aliens_3
}

pieces = {
    1: pieces_1,
    2: pieces_2,
    3: pieces_3
}

portals = {
    1: [{'position':pygame.Rect(1216,320,64,128), 'destination': 2, 'spawn_pos': (65,576)},
        {'position':pygame.Rect(0,576,64,128), 'destination': 3, 'spawn_pos': (1140,576)}],
    2: [{'position':pygame.Rect(0,576,64,128), 'destination': 1,'spawn_pos': (1140,320)}],
    3: [{'position': pygame.Rect(1216,576,64,128), 'destination': 1,'spawn_pos': (65,576)}]
}

#initialize aliens

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
    for portal in portals[actual_room]:
        if hero_rect.colliderect(portal['position']):
            transition(screen, 0.5)
            actual_room = portal['destination']
            player_pos.x, player_pos.y = portal['spawn_pos']
            hero_rect.topleft = (int(player_pos.x), int(player_pos.y))
    hero_rect.topleft = (int(player_pos.x),int(player_pos.y))

    #alien movement
    for alien in aliens[actual_room]:
        alien.move(dt, rooms[actual_room])

    screen.fill("black")
    #print information
    text_surface = font.render(f"Room: {actual_room}        Pieces found: {items}/10", True, (255,255,255))
    screen.blit(text_surface, (10,10))
    screen.blit(hero_image, hero_rect.topleft)
    if actual_room != 1:
        for alien in aliens[actual_room]:
            if isinstance(alien, Alien):
                screen.blit(red_alien_image,alien.rect.topleft)
            else:
                screen.blit(yellow_alien_image,alien.rect.topleft)
    for brick_rect in rooms[actual_room]:
        screen.blit(brick_image, brick_rect)
    
    #draw objects
    picked_up_pieces = []
    for piece in pieces[actual_room]:
        if hero_rect.colliderect(piece):
            picked_up_pieces.append(piece)
            items +=1
    for picked_up_piece in picked_up_pieces:
        pieces[actual_room].remove(picked_up_piece)
    for piece in pieces[actual_room]:
        screen.blit(part_one, piece)
    
    #aliens collition
    for alien in aliens[actual_room]:
        if hero_rect.colliderect(alien.rect):
            game_over()
            restart_game()

    pygame.display.flip()
    dt = clock.tick(60) /1000 

pygame.quit()