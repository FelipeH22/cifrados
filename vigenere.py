import string

def proceso(metodo,cadena,key,alfabeto): 
    if metodo==1: return "".join([alfabeto[(alfabeto.index(cadena[i])+alfabeto.index(key[i]))%len(alfabeto)] for i in range(len(cadena))]).upper()
    else: return "".join([alfabeto[(alfabeto.index(cadena[i])-alfabeto.index(key[i]))%len(alfabeto)] for i in range(len(cadena))]).upper()

def main():
    if int(input("¿Con números? --> 1; 0 e.o.c. \n"))==1:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n").lower(),input("Digite la llave \n"),list(string.ascii_lowercase)+[str(x) for x in range(10)]))
    else:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n").lower(),input("Digite la llave \n"),list(string.ascii_lowercase)))

main()