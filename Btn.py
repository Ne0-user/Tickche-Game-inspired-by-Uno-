import pygame as pyg

class Btn:
    def __init__(self,x,y,image,scale,nombre,screen):
        self.w=image.get_width()
        self.h=image.get_height()
        self.image=pyg.transform.scale(image, (int(self.w*scale),int(self.h*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.nombre=nombre
        self.scale=scale
        self.screen=screen
        
    def draw(self):
        self.screen.blit(self.image, (self.rect.x,self.rect.y))
    
    def draw_activate(self):
        base, ext = self.nombre.split(".")
        nombre_act = base + "_activate." + ext
        img_act = pyg.image.load(nombre_act).convert_alpha()
        img_act=pyg.transform.scale(img_act, (int(self.w*self.scale),int(self.h*self.scale)))
        self.screen.blit(img_act, (self.rect.x, self.rect.y))
        
    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)