def create_three_ingots(total_gold: int) -> tuple[dict[str, int]]:
    return tuple({"gold_ingots": total_gold} for x in range(3))


def split_booty(*args: dict[str, int]) -> tuple[dict[str, int]]:
    total_gold = 0
    for elem in args:
        if "gold_ingots" in elem:
            total_gold += elem["gold_ingots"]

    if total_gold % 3 == 0:
        return create_three_ingots(int(total_gold/3))
    else:
        ret_ingots = create_three_ingots(int(total_gold/3))
        for i in range(total_gold % 3):
            ret_ingots[i]["gold_ingots"] += 1
        return ret_ingots


if __name__ == "__main__":
    print(split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10}))
    print(split_booty({"gold_ingots": 3}, {"gold_ingots": 2},
                      {"gold_ingots": 5}, {"gold_ingots": 8}, {"apples": 10}))
    print(split_booty({"gold_ingots": 2}, {"apples": 10}))
    print(split_booty())
