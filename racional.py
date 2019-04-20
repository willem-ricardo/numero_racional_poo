import matematica as mat

class Racional:
    ### Construtor    
    def __init__(self, p=0, q=1):
        if q != 0:
            if q < 0:
                p = -p
                q = -q
            if q == 0:
                q = 1
            self.__p = p
            self.__q = q
        else:
            self.__p = 0
            self.__q = 1
            
    
    ### Métodos de acesso
    def get_p(self):
        return self.__p
    
    def get_q(self):
        return self.__q
    
    
    ### Métodos de modificação
    def set_p(self, novo_p):
        self.__p = novo_p
        
    def set_q(self, novo_q):
        if novo_q != 0:
            if novo_q < 0:
                novo_q = -novo_q
                self.__p = -self.__p
            self.__q = novo_q
    
    
    ### Métodos utilitários
    def simplificar_racional(self):
        m = mat.mdc(self.__p, self.__q)
        p = self.__p // m
        q = self.__q // m
        return Racional(p, q)
        
    def __add__(self, outro):
        p = self.__p * outro.__q + self.__q * outro.__p
        q = self.__q * outro.__q
        return Racional(p,q)
    
    def __sub__(self, outro):
        p = self.__p * outro.__q - self.__q * outro.__p
        q = self.__q * outro.__q
        return Racional(p, q)
    
    def __mul__(self, outro):
        p = self.__p * outro.__p
        q = self.__q * outro.__q
        return Racional(p, q)
        
    def __truediv__(self, outro):
        p = self.__p * outro.__q
        q = self.__q * outro.__p
        return Racional(p, q)
    
    # Método de exibição
    def __str__(self):
        if self.__q == 1:
            return "{:d}".format(self.__p)
        else:
            return "{:d}/{:d}".format(self.__p, self.__q)

    # Métodos de comparação
    def __eq__(self, outro):
        return self.__p * outro.__q == self.__q * outro.__p

    def __ne__(self, outro):
        return self.__p * outro.__q != self.__q * outro.__p

    def __lt__(self, outro):
        return self.__p * outro.__q < self.__q * outro.__p

    def __le__(self, outro):
        return self.__p * outro.__q <= self.__q * outro.__p
    def __lt__(self, outro):
        return self.__p * outro.__q < self.__q * outro.__p

    def __gt__(self, outro):
        return self.__p * outro.__q > self.__q * outro.__p

    def __ge__(self, outro):
        return self.__p * outro.__q >= self.__q * outro.__p
                
            
        
        
    
    
            
        