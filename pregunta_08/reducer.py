#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
from operator import itemgetter, attrgetter
# import statistics

if __name__ == '__main__':

    curkey = None
    total = 0
    List_8 = []

    # dict_from_list = {}


    for line in sys.stdin:

        Col1, Col3 = line.split("\t")
        Col3 = int(Col3)


        if Col1 == curkey:
    #         # print(Col1)
            total = total + Col3
            List_8.append(Col3)

        else:

            if curkey is not None:
            #
            # una vez se han reducido todos los elementos
            # con la misma clave se imprime el resultado en
            # el flujo de salida
            #
                List_8.append(Col3)
                prom = sum(List_8)/len(List_8)
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, prom))

            curkey = Col1
            total = Col3
            List_8.append(Col3)

        # print(curkey, total)
        prom = sum(List_8)/len(List_8)
        # prom = statistics.mean(List_8)
        # print(curkey)


sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, prom))
