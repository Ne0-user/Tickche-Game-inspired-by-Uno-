import os

class Card:
    def __init__(self,color,numero,habilidad=None,dis=None,ext=".png"):
        self.color=color
        self.numero=numero
        self.habilidad=habilidad
        
        if dis:
            self.dis=dis + ext
        
        else:
            self.dis=f"{numero}_{color}{ext}"
    
    def get_image_path(self, base_dir="Imagenes"):
        return os.path.join(base_dir, self.dis)
    
    def __repr__(self):
        return self.dis