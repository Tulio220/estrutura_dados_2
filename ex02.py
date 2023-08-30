"""
Escreva um programa que remova todos os elementos de uma lista que também estão presentes em outra lista.
A = [4,5,2,3,1,2,5] = {1,2,3,4,5}
B = [3,1,5,8,9] = {1,3,5,8,9}

Resultado = {2,4}
"""
listaA = [4,5,2,3,1,2,5]
ListaB = [3,1,5,8,9]

listaA = set(listaA)
ListaB = set(ListaB)
print(listaA.difference(ListaB))   



