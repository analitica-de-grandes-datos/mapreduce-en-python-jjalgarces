from re import I
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0
    Max_6 = 0
    Min_6 = 0
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:
        

        key, val = line.split("\t")
        # val = int(val)

        # print(key, val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            if val > Max_6:
                Max_6 = val
            elif val < Min_6:
                Min_6 = val
            else:
                Max_6 = val
                Min_6 = val
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, Max_6, Min_6))

            curkey = key
            Max_6 = val
            Min_6 = val

        sys.stdout.write("{}\t{}\t{}\n".format(curkey, Max_6, Min_6))
