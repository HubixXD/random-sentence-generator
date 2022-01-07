import sys
from random import randint


def incremented_randomness(org: list) -> list:
    foo = [None for i in range(len(org))]
    for index, _ in enumerate(org):
        r_int = randint(0, index)
        # print(index, r_int)
        if org[r_int] not in foo:
            foo.append(org[r_int])
        else:
            foo[index] = org[r_int]
        # print(foo)
    return foo


def main():
    arg = sys.argv[1]

    with open(arg, 'r') as f:
        original = f.read().replace('\n', " ").split(" ")

    final = incremented_randomness(original)

    with open('output.txt', 'w') as f:
        for word in final:
            if word:
                f.write(f"{word} ")


if __name__ == '__main__':
    main()
