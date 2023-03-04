"""
Модуль обработки фото.

Создатель Александр Говорухин, @alexitsochi
"""

from PIL import Image, ImageFont, ImageDraw
import datetime
import locale

# Меняем локаль для правильного формата времени.
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)
# Получаем текущие дату/время.
date_time = datetime.datetime.now()
dt_str = date_time.strftime('%d %b %Y %H:%M:%S')


def create_img(kpp_id):
    # Обработка фото
    image = Image.open(f'cache/{kpp_id}')
    width, height = image.size
    idraw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20, encoding="UTF-8")
    text = dt_str
    text2 = "26А улица Яна Фабрициуса"
    text3 = "город-курорт Сочи"
    text4 = "Краснодарский край"

    idraw.text((width - 210, height - 85), text, font=font, fill="White")
    idraw.text((width - 265, height - 65), text2, font=font, fill="White")
    idraw.text((width - 180, height - 45), text3, font=font, fill="White")
    idraw.text((width - 198, height - 25), text4, font=font, fill="White")

    image.save(f"cache/{kpp_id}")


if __name__ == '__main__':
    create_img(kpp_id=1)


