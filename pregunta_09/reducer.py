#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    tupla_9 = ()
    Lista_9 = []

    for line in sys.stdin:

        Col1, Col2, Col3 = line.split("\t")
        Col3 = int(Col3)

        tupla_9 = (Col1, Col2, Col3)
        # Lista_7 = [Col1, Col2, Col3]
        Lista_9.append(tupla_9)



        sorted_= sorted(Lista_9, key=lambda reg: (reg[2]))
    sort_req = sorted_[:6]
    for elemento in sort_req:
        sys.stdout.write("{}   {}   {}\n".format(elemento[0], elemento[1], elemento[2]))
