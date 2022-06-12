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
  col_2 = col[1]
  col_3 = col[2]


  sys.stdout.write("{}\t{}\t{}\n".format(col_1, col_2, col_3))
