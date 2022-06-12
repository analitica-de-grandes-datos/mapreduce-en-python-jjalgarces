#
import sys


if __name__ == '__main__':

    curkey = None
    total = 0
    List_8 = []
    result = {}

    for line in sys.stdin:

        Col1, Col3 = line.split("\t")
        Col3 = int(Col3)

        if Col1 in result.keys():
            result[Col1].append(Col3)
        else:
            result[Col1] = [Col3]

    for key, valor in result.items():
        sys.stdout.write("{} {} {}\n".format(key, float(sum(valor)), sum(valor)/len(valor)))
