import sys
import argparse


def pars_args() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("max_len", type=int,
                        help="Set argument : count of readable lines")
    args = parser.parse_args()
    return args.max_len


def parser_by_template(max_len: int):
    loc_counter = 0
    if max_len < 0:
        print("Set number bigger than zero")
        return
    for elem in sys.stdin:
        elem = elem.strip()
        if len(elem) == 32 and elem[:5] == "00000" and elem[5] != "0":
            print(elem)
        loc_counter += 1
        if loc_counter == max_len:
            break


if __name__ == "__main__":
    parser_by_template(pars_args())
