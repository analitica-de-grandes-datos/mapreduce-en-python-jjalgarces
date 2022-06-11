#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    tupla_7 = ()
    Lista_7 = []

    for line in sys.stdin:

        Col1, Col2, Col3 = line.split("\t")
        Col3 = int(Col3)
        # Lista_7 = [Col1, Col2, Col3]
        # X = "\t".join(Lista_7)

        # X = X.replace("\n", "")
        # # X = X.replace("\t", "")
        # # X = X.replace("  ", ";")
        # X = X.split()

        # Col3 = Col3.strip("\n")
        # 
        # # Col1, Col2, Col3 = line.split("\t")
        # # Col1, Col2, Col3 = line.split("\n")

        tupla_7 = (Col1, Col2, Col3)
        # Lista_7 = [Col1, Col2, Col3]
        Lista_7.append(tupla_7)
        # x = ",".join(tupla_7)
        # x = tuple(x)

        # # tuple_new = tuple(tupla_7)
        # # tupla_7 = tupla_7.split(')')

        # for row in tupla_7:
        #     print(row)

        # list_tup = list(tupla_7)
 
        # Reg_Sort = sorted(tupla_7, key=lambda reg: reg[0])
        # Reg_Sort = sorted(tupla_7, key=itemgetter(0))

        sorted_= sorted(Lista_7, key=lambda reg: (reg[0], reg[2]))

    for elemento in sorted_:
        sys.stdout.write("{}  {}  {}\n".format(elemento[0], elemento[1], elemento[2]))
