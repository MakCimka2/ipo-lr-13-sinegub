from k import ImageHandler, ImageProcessor

def main():
    f = False
    try:
        Image = ImageHandler.ImageHandler(input("Введите название изображения с форматом: "))
        f = True
    except:
        print("Изображение не найдено")
    
    while f:
        c = int(input("=============\n1 - Сохранить изображение\n2 - Сохранить изображение с датой\n3 - Изменить формат изображения\n4 - Масштабировать изображение до 50%\n5 - Добавление фильтра EMBOSS\n6 - Изменить размер изображения\n7 - Добавить водяной знак\n=============\n"))
        if c == 1:
            ImageHandler.ImageHandler.save(Image)
            exit()

        elif c == 2:
            ImageHandler.ImageHandler.save_with_data(Image)
            exit()
    
        elif c == 3: 
            ImageHandler.ImageHandler.change_format(Image)
        
        elif c == 4: 
            ImageHandler.ImageHandler.change_scale(Image)
    
        elif c == 5: 
            Image.img = ImageProcessor.ImageProcessor.add_filter(Image)

        elif c == 6: 
            Image.img = ImageProcessor.ImageProcessor.change_size(Image)

        elif c == 7: 
            Image.img = ImageProcessor.ImageProcessor.watermark(Image)
        
        else: 
            print('Введите корректное значение')

if __name__=="__main__":
    main()
