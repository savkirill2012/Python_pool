import random
import time


def emit_gel(step):
    total = 20
    sign = 1
    while True:
        total += sign * random.randrange(0, step)
        print(f"Val now: {total}")
        sign = yield total
        time.sleep(0.7)


def valve(iter):
    num = next(iter)
    sign = 1
    prev_num = 0
    while True:
        if not (10 <= num and num <= 90):
            print(f"Error: Programm end. Val = {num}")
            exit()
        elif 20 > num and prev_num > 20 or num > 80 and prev_num < 80:
            sign *= -1
        prev_num = num
        num = iter.send(sign)


if __name__ == "__main__":
    valve(emit_gel(30))
