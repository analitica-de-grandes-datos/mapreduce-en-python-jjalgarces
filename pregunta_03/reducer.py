#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
if __name__ == '__main__':
    dict_from_list = {}

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        dict_from_list[key] = val

        sorted_= sorted(dict_from_list.items(), key=operator.itemgetter(1))
        # keyssss = sorted_.keys()
        # sorted_list = sorted(dict_from_list.items(), key=lambda x: x[1])
        # complete = key + "," + val

    for elemento in sorted_:
        print(elemento)
