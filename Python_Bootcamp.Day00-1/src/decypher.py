import argparse


def pars_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str,
                        help="Set text for decript")
    args = parser.parse_args()
    return args.text


def decryptor(text_to_decript: str):
    for word in text_to_decript.split(" "):
        print(word[0], end="")
    print()


if __name__ == "__main__":
    decryptor(pars_args())
