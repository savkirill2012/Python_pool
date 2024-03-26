import sys
import re


def mfinder():
    patterns = (
        "\*(?!\*).(?!\*).(?!\*).\*",
        "\*\*(?!\*).\*\*",
        "\*(?!\*).\*(?!\*).\*"
    )

    for i, row in enumerate(sys.stdin):
        if len(row.strip()) != 5 or i > 2:
            return "Error"
        if not re.search(patterns[i], row.strip()):
            return "False"
    return "True"


if __name__ == "__main__":
    print(mfinder())
