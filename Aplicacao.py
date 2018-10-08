from ArvoreBinaria import *
from Node import *
          
a1 = ArvoreBinaria()
a1.inserir(20)
a1.inserir(10)
a1.inserir(30)


#print(a1.consultaGrau(4))

arvore = a1

print("Balanceada" if arvore.isBalanceada() else "Não está Balanceada")
print("Binária Completa" if arvore.isBinariaCompleta() else "Não é Binária Completa")