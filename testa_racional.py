import racional 
import random

lista = []
r1 = racional.Racional()
r2 = racional.Racional(1,0)
r3 = racional.Racional(2,2).simplificar_racional()
r4 = racional.Racional(2,-3)
r5 = racional.Racional(-2,3)
r6 = racional.Racional(-2,-3)
r7 = racional.Racional(3,5)
r8 = racional.Racional(4,7)
soma = r7 + r8
subtracao = r7 - r8
produto = r7 * r8
divisao = r7 / r8

lista.append(r1)
lista.append(r2)
lista.append(r3)
lista.append(r4)
lista.append(r5)
lista.append(r6)
lista.append(r7)
lista.append(r8)

print("r1 =", r1)
print("r2 =", r2)
print("r3 =", r3)
print("r4 =", r4)
print("r5 =", r5)
print("r6 =", r6)
print(30*'--')
print(r7, "+", r8, "=", soma.simplificar_racional())
print(r7, "-", r8, "=", subtracao.simplificar_racional())
print(r7, "*", r8, "=", produto.simplificar_racional())
print(r7, "/", r8, "=", divisao.simplificar_racional())
print(30*'--')
for i in sorted(lista):
    print(i, end=' ')