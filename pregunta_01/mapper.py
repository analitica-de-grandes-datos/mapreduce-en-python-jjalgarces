#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)

import sys
if __name__ == "__main__":

# itera sobre cada linea de codigo recibida
# a traves del flujo de entrada

  for line in sys.stdin:

  # genera las tuplas palabra \tabulador 1
  # ya que es un conteo de palabras

    col = line.split(',')
    col_credit_history = col[2]

  # escribe al flujo estandar de salida

    sys.stdout.write("{}\t1\n".format(col_credit_history))
