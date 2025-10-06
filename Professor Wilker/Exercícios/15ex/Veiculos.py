# Define a classe 'Veiculo', que servirá como classe mãe (ou superclasse).
class Veiculo:
    """
    Representa um veículo genérico com marca e modelo.
    """
    # Construtor da classe mãe, que inicializa 'marca' e 'modelo'.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método que pertence à classe Veiculo e será herdado por suas filhas.
    def acelerar(self):
        """Exibe uma mensagem genérica de aceleração."""
        print(f"O {self.modelo} está acelerando!")

# Define a classe 'Moto', que herda da classe 'Veiculo'.
# A sintaxe 'Moto(Veiculo)' estabelece a relação de herança.
class Moto(Veiculo):
    """
    Representa uma Moto, que é um tipo de Veiculo com cilindradas
    e um comportamento específico de 'empinar'.
    """
    # Construtor da classe filha 'Moto'.
    def __init__(self, marca, modelo, cilindradas):
        # 'super().__init__(marca, modelo)' chama o construtor da classe mãe (Veiculo).
        # Isso é essencial para garantir que os atributos 'marca' e 'modelo' sejam inicializados.
        super().__init__(marca, modelo)
        
        # 'self.cilindradas = cilindradas' inicializa um atributo que é específico da classe Moto.
        self.cilindradas = cilindradas

    # Define o método 'empinar', que é exclusivo da classe Moto.
    def empinar(self):
        """Exibe uma mensagem específica da ação de empinar a moto."""
        print(f"A {self.modelo} de {self.cilindradas}cc está empinando! Uau!")

# CLASSE ADICIONADA: Outra classe que herda de Veiculo.
class Carro(Veiculo):
    """
    Representa um Carro, que é um tipo de Veiculo com um número de portas
    e um comportamento específico de 'abrir_porta_malas'.
    """
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def abrir_porta_malas(self):
        """Exibe uma mensagem específica da ação de abrir o porta-malas."""
        print(f"O porta-malas do {self.modelo} foi aberto.")

# --- Exemplo de uso ---
if __name__ == "__main__":
    
    print("--- Testando a Moto ---")
    # Cria um objeto 'minha_moto' da classe Moto.
    minha_moto = Moto("Honda", "CB 500", 500)
    
    # Acessa e imprime os atributos 'marca' e 'modelo' que foram herdados.
    print(f"Moto: {minha_moto.marca} {minha_moto.modelo}")
    
    # Chama o método 'acelerar()'. Este método não está em Moto, mas é herdado de Veiculo.
    minha_moto.acelerar()
    
    # Chama o método 'empinar()', que é um método específico da classe Moto.
    minha_moto.empinar()

    print("\n" + "="*25 + "\n")

    print("--- Testando o Carro ---")
    # Cria um objeto 'meu_carro' da classe Carro.
    meu_carro = Carro("Toyota", "Corolla", 4)
    
    # Acessa os atributos herdados.
    print(f"Carro: {meu_carro.marca} {meu_carro.modelo}")
    
    # Chama o método herdado 'acelerar()'.
    meu_carro.acelerar()
    
    # Chama o método específico 'abrir_porta_malas()'.
    meu_carro.abrir_porta_malas()