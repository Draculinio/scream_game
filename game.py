import pygame
import time
import copy

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
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return "quit"
        screen.fill("black")
        screen.blit(font.render("GAME OVER (R-restart/Q-quit)", True, (255,255,255)), (screen.get_width() // 2 - 200, screen.get_height() //2))
        pygame.display.flip()

def restart_game(initial_pieces):
    player_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
    pieces = copy.deepcopy(initial_pieces)
    items = 0
    actual_room = 1
    return player_pos, actual_room, pieces, items

def check_win_condition(player_rect, ship_rect, collected_pieces, total_pieces):
    if collected_pieces == total_pieces:  # Si se han recogido todas las piezas
        if player_rect.colliderect(ship_rect):  # Si colisiona con la nave
            return True  # El jugador gana
    return False


def show_victory_screen():
    screen.fill("black")
    victory_message = font.render("Robert Python repaired his ship, now he can return to our planet", True, (255, 255, 255))
    screen.blit(victory_message, (screen.get_width() // 2 - 100, screen.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  

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

class Worm:
    def __init__(self, x, y):
        self.rect = worm_alien_image.get_rect(topleft=(x, y))
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Arriba, derecha, abajo, izquierda
        self.current_direction = 0
        self.move_speed = 100  # Velocidad de movimiento
        self.direction_change_timer = 0  # Temporizador para cambiar dirección
        self.direction_change_interval = 1  # Cambiar dirección cada segundo

    def move(self, dt, room):
        # Mover en la dirección actual
        self.rect.x += self.directions[self.current_direction][0] * self.move_speed * dt
        self.rect.y += self.directions[self.current_direction][1] * self.move_speed * dt

        # Actualizar el temporizador
        self.direction_change_timer += dt
        if self.direction_change_timer >= self.direction_change_interval:
            self.direction_change_timer = 0  # Reiniciar temporizador
            self.current_direction = (self.current_direction + 1) % 4  # Cambiar dirección


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.Font(None, 36)

#malosos
red_alien_image = pygame.image.load('red_alien.png')
yellow_alien_image = pygame.image.load('yellow_alien.png')
worm_alien_image = pygame.image.load('worm.png')

aliens_2 = [Alien(256,512), Yellow_Alien(256, 384), Alien(960,128),Yellow_Alien(640, 576)]
aliens_1 = []
aliens_3 =[Alien(600,320), Yellow_Alien(300, 256),Alien(300,512), Yellow_Alien(500, 256),Yellow_Alien(900, 256)]
aliens_4 =[Alien(600,320), Yellow_Alien(256, 324),Alien(300,512), Yellow_Alien(448, 512),Yellow_Alien(900, 256), Worm(192,256)]
aliens_5 =[Alien(600,320), Alien(600,512), Yellow_Alien(300, 256),Alien(300,512), Yellow_Alien(500, 256),Yellow_Alien(900, 256)]
aliens_6 =[Alien(600,192), Yellow_Alien(300, 256),Alien(300,512), Yellow_Alien(500, 256),Yellow_Alien(832, 256),Worm(704,512),Alien(960,320)]
aliens_7 =[Yellow_Alien(300, 256),Yellow_Alien(768,320), Yellow_Alien(500, 256),Yellow_Alien(896, 256),Yellow_Alien(704,768),Yellow_Alien(960, 512),Alien(128,512)]
aliens_8 = [Worm(320,512),Worm(320,384),Worm(768,512),Worm(768,384),Worm(832,320),Worm(256,320)]
aliens_9 = [Yellow_Alien(384, 512),Yellow_Alien(320, 448),Alien(128,448)]
aliens_10 = [Yellow_Alien(320, 448),Alien(128,256),Alien(896,448),Yellow_Alien(576, 196)]
aliens_11 = [Yellow_Alien(320, 448),Alien(128,256),Alien(896,448),Alien(768, 576),Yellow_Alien(256, 448)]
#pieces
part_one = pygame.image.load('ship_part_1.png')
pieces_3 = [part_one.get_rect(topleft=(128,128))]
pieces_1 = []
pieces_2 = [part_one.get_rect(topleft=(512,256))]
pieces_4 = [part_one.get_rect(topleft=(576,576))]
pieces_5 = [part_one.get_rect(topleft=(128,128)),part_one.get_rect(topleft=(576,448))]
pieces_6 = [part_one.get_rect(topleft=(1152,128))]
pieces_7 = [part_one.get_rect(topleft=(256,576))]
pieces_8 = [part_one.get_rect(topleft=(640,320))]
pieces_9 = [part_one.get_rect(topleft=(1152,576))]
pieces_10 = [part_one.get_rect(topleft=(576,384))]
pieces_11 = [part_one.get_rect(topleft=(128,128))]

#walls
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
    brick_image.get_rect(topleft=(256, 192)),
    brick_image.get_rect(topleft=(256, 256)),
    brick_image.get_rect(topleft=(320, 192)),
    brick_image.get_rect(topleft=(320, 256)),
    brick_image.get_rect(topleft=(384, 320)),
    brick_image.get_rect(topleft=(448, 384)),
    brick_image.get_rect(topleft=(576, 384)),
    brick_image.get_rect(topleft=(640, 320)),
    brick_image.get_rect(topleft=(704, 192)),
    brick_image.get_rect(topleft=(704, 256)),
    brick_image.get_rect(topleft=(768, 192)),
    brick_image.get_rect(topleft=(768, 256)),

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
    brick_image.get_rect(topleft=(1152,512)),
    brick_image.get_rect(topleft=(64,512)),
    brick_image.get_rect(topleft=(128,512)),
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

room_4 = [
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
    #brick_image.get_rect(topleft=(512, 64)),
    #brick_image.get_rect(topleft=(576, 64)),
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
room_5 = [
    brick_image.get_rect(topleft=(384, 320)),
    brick_image.get_rect(topleft=(384, 384)),
    brick_image.get_rect(topleft=(384, 448)),
    brick_image.get_rect(topleft=(384, 512)),
    brick_image.get_rect(topleft=(852, 320)),
    brick_image.get_rect(topleft=(852, 384)),
    brick_image.get_rect(topleft=(852, 448)),
    brick_image.get_rect(topleft=(852, 512)),

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
    brick_image.get_rect(topleft=(0, 576)),
    brick_image.get_rect(topleft=(0, 640)),
    brick_image.get_rect(topleft=(1216, 128)),
    brick_image.get_rect(topleft=(1216, 192)),
    brick_image.get_rect(topleft=(1216, 256)),
    brick_image.get_rect(topleft=(1216, 320)),
    brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    #brick_image.get_rect(topleft=(1216, 576)),
    #brick_image.get_rect(topleft=(1216, 640)),
]

room_6 = [
    brick_image.get_rect(topleft=(960, 128)),
    brick_image.get_rect(topleft=(960, 192)),
    brick_image.get_rect(topleft=(960, 256)),
    brick_image.get_rect(topleft=(1024, 256)),
    brick_image.get_rect(topleft=(800, 320)),
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
    #brick_image.get_rect(topleft=(704, 656)),
    #brick_image.get_rect(topleft=(768, 656)),
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
    #brick_image.get_rect(topleft=(0, 320)),
    #brick_image.get_rect(topleft=(0, 384)),
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
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]
room_7 = [
    brick_image.get_rect(topleft=(384, 128)),
    brick_image.get_rect(topleft=(384, 192)),
    #brick_image.get_rect(topleft=(384, 320)),
    brick_image.get_rect(topleft=(384, 384)),
    brick_image.get_rect(topleft=(384, 448)),
    brick_image.get_rect(topleft=(384, 512)),
    brick_image.get_rect(topleft=(384, 576)),
    brick_image.get_rect(topleft=(384, 640)),
    brick_image.get_rect(topleft=(384, 128)),
    brick_image.get_rect(topleft=(640, 128)),
    brick_image.get_rect(topleft=(640, 192)),
    brick_image.get_rect(topleft=(640, 256)),
    brick_image.get_rect(topleft=(640, 320)),
    brick_image.get_rect(topleft=(640, 384)),
    #brick_image.get_rect(topleft=(640, 512)),
    brick_image.get_rect(topleft=(640, 576)),
    brick_image.get_rect(topleft=(640, 640)),

    brick_image.get_rect(topleft=(832, 128)),
    brick_image.get_rect(topleft=(832, 192)),
    #brick_image.get_rect(topleft=(832, 256)),
    #brick_image.get_rect(topleft=(832, 320)),
    brick_image.get_rect(topleft=(832, 384)),
    brick_image.get_rect(topleft=(832, 512)),
    brick_image.get_rect(topleft=(832, 448)),
    brick_image.get_rect(topleft=(832, 576)),
    brick_image.get_rect(topleft=(832, 640)),

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
    #brick_image.get_rect(topleft=(0, 320)),
    #brick_image.get_rect(topleft=(0, 384)),
    brick_image.get_rect(topleft=(0, 448)),
    brick_image.get_rect(topleft=(0, 512)),
    brick_image.get_rect(topleft=(0, 576)),

    brick_image.get_rect(topleft=(1216, 128)),
    #brick_image.get_rect(topleft=(1216, 192)),
    #brick_image.get_rect(topleft=(1216, 256)),
    brick_image.get_rect(topleft=(1216, 320)),
    brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]

room_8 = [
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
    #brick_image.get_rect(topleft=(832, 656)),
    #brick_image.get_rect(topleft=(896, 656)),
    brick_image.get_rect(topleft=(960, 656)),
    brick_image.get_rect(topleft=(1024, 656)),
    brick_image.get_rect(topleft=(1088, 656)),
    brick_image.get_rect(topleft=(1152, 656)),
    brick_image.get_rect(topleft=(1216, 656)),

    brick_image.get_rect(topleft=(0, 128)),
    #brick_image.get_rect(topleft=(0, 192)),
    #brick_image.get_rect(topleft=(0, 256)),
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
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]

room_9 = [
    brick_image.get_rect(topleft=(768, 128)),
    brick_image.get_rect(topleft=(960, 128)),
    brick_image.get_rect(topleft=(768, 192)),
    brick_image.get_rect(topleft=(960, 192)),
    brick_image.get_rect(topleft=(768, 256)),
    brick_image.get_rect(topleft=(960, 256)),
    brick_image.get_rect(topleft=(1024, 256)),
    brick_image.get_rect(topleft=(1088, 256)),
    brick_image.get_rect(topleft=(1152, 256)),
    brick_image.get_rect(topleft=(1152, 448)),
    brick_image.get_rect(topleft=(1088, 448)),
    brick_image.get_rect(topleft=(1024, 448)),
    brick_image.get_rect(topleft=(960, 448)),
    brick_image.get_rect(topleft=(896, 448)),
    brick_image.get_rect(topleft=(832, 448)),
    brick_image.get_rect(topleft=(768, 448)),
    brick_image.get_rect(topleft=(704, 448)),
    brick_image.get_rect(topleft=(640, 448)),
    brick_image.get_rect(topleft=(576, 448)),
    brick_image.get_rect(topleft=(512, 448)),
    brick_image.get_rect(topleft=(512, 384)),
    brick_image.get_rect(topleft=(448, 384)),
    brick_image.get_rect(topleft=(384, 384)),
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
    #brick_image.get_rect(topleft=(832, 64)),
    #brick_image.get_rect(topleft=(896, 64)),
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
    brick_image.get_rect(topleft=(0, 576)),
    brick_image.get_rect(topleft=(0, 640)),

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

room_10 = [
    brick_image.get_rect(topleft=(448, 320)),
    brick_image.get_rect(topleft=(832, 320)),
    brick_image.get_rect(topleft=(448, 384)),
    brick_image.get_rect(topleft=(832, 384)),
    brick_image.get_rect(topleft=(512, 448)),
    brick_image.get_rect(topleft=(768, 448)),
    brick_image.get_rect(topleft=(512, 256)),
    brick_image.get_rect(topleft=(768, 256)),
    brick_image.get_rect(topleft=(0, 64)),
    brick_image.get_rect(topleft=(64, 64)),
    brick_image.get_rect(topleft=(128, 64)),
    brick_image.get_rect(topleft=(192, 64)),
    brick_image.get_rect(topleft=(256, 64)),
    brick_image.get_rect(topleft=(320, 64)),
    brick_image.get_rect(topleft=(384, 64)),
    #brick_image.get_rect(topleft=(448, 64)),
    #brick_image.get_rect(topleft=(512, 64)),
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
    #brick_image.get_rect(topleft=(0, 320)),
    #brick_image.get_rect(topleft=(0, 384)),
    brick_image.get_rect(topleft=(0, 448)),
    brick_image.get_rect(topleft=(0, 512)),
    brick_image.get_rect(topleft=(0, 576)),

    brick_image.get_rect(topleft=(1216, 128)),
    brick_image.get_rect(topleft=(1216, 192)),
    brick_image.get_rect(topleft=(1216, 256)),
    brick_image.get_rect(topleft=(1216, 320)),
    brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]

room_11 = [
    brick_image.get_rect(topleft=(320, 192)),
    brick_image.get_rect(topleft=(320, 320)),
    brick_image.get_rect(topleft=(320, 448)),
    brick_image.get_rect(topleft=(320, 576)),
    brick_image.get_rect(topleft=(640, 128)),
    brick_image.get_rect(topleft=(640, 256)),
    brick_image.get_rect(topleft=(640, 384)),
    brick_image.get_rect(topleft=(640, 512)),
    brick_image.get_rect(topleft=(960, 192)),
    brick_image.get_rect(topleft=(960, 320)),
    brick_image.get_rect(topleft=(960, 448)),
    brick_image.get_rect(topleft=(960, 576)),
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
    #brick_image.get_rect(topleft=(704, 64)),
    #brick_image.get_rect(topleft=(768, 64)),
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
    #brick_image.get_rect(topleft=(448, 656)),
    #brick_image.get_rect(topleft=(512, 656)),
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
    brick_image.get_rect(topleft=(1216, 320)),
    brick_image.get_rect(topleft=(1216, 384)),
    brick_image.get_rect(topleft=(1216, 448)),
    brick_image.get_rect(topleft=(1216, 512)),
    brick_image.get_rect(topleft=(1216, 576)),
    brick_image.get_rect(topleft=(1216, 640)),
]

rooms = {
    1: room_1,
    2: room_2,
    3: room_3,
    4: room_4,
    5: room_5,
    6: room_6,
    7: room_7,
    8: room_8,
    9: room_9,
    10: room_10,
    11: room_11
}

aliens = {
    1: aliens_1,
    2: aliens_2,
    3: aliens_3,
    4: aliens_4,
    5: aliens_5,
    6: aliens_6,
    7: aliens_7,
    8: aliens_8,
    9: aliens_9,
    10: aliens_10,
    11: aliens_11
}

pieces = {
    1: pieces_1,
    2: pieces_2,
    3: pieces_3,
    4: pieces_4,
    5: pieces_5,
    6: pieces_6,
    7: pieces_7,
    8: pieces_8,
    9: pieces_9,
    10: pieces_10,
    11: pieces_11
}

initial_pieces = copy.deepcopy(pieces)
player_pos, actual_room, pieces, items = restart_game(initial_pieces)
portals = {
    1: [{'position':pygame.Rect(1216,320,64,128), 'destination': 2, 'spawn_pos': (65,576)},
        {'position':pygame.Rect(0,576,64,128), 'destination': 3, 'spawn_pos': (1140,576)}],
    2: [{'position':pygame.Rect(0,576,64,128), 'destination': 1,'spawn_pos': (1140,320)},
        {'position': pygame.Rect(1216,320,64,128), 'destination': 6,'spawn_pos': (65,321)}],
    3: [{'position': pygame.Rect(1216,576,64,128), 'destination': 1,'spawn_pos': (65,576)},
        {'position': pygame.Rect(512,656,64,64), 'destination': 4,'spawn_pos': (512,129)}],
    4: [{'position': pygame.Rect(512,64,64,64), 'destination': 3,'spawn_pos': (512,592)},
        {'position': pygame.Rect(0,576,64,128), 'destination': 5,'spawn_pos': (1140,576)},
        {'position': pygame.Rect(1216,320,64,128), 'destination': 7,'spawn_pos': (65,320)}],
    5: [{'position': pygame.Rect(1216,576,64,128), 'destination': 4,'spawn_pos': (65,576)}],
    6: [{'position': pygame.Rect(0,320,64,128), 'destination': 2,'spawn_pos': (1140,320)},
        {'position': pygame.Rect(704,656,64,64), 'destination': 11,'spawn_pos': (704,129)}],
    7: [{'position': pygame.Rect(0,320,64,128), 'destination': 4,'spawn_pos': (1140,320)},
        {'position': pygame.Rect(1216,128,64,128), 'destination': 8,'spawn_pos': (65,192)}],
    8: [{'position': pygame.Rect(0,128,64,128), 'destination': 7,'spawn_pos': (1140,192)},
        {'position': pygame.Rect(832,656,64,64), 'destination': 9,'spawn_pos': (832,129)}],
    9: [{'position': pygame.Rect(832,0,64,64), 'destination': 8,'spawn_pos': (832,592)},
        {'position': pygame.Rect(1216,320,64,128), 'destination': 10,'spawn_pos': (65,320)}],
    10: [{'position': pygame.Rect(0,320,64,128), 'destination': 9,'spawn_pos': (1140,320)},
        {'position': pygame.Rect(448,0,64,64), 'destination': 11,'spawn_pos': (448,592)}],
    11: [{'position': pygame.Rect(448,656,64,64), 'destination': 10,'spawn_pos': (448,129)},
        {'position': pygame.Rect(704,0,64,64), 'destination': 6,'spawn_pos': (704,592)}]

}

hero_image = pygame.image.load('hero.png')
hero_image = pygame.transform.scale(hero_image, (60,60))
hero_rect = hero_image.get_rect(center=(player_pos.x,player_pos.y))
ship_image = pygame.image.load('ship.png')
ship_rect = ship_image.get_rect(topleft=(192,192))
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
    text_surface = font.render(f"Sector: {actual_room}        Pieces found: {items}/11", True, (255,255,255))
    screen.blit(text_surface, (10,10))
    screen.blit(hero_image, hero_rect.topleft)
    if actual_room == 1:
        screen.blit(ship_image, ship_rect.topleft)
    if actual_room != 1:
        alien_images = {
            Alien: red_alien_image,
            Yellow_Alien: yellow_alien_image,
            Worm: worm_alien_image
        }
        for alien in aliens[actual_room]:
            screen.blit(alien_images.get(type(alien)),alien.rect.topleft)
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
            resultado = game_over()
            if resultado == "restart":
                player_pos, actual_room, pieces, items = restart_game(initial_pieces)
            elif resultado == "quit":
                runnint = False
            
    if check_win_condition(hero_rect, ship_rect, items, 11):
        show_victory_screen()
        running = False
    pygame.display.flip()
    dt = clock.tick(60) /1000 

pygame.quit()
print('Thank you for playing this demo!')