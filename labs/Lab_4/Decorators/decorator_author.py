from functools import wraps


def author(param):
    name = param

    @wraps(param)
    def decorator(func):
        result = f"Name:\n{name}\n" + "Characteristics:\n" + func()
        print("----------------- \n")
        print(result)
        func._author = name
        return func

    return decorator


def main():
    while True:
        name = input("Input name : ")
        if name == "Exit" or name == "exit":
            return False
        else:
            data = input("Input params : ").split(',')

            @author(name)
            def add_info(*args):
                res_info = ''
                for i in range(len(args)):
                    res_info += f"{args[i]} | "
                return res_info

            print(add_info(*data))
            print("Here is a add_info._author method prints : ", add_info._author)


if __name__ == '__main__':
    main()
    print("-- Successfully Compiled")
else:
    print("-- Error")
