import pygame
import sys

class Tiktekto:
    def __init__(self):
        pygame.init() # biar pygame ny bs dipakek
        
        self.size = lebar, tinggi = 640, 320
        self.background = (224, 241, 244)
        self.warna_game = (0, 55, 61) # Red, Green, Blue
        self.screen = pygame.display.set_mode(self.size) # buat nampilin

    def main_game(self):
        while True:
            self.screen.fill(self.background) # ngisi layar pake background di atas, jd setiap permainan baru, dia bakal munculin latar baru terus
            for event in pygame.event.get(): # untuk semua event yg terjd
                if event.type == pygame.QUIT: # klo ad yg keluat, berarti ya keluar dr gamenya
                    sys.exit()

                self.gambar_border()
                pygame.display.flip() # manggil fungsi untuk memperbaharui setiap layar setiap add perubahan
    
    def gambar_border(self):
        screen_lebar, screen_tinggi = self.size

        garis = [

            {
                'Mulai' : [],
                'Selesai' : []
            },

        ]

if __name__ == "__main__":
    Tiktekto()

#Syasya