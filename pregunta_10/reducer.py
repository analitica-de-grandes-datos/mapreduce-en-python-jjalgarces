#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    result = {}

    for line in sys.stdin:

        clean = line.strip("\n")

        Col1, Col2 = clean.split("\t")
        Col1 = int(Col1)
        Col2 = Col2.replace(",", "")

        for i in Col2:

            if i in result.keys():
                result[i].append(Col1)
            else:
                result[i] = [Col1]

    # print(result)
    # print(result.values())

    for key, valor in result.items():
        sys.stdout.write("{}\t{}\n".format(key, valor))
