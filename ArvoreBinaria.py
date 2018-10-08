from Node import *

class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.cont = 0

    def print(self):
        self.raiz.print()

    def isEmpty(self):
        if self.raiz == None:
            return True
        else:
            return False

    def inserir(self, info):
        if self.isEmpty():
            self.raiz = Node(info)
            self.cont += 1
        else:
            aux = self.raiz
            p = self.raiz

            while ((info != p.info) and (aux != None)):
                p = aux
                if (info < p.info):
                    aux = p.se
                else:
                    aux = p.sd
            if (info == p.info):
                print ("Informação Repetida")
            elif (info < p.info):
                p.se = Node(info, p)
                self.cont += 1
            elif (info > p.info):
                p.sd = Node(info, p )
                self.cont += 1

    def pesquisar(self, info):
        aux = self.raiz
        p = self.raiz
        while(info != p.info and aux != None):
            p = aux
            if (info < p.info):
                aux = p.se
            else:
                aux = p.sd
        if (p != None and info == p.info):
            return p
        else:
            return None

    def altura(self):
        if (self.isEmpty()):
            raise Exception("Árvore inexistente")
        return self.raiz.nivel()

    def isBinariaCompleta(self):
        if ((self.cont + 1) == (2 ** (self.altura() + 1))):
            return True
        else:
            return False

    def consultaGrau(self, info):
        p = self.pesquisar(info)
        if (p):
            return p.grau()
        else:
            return None

     #necessario correcao
    def isBalanceada(self):
        aux = self.raiz
        if ():
            return False
        else:
            return True
