import pygame as pyg
import sys
from Btn import Btn
from Stack import Stack
from Card import Card
from Player import Player
from Slider import Slider
from CircularLinkedList import CircularLinkedList

pyg.init()


def generate_maze():
    lis=Stack()
    numeros = ["1","2","3","4","5","6","7","8","9","+1"]
    colores = ["amarillo","rojo","azul","verde"]
    
    for numero in numeros:
        for color in colores:
            lis.push(Card(color,numero))
            
    for i in range(4):
        lis.push(Card("all", "+4"))
    
    return lis
            
class juego:
    def __init__(self):
        self.main_menu()
    
    def main_menu(self):
        screen.fill("black")
        background=pyg.image.load('Imagenes/menu.png')
        img_btn_Play=pyg.image.load('Imagenes/Play.png').convert_alpha()
        img_btn_Exit=pyg.image.load('Imagenes/Exit.png').convert_alpha()
        
        play_btn=Btn(240, 250,img_btn_Play,.5,'Imagenes/Play.png',screen)
        exit_btn=Btn(240, 400,img_btn_Exit,.5,'Imagenes/Exit.png',screen)
        
        running=True
        
        while running:
            screen.fill("black")
            
            screen.blit(background,(0,0))
            mouse_pos = pyg.mouse.get_pos()
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                    running=False
                
                    
                
                if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1: 
                    if play_btn.is_hovered(mouse_pos):
                        print("Play presionado")
                        play_btn.draw_activate()
                        self.selection()
                        running=False
                      
    
                    if exit_btn.is_hovered(mouse_pos):
                        print("Exit presionado")
                        exit_btn.draw_activate()
                        pyg.quit()
                        sys.exit()
                        
            
            if play_btn.is_hovered(mouse_pos):
                play_btn.draw_activate()
            else:
                play_btn.draw()
    
            if exit_btn.is_hovered(mouse_pos):
                exit_btn.draw_activate()
            else:
                exit_btn.draw()
            
            pyg.display.update()
            clock.tick(60)
            
    
    def selection(self):
        background=pyg.image.load('Imagenes/menu.png')
        img_btn_volver=pyg.image.load('Imagenes/volver.png')
        img_btn_Continue=pyg.image.load('Imagenes/Continue.png')
        img_Players=pyg.image.load('Imagenes/Players.png').convert_alpha()
        img_Bots=pyg.image.load('Imagenes/Bots.png').convert_alpha()
        
        img_min_players=pyg.image.load('Imagenes/2.png').convert_alpha()
        img_max_players=pyg.image.load('Imagenes/4.png').convert_alpha()
        
        bar_img = pyg.image.load("Imagenes/slidebar.png").convert_alpha()
        handle_img = pyg.image.load("Imagenes/handle.png").convert_alpha()
        
        
        img_Players = pyg.transform.scale(img_Players, (150, 50))
        img_Bots = pyg.transform.scale(img_Bots, (150, 50))
        
        img_min_players=pyg.transform.scale(img_min_players, (50,50))
        img_max_players=pyg.transform.scale(img_max_players, (50,50))
        
        slider_player = Slider(200, 300, bar_img, handle_img, (400, 40), (60, 60), 2, 4, 2)
        screen.fill("black")
        volver_btn=Btn(0, 0,img_btn_volver,.25,'Imagenes/volver.png',screen)
        Continue_btn=Btn(225, 450,img_btn_Continue,.4,'Imagenes/Continue.png',screen)
        
        
        running=True
        while running:
            screen.fill("black")
            
            screen.blit(background,(0,0))
            mouse_pos = pyg.mouse.get_pos()
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                    running=False
                
                slider_player.handle_event(event)
                
                if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                    if volver_btn.is_hovered(mouse_pos):
                        volver_btn.draw_activate()
                        running=False
                        self.main_menu()
                        
                    if Continue_btn.is_hovered(mouse_pos):
                        Continue_btn.draw_activate()
                        running=False
                        self.juego(slider_player.value)
            
            
            if volver_btn.is_hovered(mouse_pos):
                volver_btn.draw_activate()
            else:
                volver_btn.draw()
            
            if Continue_btn.is_hovered(mouse_pos):
                Continue_btn.draw_activate()
            else:
                Continue_btn.draw()
            
            slider_player.draw(screen)
            
            img_players_rect = img_Players.get_rect(midbottom=(slider_player.bar_rect.centerx, slider_player.bar_rect.top - 10))
            screen.blit(img_Players, img_players_rect)
            
            offset_x = 40  

            
            img_min_players_rect = img_min_players.get_rect(
                midright=(slider_player.bar_rect.left + offset_x-20,
                          slider_player.bar_rect.centery - 10)
            )
            
            
            img_max_players_rect = img_max_players.get_rect(
                midleft=(slider_player.bar_rect.right - offset_x,
                         slider_player.bar_rect.centery - 10)
            )
            
            screen.blit(img_min_players, img_min_players_rect)
            screen.blit(img_max_players, img_max_players_rect)


                
            pyg.display.update()
            clock.tick(60)
    
    def crear_botones_cartas(self,jugador, x_base, y_base, separacion=30, escala=0.25):
        botones = []
        offset = 40
        current_card = jugador.hand._LinkedList__head  
        
        while current_card:
            carta = current_card.get_data()
            img = pyg.image.load(carta.get_image_path()).convert_alpha()
            img = pyg.transform.scale(img, (360, 480))
            
          
            btn_carta = Btn(x_base + offset, y_base, img, escala, carta.get_image_path(),screen)
            botones.append(btn_carta)
            
            offset += separacion+30
            current_card = current_card.get_next()
    
        return botones
    
    def robar_carta(self,thief_maze, used_maze):
        if thief_maze.is_empty():
            if not used_maze.is_empty():
                top_card = used_maze.pop()
                thief_maze = used_maze
                thief_maze.shuffle()
                used_maze = Stack()
                used_maze.push(top_card)
            else:
                print("No quedan cartas en ninguno de los mazos")
                return None, thief_maze, used_maze
    
        return thief_maze.pop(), thief_maze, used_maze
    
    def draw_player_hand(self, player, position, hide_cards=True, vertical=False):
        x, y = position
        spacing = 30
        for i, card in enumerate(player.hand.to_list()):
            if hide_cards:
                img = pyg.image.load("Imagenes/back_card.png").convert_alpha()
            else:
                img = pyg.image.load(card.get_image_path()).convert_alpha()
            
            img = pyg.transform.scale(img, (90, 120))
            
            if vertical:
                screen.blit(img, (x, y + i * spacing))
            else:
                screen.blit(img, (x + i * spacing, y))
    
    def juego(self, players):
        jugadores = CircularLinkedList()
        for i in range(players):
            Datos = Player(f"Jugador {i+1}")
            jugadores.append(Datos)
    
        background = pyg.image.load('Imagenes/mesa.png')
        img_btn_volver = pyg.image.load('Imagenes/volver.png')
        img_btn_card_back = pyg.image.load('Imagenes/back_card.png')
        img_btn_card_back = pyg.transform.scale(img_btn_card_back, (360, 480))
    
        thief_maze = generate_maze()
        used_maze = Stack()
        thief_maze.shuffle()
    
        current_player_node = jugadores.get_head()
    
        
        for i in range(7):
            for j in range(players):
                current_player_node.get_data().add_card(thief_maze.pop())
                current_player_node = current_player_node.get_next()
    
        volver_btn = Btn(0, 0, img_btn_volver, .25, 'Imagenes/volver.png',screen)
        
        img_rojo = pyg.image.load("Imagenes/rojo.png").convert_alpha()
        img_rojo=pyg.transform.scale(img_rojo, (200,360))
        img_azul = pyg.image.load("Imagenes/azul.png").convert_alpha()
        img_azul=pyg.transform.scale(img_azul, (200,360))
        img_verde = pyg.image.load("Imagenes/verde.png").convert_alpha()
        img_verde=pyg.transform.scale(img_verde, (200,360))
        img_amarillo = pyg.image.load("Imagenes/amarillo.png").convert_alpha()
        img_amarillo=pyg.transform.scale(img_amarillo, (200,360))
        
        btn_rojo = Btn(200, 250, img_rojo, 0.3, "rojo",screen)
        btn_azul = Btn(300, 250, img_azul, 0.3, "azul",screen)
        btn_verde = Btn(400, 250, img_verde, 0.3, "verde",screen)
        btn_amarillo = Btn(500, 250, img_amarillo, 0.3, "amarillo",screen)
        
        botones_color = [btn_rojo, btn_azul, btn_verde, btn_amarillo]
        
        img_win = pyg.image.load("Imagenes/win.png").convert_alpha()
        img_win=pyg.transform.scale(img_azul, (400,360))
            
        running = True
    
       
        jugador_actual = current_player_node.get_data()
        cartas_btns = self.crear_botones_cartas(jugador_actual, 150, screen.get_height() - 120)
        
        mazo_btn = Btn(300, 200, img_btn_card_back, 0.25, "mazo",screen)  
        discard_img = None
        discard_rect = None
        
        other_player_info = [
            {"pos": (50, 50), "vertical": True},                       
            {"pos": (screen.get_width() - 150, 50), "vertical": True}, 
            {"pos": (screen.get_width() - 150, 150), "vertical": True},
            {"pos": (50, 150), "vertical": True}                     
        ]
    
        while running:
            screen.fill("black")
            screen.blit(background, (0, 0))
            mouse_pos = pyg.mouse.get_pos()
            
            node = jugadores.get_head()
            draw_idx = 0
            for _ in range(players):
                player = node.get_data()
                if player != jugador_actual:
                    info = other_player_info[draw_idx]
                    self.draw_player_hand(
                        player,
                        info["pos"],
                        hide_cards=True,
                        vertical=info["vertical"]
                    )
                    draw_idx += 1
                node = node.get_next()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                    running = False
    
                if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
                    if volver_btn.is_hovered(mouse_pos):
                        volver_btn.draw_activate()
                        running = False
                        self.main_menu()
                        
                    if mazo_btn.is_hovered(mouse_pos):
                        if not thief_maze.is_empty():
                            nueva_carta = thief_maze.pop()
                            jugador_actual.add_card(nueva_carta)
                            print(f"{jugador_actual.name} robó {nueva_carta}")
                            cartas_btns = self.crear_botones_cartas(jugador_actual, 150, screen.get_height() - 120)
                        
                        else:
                            thief_maze=used_maze
                            thief_maze.shuffle()
                            used_maze=Stack()
                            
    
                    for btn in cartas_btns:
                        if btn.is_hovered(mouse_pos):
                            print(f"Carta seleccionada: {btn.nombre}")
    
                            
                            carta_jugada = None
                            current_card_node = jugador_actual.hand._LinkedList__head
                            while current_card_node:
                                if current_card_node.get_data().get_image_path() == btn.nombre:
                                    carta_jugada = current_card_node.get_data()
                                    break
                                current_card_node = current_card_node.get_next()
    
                            if carta_jugada:
                                
                                if not used_maze.is_empty():
                                    ultima_carta = used_maze.peek()
                                    if not (carta_jugada.color == ultima_carta.color or
                                            carta_jugada.numero == ultima_carta.numero or
                                            carta_jugada.color == "all"):
                                        print("Movimiento inválido: no coincide en color ni número.")
                                        break  
    
                               
                                used_maze.push(carta_jugada)
                                jugador_actual.remove_card(carta_jugada)
                                
                                img_top = pyg.image.load(carta_jugada.get_image_path()).convert_alpha()
                                img_top = pyg.transform.scale(img_top, (90, 120)) 
                                discard_img = img_top
                                discard_rect = discard_img.get_rect(topleft=(450, 200))
    
                                
                                cartas_btns = self.crear_botones_cartas(jugador_actual, 150, screen.get_height() - 120)
                                
                                if str(carta_jugada.numero).strip() =="+4" or str(carta_jugada.color).strip().lower() == "all":
                                    eligiendo_color = True
                                    while eligiendo_color:
                                        screen.fill("black")
                                        screen.blit(background, (0, 0))
                            
                                        for btn in botones_color:
                                            btn.draw()
                            
                                        pyg.display.update()
                            
                                        for e in pyg.event.get():
                                            if e.type == pyg.QUIT:
                                                pyg.quit()
                                                sys.exit()
                                            if e.type == pyg.MOUSEBUTTONDOWN and e.button == 1:
                                                for btn in botones_color:
                                                    if btn.is_hovered(pyg.mouse.get_pos()):
                                                        nuevo_color = btn.nombre
                                                        print(f"Color elegido: {nuevo_color}")
                                                        carta_jugada.color = nuevo_color
                                                        eligiendo_color = False
                                                        break
                                                    
                                jugador_sig=current_player_node.get_next().get_data()
                                
                                if carta_jugada.numero=="+4":
                                    for i in range(4): 
                                        nueva_carta, thief_maze, used_maze = self.robar_carta(thief_maze, used_maze)
                                        if nueva_carta:
                                            jugador_sig.add_card(nueva_carta)

                                
                                if carta_jugada.numero=="+1":
                                    nueva_carta, thief_maze, used_maze = self.robar_carta(thief_maze, used_maze)
                                    if nueva_carta:
                                        jugador_sig.add_card(nueva_carta)

                                    
                                if jugador_actual.hand.empty():
                                    img_win_rect = img_win.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                                    screen.blit(img_win, img_win_rect)
                                
                                else:
                                    current_player_node = current_player_node.get_next()
                                    jugador_actual = current_player_node.get_data()
                                    cartas_btns = self.crear_botones_cartas(jugador_actual, 150, screen.get_height() - 120)
            
    
            
            if volver_btn.is_hovered(mouse_pos):
                volver_btn.draw_activate()
            else:
                volver_btn.draw()
    
            for btn in cartas_btns:
                if btn.is_hovered(mouse_pos):
                    btn.draw_activate()
                else:
                    btn.draw()
                
            mazo_btn.draw()
            if discard_img:
                screen.blit(discard_img, discard_rect)
    
            pyg.display.update()
            clock.tick(60)


                
ANCHO, ALTO = 800, 600
screen = pyg.display.set_mode((ANCHO, ALTO))
pyg.display.set_caption("Tikche")
clock = pyg.time.Clock()

juego()

pyg.quit()
sys.exit()
