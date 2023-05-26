from operator import xor
import string

def proceso(cadena,key,alfabeto):
    resultado=list()
    for i in range(len(cadena)):
        x=xor(alfabeto.index(cadena[i]),alfabeto.index(key[i]))
        if x>len(alfabeto): x-=len(alfabeto)
        resultado.append(alfabeto[x])
    return "".join(resultado)

def main():
    if int(input("¿Con números? --> 1; 0 e.o.c. \n"))==1:
        print(proceso(input("Digite la cadena \n").lower(),input("Digite la llave \n"),list(string.ascii_lowercase)+[str(x) for x in range(10)]))
    else:
        print(proceso(input("Digite la cadena \n").lower(),input("Digite la llave \n"),list(string.ascii_lowercase)))

main()