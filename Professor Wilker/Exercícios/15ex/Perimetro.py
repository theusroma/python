# Define a classe 'Retangulo'.
class Retangulo:
    """
    Representa um retângulo e calcula sua área e perímetro.
    """
    
    # O construtor recebe 'base' e 'altura' e os armazena como atributos do objeto.
    def __init__(self, base, altura):
        # VALIDAÇÃO: Garante que os valores de base e altura sejam positivos.
        if base <= 0 or altura <= 0:
            raise ValueError("A base e a altura devem ser números positivos.")
        self.base = base
        self.altura = altura
    
    # Adiciona uma representação em string para o objeto.
    def __str__(self):
        """Retorna uma representação textual do objeto."""
        return f"Retângulo(base={self.base}, altura={self.altura})"

    # Define o método para calcular a área.
    def calcular_area(self):
        """
        Calcula a área do retângulo.
        A fórmula da área é base multiplicada pela altura.
        """
        # 'return' envia o resultado do cálculo de volta para quem chamou o método.
        return self.base * self.altura

    # Define o método para calcular o perímetro.
    def calcular_perimetro(self):
        """
        Calcula o perímetro do retângulo.
        A fórmula é 2 * (base + altura).
        """
        # Retorna o resultado do cálculo do perímetro.
        return 2 * (self.base + self.altura)

# --- Exemplo de uso ---
if __name__ == "__main__":
    
    # Cria um objeto da classe Retangulo com base 10 e altura 5.
    meu_retangulo = Retangulo(10, 5)
    
    # Imprime a representação do objeto usando o método __str__.
    print(f"Objeto criado: {meu_retangulo}")
    
    # Chama o método 'calcular_area()' e insere o valor retornado na string de impressão.
    print(f"Área: {meu_retangulo.calcular_area()}")
    
    # Chama o método 'calcular_perimetro()' e insere o valor retornado na string de impressão.
    print(f"Perímetro: {meu_retangulo.calcular_perimetro()}")

    print("\n--- Tentando criar um retângulo inválido ---")
    try:
        retangulo_invalido = Retangulo(-5, 10)
    except ValueError as e:
        print(f"Erro: {e}")
