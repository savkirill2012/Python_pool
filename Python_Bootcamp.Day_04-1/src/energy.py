def is_str(elem: str) -> bool:
    if type(elem) is str:
        return True
    else:
        return False


def fix_wiring(cables: list, sockets: list, plugs: list):
    n_plugs = list(filter(is_str, plugs))
    inner = list(zip((filter(is_str, cables)), filter(is_str, sockets)))
    loc_counter = 0
    for elem in inner:
        if loc_counter < len(n_plugs):
            yield f"plug {elem[0]} into {elem[1]} " + \
                f"using {n_plugs[loc_counter]}"
        else:
            yield f"weld {elem[0]} to {elem[1]} without plug"
        loc_counter += 1


if __name__ == "__main__":
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for c in fix_wiring(cables, sockets, plugs):
        print(c)
