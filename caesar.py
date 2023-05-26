import string

def proceso(metodo,cadena,key,alfabeto):
    if metodo==1: return "".join([alfabeto[(alfabeto.index(x)+key)%len(alfabeto)] if x in alfabeto else x for x in cadena])
    else: return "".join([alfabeto[(alfabeto.index(x)-key)%len(alfabeto)] if x in alfabeto else x for x in cadena])

def main():
    if int(input("¿Con números? --> 1; 0 e.o.c. \n"))==1:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n"),int(input("Digite la llave \n")),list(string.ascii_lowercase)+[str(x) for x in range(10)]))
    else:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n"),int(input("Digite la llave \n")),list(string.ascii_lowercase)))

main()