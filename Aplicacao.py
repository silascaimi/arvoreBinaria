from ArvoreBinaria import *
from Node import *
          
a1 = ArvoreBinaria()
a1.inserir(20)
a1.inserir(10)
a1.inserir(30)
a1.inserir(5)
a1.inserir(15)
a1.inserir(25)
a1.inserir(40)

#print(a1.consultaGrau(20))

arvore = a1

print("A ávore possui altura: {}".format(arvore.altura()))
print("Está Balanceada" if arvore.isAVL() else "Não está Balanceada")
print("É estritamente Binária" if arvore.isEstritamente() else "Não é estritamente Binária")
print("É Binária Completa" if arvore.isBinariaCompleta() else "Não é Binária Completa")



