import numpy as np
import string
import sympy

def proceso(metodo,cadena,key,alfabeto):
    size=int(len(key.split(","))**(1/2))
    result=list()
    cadena=cadena.lower()
    key=np.array([int(x.strip()) for x in key.split(",")]).reshape((size,size))
    for i in range(0,len(cadena),size):
        vector=np.array([alfabeto.index(x) for x in cadena[i:i+size]])
        if metodo==1: mul=(vector@key)%len(alfabeto)
        else:
            deter=int(np.linalg.det(key)%len(alfabeto))
            det_inv=pow(deter,-1,len(alfabeto))
            m=sympy.Matrix(key)
            cofactor=np.asarray(m.adjugate().T)
            inversa=(det_inv*cofactor).T%len(alfabeto)
            mul=(vector@inversa)%len(alfabeto)
        result.append("".join([alfabeto[int(x)] for x in mul]))
    return "".join(result).upper()

def main():
    if int(input("¿Con números? --> 1; 0 e.o.c. \n"))==1:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n"),input("Digite la llave separada por comas \n"),list(string.ascii_lowercase)+[str(x) for x in range(10)]))
    else:
        print(proceso(int(input("1. Encriptar; 2. Desencriptar\n")),input("Digite la cadena \n"),input("Digite la llave separada por comas \n"),list(string.ascii_lowercase)))

main()