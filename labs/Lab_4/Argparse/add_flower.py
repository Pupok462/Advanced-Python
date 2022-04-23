import json
import argparse

array = ['name', 'country', 'petal-colour', 'stem-length', 'with-thorns', 'companion-plants']


def cmd_input():
    parser = argparse.ArgumentParser(description='How to add something into journal.txt')
    parser.add_argument(f"--{array[0]}", f"--{array[0][:1]}", default=None, type=str, metavar='Название')
    parser.add_argument(f"--{array[1]}", f"--{array[1][:1]}", default=None, type=str, metavar='Страна')
    parser.add_argument(f"--{array[2]}", f"--{array[2][:5]}", default=None, type=str, metavar='Цвет лепестка')
    parser.add_argument(f"--{array[3]}", f"--{array[3][:4]}", default=None, type=int,
                        metavar='Длина стебля в сантиметрах')
    parser.add_argument(f"--{array[4]}", f"--{array[4][:4]}", action="store_true")
    parser.add_argument(f"--{array[5]}", f"--{array[5][:9]}", default=None, type=str,
                        metavar='С какими растениями хорошо сочетается в букете', nargs='+')
    args = parser.parse_args()
    return args


def upload_in_txt():
    result = cmd_input()
    with open('journal.txt', 'a') as journal:
        dictionary = {
            array[0]: result.name,
            array[1]: result.country,
            array[2]: result.petal_colour,
            array[3]: result.stem_length,
            array[4]: result.with_thorns,
            array[5]: result.companion_plants
        }
        json.dump(dictionary, journal, indent=4)


def main():
    upload_in_txt()


if __name__ == '__main__':
    main()
    print("-- Successfully Compiled")
else:
    print("-- Error")
