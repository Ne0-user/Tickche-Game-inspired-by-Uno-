import pygame as pyg


class Slider:
    def __init__(self, x, y, bar_img, handle_img, bar_size, handle_size, min_val=2, max_val=4, start_val=2):
        
        self.bar = pyg.transform.scale(bar_img, bar_size)
        self.handle = pyg.transform.scale(handle_img, handle_size)

        self.bar_rect = self.bar.get_rect(topleft=(x, y))
        
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        
        
        self.handle_rect = self.handle.get_rect()
        self.handle_rect.centery = self.bar_rect.centery
        self.dragging = False
        
        self.update_handle_pos()

    def update_handle_pos(self):
        available_width = self.bar_rect.width - self.handle_rect.width
        rel = (self.value - self.min_val) / (self.max_val - self.min_val)
        self.handle_rect.centerx = self.bar_rect.left + self.handle_rect.width//2 + int(rel * available_width)

    def draw(self, surface):
        surface.blit(self.bar, self.bar_rect)
        surface.blit(self.handle, self.handle_rect)

    def handle_event(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pyg.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pyg.MOUSEMOTION and self.dragging:
            min_x = self.bar_rect.left + self.handle_rect.width//2
            max_x = self.bar_rect.right - self.handle_rect.width//2
            x = max(min_x, min(event.pos[0], max_x))
            self.handle_rect.centerx = x
            
            
            available_width = self.bar_rect.width - self.handle_rect.width
            rel = (x - min_x) / available_width
            self.value = int(self.min_val + rel * (self.max_val - self.min_val))
        
