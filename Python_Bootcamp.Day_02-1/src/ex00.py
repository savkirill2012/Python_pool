class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"

    def __str__(self) -> str:
        return "GeneralTsoKeycard"

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, key: int) -> int:
        try:
            if key == 404:
                return 3
            else:
                raise KeyError("No key")
        except TypeError:
            raise TypeError("Type error")

    def __gt__(self, other: int) -> bool:
        if other <= 9000:
            return True
        else:
            return False


if __name__ == "__main__":
    key = Key()

    print(len(key) == 1337)
    print(key[404] == 3)
    print(key > 9000)
    print(key.passphrase == "zax2rulez")
    print(str(key) == "GeneralTsoKeycard")
