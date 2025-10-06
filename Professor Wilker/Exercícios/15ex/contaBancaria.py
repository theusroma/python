class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Construtor da classe.
        'saldo_inicial=0' define um valor padrão caso nenhum seja fornecido.
        """
        self.titular = titular
        # O prefixo '_' indica um atributo "protegido", uma convenção para
        # sinalizar que ele não deve ser alterado diretamente fora da classe.
        self._saldo = float(saldo_inicial)

    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta."""
        if valor > 0:
            self._saldo += valor # '+=' é um atalho para 'self._saldo = self._saldo + valor'.
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Erro: O valor do depósito deve ser positivo.")
            return False
    
    def sacar(self, valor):
        """Retira um valor do saldo, se houver fundos suficientes."""
        # Valida se o valor é positivo E se há saldo suficiente.
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print(f"Falha ao sacar R$ {valor:.2f}. Saldo insuficiente ou valor inválido.")
            return False
    
    def ver_saldo(self):
        """Exibe o saldo atual formatado."""
        print(str(self)) # Reutiliza a lógica do método __str__

    def __str__(self):
        """Retorna a representação em string do objeto."""
        return f"Conta de {self.titular} | Saldo: R$ {self._saldo:.2f}"

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    # Cria uma instância de ContaBancaria para "Ana" com saldo inicial de 500.
    conta_ana = ContaBancaria("Ana", 500)
    print(f"Situação inicial: {conta_ana}\n")
    
    print("--- Realizando operações ---")
    conta_ana.depositar(150)
    
    # Tentativa de saque inválida (valor maior que o saldo).
    conta_ana.sacar(1000)
    
    # Saque válido.
    conta_ana.sacar(200)
    
    print("\n--- Situação Final ---")
    # Exibe o saldo final chamando o método ver_saldo.
    conta_ana.ver_saldo()