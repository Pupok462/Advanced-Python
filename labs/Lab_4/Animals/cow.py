import os
import warnings
from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)


name = input("Введите имя : ")
age = input( "Введите возраст :")

BIRTHDAY_GREETINGS = r"""
  _________________________
/   Happy Birthday, """  f"{name}"r"""!  \
\ You are now """ f"{age} " r"""years old!/
  =========================
                \
                 \
                   ^__^
                   (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||
"""

FONT_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'fonts', 'mono', 'Roboto-Mono', 'Roboto-Mono-700.ttf'
)

FONT_SIZE = 30


if __name__ == '__main__':
    image = Image.new(
        mode='RGB',
        size=(650, 500),
        color=(255, 255, 255),
    )

    draw = ImageDraw.Draw(image)

    if os.path.isfile(FONT_FILE_PATH):
        font = ImageFont.truetype(FONT_FILE_PATH, FONT_SIZE)
    else:
        font = None

        warnings.warn(f'No font file "{FONT_FILE_PATH}" found!')

    draw.text(
        xy=(0, 0),
        text=BIRTHDAY_GREETINGS,
        font=font,
        fill=(0, 0, 0),
    )

    image.save('happy_birthday_from_the_cow.png')