import sys


if __name__ == '__main__':

    result = {}

    for line in sys.stdin:

        clean = line.strip("\n")
        # line = line.replace("\n", "\t")
        Col1, Col3 = clean.split("\t")
        # Col3 = int(Col3)
        # print(Col1, Col3)

        if Col1 in result.keys():
            result[Col1].append(Col3)
        else:
            result[Col1] = [Col3]

    for key, valor in result.items():
    #     # print(key, float(sum(valor)), sum(valor)/len(valor))
        sys.stdout.write("{}\t{}\t{}\n".format(key, max(valor), min(valor)))
