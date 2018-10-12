from Node import *

class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.cont = 0

    def imprimir(self, node = None):
        if self.isEmpty():
            print("Árvore vazia")
        else:
            if node == None:
                node = self.raiz
            print(node.info)
            if node.se:
                self.imprimir(node.se)
            if node.sd:
                self.imprimir(node.sd)

    def isEmpty(self):
        return True if not self.raiz else False

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

    def remover(self,info):
        info = int(info)
        aux = self.raiz
        p = self.raiz
        while ((info != p.info) and (aux != None)):
            p = aux
            if (info< p.info):
                aux = p.se
            else:
                aux = p.sd
        if (p and p.info == info):
            nopai = p.pai
            if (p.se == None and p.sd == None):
                if (nopai.se == p):
                    nopai.se = None
                else:
                    nopai.sd = None
            elif (p.se != None and p.sd == None):
                orfesq = p.se
                if (nopai.se == p):
                    nopai.se = orfesq
                else:
                    nopai.sd = orfesq
                orfesq.pai = nopai
            elif (p.se == None and p.sd != None):
                orfdir = p.sd
                if (nopai.se == p):
                    nopai.se = orfdir
                else:
                    nopai.sd = orfdir
                orfdir.pai = nopai
            elif (p.se != None and p.sd != None):
                orfesq = p.se
                orfdir = p.sd
                if (nopai.se == p):
                    nopai.se = orfesq
                    orfesq.pai = nopai
                    self.realocar(orfesq, orfdir)
                else:
                    nopai.sd = orfdir
                    orfdir.pai = nopai
                    self.realocar(orfdir, orfesq)

    def realocar (self, orf1, orf2):
        info = orf2.info
        aux = orf1
        p = self.raiz
        while ((info != p.info) and (aux != None)):
            p = aux
            if (info< p.info):
                aux = p.se
            else:
                aux = p.sd
        if (info < p.info):
            p.se = orf2
        else:
            p.sd = orf2
        orf2.pai = p

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
        """
        Verifica matematicamente se a árvore é binária completa
        Sabendo que 2 elevado a altura da árvore + 1 é igual a quantidade nós da árvore + 1
        """
        if ((self.cont + 1) == (2 ** (self.altura() + 1))):
            return True
        else:
            return False

    def consultaGrau(self, info):
        """Consulta o grau de determinado nó através do seu valor"""
        p = self.pesquisar(info)
        if (p):
            return p.grau()
        else:
            return None

    def isBalanceada(self, node = None):
        if node == None:
            node = self.raiz 
        if not node.isBalanceado():
            return False
        else:
            if node.se:
                self.isBalanceada(node.se)
            if node.sd:
                self.isBalanceada(node.sd)
        return True

    def isEstritamente(self, node = None):
        if node == None:
            node = self.raiz
        if (node):
            if node.se == None and node.sd == None:
                return True
            if node.se and node.sd:
                return self.isEstritamente(node.se) and self.isEstritamente(node.sd)
        return False
