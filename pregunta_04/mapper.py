#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

# itera sobre cada linea de codigo recibida
# a traves del flujo de entrada

for line in sys.stdin:

# genera las tuplas palabra \tabulador 1
# ya que es un conteo de palabras
  clean = line.strip()

  col = clean.split()

  

  col_1 = col[0]

# escribe al flujo estandar de salida

  sys.stdout.write("{}\t1\n".format(col_1))
