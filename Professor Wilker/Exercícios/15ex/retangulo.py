class Retangulo:
    def __init__(self, largura, altura):
        # 1. VALIDAÇÃO ADICIONADA: Garante que as dimensões sejam válidas.
        if largura <= 0 or altura <= 0:
            raise ValueError("A largura e a altura devem ser números positivos.")
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        """Retorna o produto da largura pela altura."""
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        """Retorna a soma de todos os lados do retângulo."""
        return 2 * (self.largura + self.altura)

    # 2. MÉTODO ADICIONADO: Para representação em string.
    def __str__(self):
        """Retorna uma descrição textual do objeto."""
        return f"Retângulo(largura={self.largura}, altura={self.altura})"

    # 3. MÉTODO ADICIONADO: Para verificar se é um quadrado.
    def eh_quadrado(self):
        """Retorna True se a largura for igual à altura, False caso contrário."""
        return self.largura == self.altura

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    print("--- Criando um retângulo (10x5) ---")
    # Cria uma instância da classe.
    r1 = Retangulo(10, 5)
    
    # Imprime o objeto diretamente, usando o método __str__
    print(f"Objeto: {r1}")

    # Chama os métodos e imprime os valores retornados.
    print(f"Área: {r1.calcular_area()}")
    print(f"Perímetro: {r1.calcular_perimetro()}")
    print(f"É um quadrado? {r1.eh_quadrado()}")

    print("\n" + "="*30 + "\n")

    print("--- Criando um quadrado (7x7) ---")
    q1 = Retangulo(7, 7)
    print(f"Objeto: {q1}")
    print(f"Área: {q1.calcular_area()}")
    print(f"Perímetro: {q1.calcular_perimetro()}")
    print(f"É um quadrado? {q1.eh_quadrado()}")

    print("\n" + "="*30 + "\n")

    print("--- Tentando criar um retângulo inválido ---")
    try:
        r_invalido = Retangulo(-5, 10)
    except ValueError as e:
        print(f"Erro ao criar objeto: {e}")