#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
##FUNCIÓN MAP

# Esta es la funcion que mapea la entrada a parejas (clave, valor)

import sys
if __name__ == "__main__":

# itera sobre cada linea de codigo recibida
# a traves del flujo de entrada

  for line in sys.stdin:

    #Eliminar vacíos
    clean = line.strip()

    col = clean.split(',')
    col_1 = col[0]
    col_2 = col[1]

  # escribe al flujo estandar de salida

    # print ('%s, %s' %  (col_1, col_2))
    print ('%s\t%s' % (col_1, col_2))
