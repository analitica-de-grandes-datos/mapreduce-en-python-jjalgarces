#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    result = {}

    for line in sys.stdin:

        clean = line.strip("\n")

        Col1, Col2 = clean.split("\t")
        Col1 = int(Col1)
        Col2 = Col2.replace(",", "")

        for i in Col2:

            if i in result.keys():
                result[i].append(Col1)
            else:
                result[i] = [Col1]

        sorted_= sorted(result.items(), key=lambda x: x[0])
        list_of_tuples_dict = dict(sorted_)

    # print(list_of_tuples_dict)
    # print(result.values())

    # print(result.keys())


    for key, valor in list_of_tuples_dict.items():
        # print(key, valor)
        elCorch = sorted(valor, key = int)
        valor = ",".join(map(str, elCorch))
    #     # print (key, valor)
        sys.stdout.write("{}\t{}\n".format(key, valor))

        # print(f"{key}{valor}")
        # print(", ".join(valor))
        # x = key, "#".join(valor)
        # print(key.join(valor))
        # sys.stdout.write("{}\t{}\n".format(key, valor))

        
