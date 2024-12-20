from PIL import Image, ImageFilter, ImageDraw
from k import ImageHandler

class ImageProcessor():
    #функция при создании
    def __init__(self, img):
        self.img = img
    
    #добавление фильтра EMBOSS
    def add_filter(self):
        self.img = self.img.filter(ImageFilter.EMBOSS)
        return self.img
    
    #изменение размера
    def change_size(self):
        try:
            w = int(input("Введите ширину изображения: "))
            h = int(input("Введите высоту изображения: "))
            self.img = self.img.resize(w,h)
            print("Размер изображения изменён")
        except:
            print("Некорректный ввод данных")
        return self.img
    
    #добавление водяного знака
    def watermark(self):
        with Image.open("k\\watermark.jpg") as wm:
            wm.load()
        w,h = self.img.size
        w2,h2=wm.size
        wm.putalpha(128)
        self.img.paste(wm, (w-w2,h-h2), wm)
        return self.img
