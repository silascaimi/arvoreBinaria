class Node:
    def __init__(self, info, pai = None, se = None, sd = None):
        self.info = info
        self.pai = pai
        self.se = se
        self.sd = sd

    def __str__(self):
        return str(self.valor)

    def print(self):
        print(self.info)
        if(self.se):
            self.se.print()
        if(self.sd):
            self.sd.print()

    def grau(self):
        g = 0
        if (self.se):
            g += 1
        if (self.sd):
            g += 1
        return g

    def pesoEsq(self):
        e = 0
        if (self):
            if (self.se):
                e += 1
                e += self.se.pesoEsq()
        else:
            raise Exception("Nó inexistente")
        return e

    def pesoDir(self):
        d = 0
        if (self):
            if (self.sd):
                d += 1
                d += self.sd.pesoDir()
        else:
            raise Exception("Nó inexistente")
        return d

    def nivel(self):
        if (self.pesoEsq() > self.pesoDir()):
            return self.pesoEsq()
        return self.pesoDir()

    def fatBal(self):
        return self.pesoDir() - self.pesoEsq()


