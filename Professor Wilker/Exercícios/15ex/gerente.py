# Superclasse (classe-base)
class Funcionario:
    def __init__(self, nome, salario):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.nome = nome
        self.salario = float(salario)
    
    # MÉTODO ADICIONADO: para exibir os dados básicos do funcionário.
    def exibir_dados(self):
        """Imprime as informações básicas do funcionário."""
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R$ {self.salario:.2f}")

# Subclasse (herda de Funcionario)
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        # Invoca o construtor da superclasse (Funcionario) para inicializar nome e salario.
        super().__init__(nome, salario)
        
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        # Inicializa o atributo específico da subclasse.
        self.bonus = float(bonus)
    
    def salario_total(self):
        """Calcula o salário total somando o salário base e o bônus."""
        # Acessa o atributo herdado 'self.salario' e o próprio 'self.bonus'.
        return self.salario + self.bonus

    # MÉTODO SOBRESCRITO: para incluir a informação do bônus.
    def exibir_dados(self):
        """
        Chama o método original da classe-pai e depois adiciona
        as informações específicas do gerente.
        """
        print("--- Dados do Gerente ---")
        super().exibir_dados() # Chama Funcionario.exibir_dados()
        print(f"Bônus: R$ {self.bonus:.2f}")

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    # Criando uma instância da subclasse Gerente.
    gerente = Gerente("Maria", 7000, 1500)
    
    # Usando o novo método para exibir todas as informações de forma organizada.
    gerente.exibir_dados()
    
    print("-" * 25)
    
    # Usando o método para calcular e imprimir o salário total.
    salario_final = gerente.salario_total()
    print(f"O salário total da gerente {gerente.nome} é R$ {salario_final:.2f}")

    print("\n" + "="*25 + "\n")

    # Criando uma instância da classe-pai para comparação.
    funcionario_comum = Funcionario("João", 3000)
    print("--- Dados do Funcionário Comum ---")
    funcionario_comum.exibir_dados()