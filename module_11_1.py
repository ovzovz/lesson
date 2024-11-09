import requests
from PIL import Image, ImageFilter

def pillow_test():
    im=Image.open('1.jpg') # открытие файла с изображением
    w,h= im.size # размеры изображения
    new_im=im.resize((w//2,h//2)) # изменение размера
    new_im=im.reduce(2) # тоже изменение размера
    new_im=new_im.rotate(45,expand=True) # поворот на угол 45 без обрезки углов изображения
    new_im.save('new_1.png') # сохранение в др.формате
    gray_img = im.convert("L") # в  градациях серого
    gray_img = gray_img.filter(ImageFilter.EMBOSS) # тиснение
    gray_img.show() #  открытие изображения в программе просмотрщике

def  requests_test():
    req = requests.get('https://ru.pinterest.com/') #GET-метод используется для обычного запроса к серверу и получения информации по URL
    print(req.status_code) #код завершения запроса (200=ОК)
    print(req.encoding) # кодировка
    print(req.headers) # заголовки, которые вернул сервер
    print(req.request.headers) # заголовки, которые были направлены серверу
    # запрос с параметром:
    query = {'q': 'тыква'}
    req = requests.get('https://ru.pinterest.com/search/pins/', params=query)
    print(req.url) #ссылка с нужными параметрами запроса

pillow_test()
requests_test()