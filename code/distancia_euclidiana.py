# O que é classe:
# Um conjunto de objetos
class DistanciaEuclidiana:
    """
      atributos e construtor
    """
    # Joaquim chegou na feira do Goianos e quer comprar roupas o ponto de localização do Joaquim é (2, 3) e o ponto de localização do Box do Goianos é (5, 7). Qual é a distância entre os dois pontos?"
    # construtor padrão (se o programador não criar um construtor, o Python cria um construtor padrão)
    # O construtor padrão é automático
    # O contrutor com parâmetros é criado pelo programador
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1        

    """Método Especial"""
    def __str__(self):
        return f"(ponto1={self.x1},ponto2={self.y2})"
    
    """Método Workers"""
    def calcular_distancia(self,x2, y2):
        # passo 1 - diferença horizontal - eixo X
        

        # passo 2 - diferença vertical - eixo Y

        # passo 3 - teorema de Pitágoras
        return 0
    def calcular_distancia_completa(self, x2, y2):
        pass