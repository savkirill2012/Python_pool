from Ex00 import add_ingot, get_ingot, empty


def squeak_dec(func):
    def wrapper(*args, **kwargs):
        tmp = func(*args, **kwargs)
        print("SQUEAK")
        return tmp
    return wrapper


add_ingot = squeak_dec(add_ingot)
get_ingot = squeak_dec(get_ingot)
empty = squeak_dec(empty)


if __name__ == "__main__":
    purse = {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    print(add_ingot(add_ingot(add_ingot(empty(purse)))))
    print(add_ingot(get_ingot(get_ingot(empty(purse)))))
    print(purse.keys())
