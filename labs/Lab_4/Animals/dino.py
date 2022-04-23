import os
import warnings
from PIL import (
    Image,
    ImageDraw,
    ImageFont,
)

name = input("Введите имя: ")

BIRTHDAY_GREETINGS = r"""
  _____________________
|      Hello, """ f"{name}" r"""      |
  =====================
                            \
                             \
                              \
                               \
                                  .-=-==--==--.
                            ..-=="  ,'o`)      `.
                          ,'         `"'         \
                         :  (                     `.__...._
                         |                  )    /         `-=-.
                         :       ,vv.-._   /    /               `---==-._
                          \/\/\/VV ^ d88`;'    /                         `.
                              ``  ^/d88P!'    /             ,              `._
                                 ^/    !'   ,.      ,      /                  "-,,__,,--''"'"-.
                                ^/    !'  ,'  \ . .(      (         _           )  ) ) ) ))_,-.\
                               ^(__ ,!',"'   ;:+.:%:a.     \:.. . ,'          )  )  ) ) ,"'    '
                               ',,,'','     /o:::":%:%a.    \:.:.:         .    )  ) _,'
                                '''''''''       ;':::'' `+%%%a._  \%:%|         ;.). _,-""
                                       ,-='_.-'      ``:%::)  )%:|        /:._,"
                                      (/(/"           ," ,'_,'%%%:       (_,' 
                                                     (  (//(`.___;        \
                                                      \     \    `         `
                                                       `.    `.   `.        :
                                                         \. . .\    : . . . :
                                                          \. . .:    `.. . .:
                                                           `..:.:\     \:...\
                                                            ;:.:.;      ::...:
                                                            ):%::       :::::;
                                                        __,::%:(        :::::
                                                     ,;:%%%%%%%:        ;:%::
                                                       ;,--""-.`\  ,=--':%:%:\
                                                      /"       "| /-".:%%%%%%%\
                                                                      ;,-"'`)%%)
                                                                     /"      "|
"""


FONT_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'fonts', 'mono', 'Roboto-Mono', 'Roboto-Mono-700.ttf'
)

FONT_SIZE = 20


if __name__ == '__main__':
    image = Image.new(
        mode='RGB',
        size=(1200, 1020),
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

    image.save('hello_from_the_dino.png')