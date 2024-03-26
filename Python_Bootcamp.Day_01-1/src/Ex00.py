def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse
    if "gold_ingots" in purse.keys():
        new_purse["gold_ingots"] += 1
    else:
        new_purse["gold_ingots"] = 1
    return new_purse


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse
    if "gold_ingots" in purse.keys() and new_purse["gold_ingots"] > 0:
        new_purse["gold_ingots"] -= 1
    else:
        new_purse["gold_ingots"] = 0
    return new_purse


def empty(purse: dict[str, int]) -> dict[str, int]:
    new_purse = {}
    return new_purse


if __name__ == "__main__":
    purse = {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    print(add_ingot(add_ingot(add_ingot(empty(purse)))))
    print(add_ingot(get_ingot(get_ingot(empty(purse)))))
    print(purse.keys())
