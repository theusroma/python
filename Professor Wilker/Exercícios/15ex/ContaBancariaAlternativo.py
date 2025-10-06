# Define a classe 'ContaBancaria', um molde para criar contas.
class ContaBancaria:
    """
    Representa uma conta bancária com funcionalidades de depósito,
    saque e consulta de saldo.
    """
    
    # Define o método construtor. 'saldo_inicial=0' significa que se nenhum valor for passado,
    # o saldo começará com 0.
    def __init__(self, saldo_inicial=0):
        # 'self.__saldo' cria um atributo de instância.
        # Os dois underlines no início ('__') o tornam "privado", indicando
        # que ele não deve ser acessado diretamente de fora da classe.
        self.__saldo = float(saldo_inicial)

    # Define o método 'depositar', que recebe um 'valor' para adicionar ao saldo.
    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta, se o valor for positivo."""
        # 'if valor > 0:' verifica se o valor a ser depositado é positivo.
        if valor > 0:
            # 'self.__saldo += valor' adiciona o valor ao saldo atual.
            self.__saldo += valor
            # Imprime uma mensagem de confirmação, formatando o valor para duas casas decimais.
            print(f"Depósito de R$ {valor:.2f} realizado.")
        # 'else:' executa se a condição do 'if' for falsa.
        else:
            # Informa ao usuário que o valor fornecido é inválido.
            print("Valor de depósito inválido.")

    # Define o método 'sacar', que recebe um 'valor' a ser retirado do saldo.
    def sacar(self, valor):
        """Retira um valor do saldo, se houver fundos e o valor for válido."""
        # 'if valor > self.__saldo:' verifica se o valor do saque é maior que o saldo disponível.
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        # 'elif valor > 0:' se a primeira condição for falsa, verifica se o valor do saque é positivo.
        elif valor > 0:
            # 'self.__saldo -= valor' subtrai o valor do saldo.
            self.__saldo -= valor
            # Imprime uma mensagem de confirmação do saque.
            print(f"Saque de R$ {valor:.2f} realizado.")
        # 'else:' executa se nenhuma das condições anteriores for verdadeira.
        else:
            print("Valor de saque inválido.")

    # Define o método 'ver_saldo' para exibir o estado atual da conta.
    def ver_saldo(self):
        """Exibe o saldo atual da conta."""
        # Imprime o valor do atributo privado '__saldo', formatado como moeda.
        print(f"Saldo atual: R$ {self.__saldo:.2f}")


# --- Exemplo de uso ---
if __name__ == "__main__":
    
    # Cria um objeto da classe ContaBancaria com saldo inicial de 100.
    minha_conta = ContaBancaria(100)
    
    # Chama o método para ver o saldo inicial.
    minha_conta.ver_saldo()
    
    print("-" * 25) # Separador para clareza
    
    # Chama o método para depositar 50.
    minha_conta.depositar(50)
    
    # Chama o método para sacar 30.
    minha_conta.sacar(30)
    
    # Tenta sacar 200. Como o saldo é insuficiente, esta operação falhará.
    minha_conta.sacar(200)

    print("-" * 25) # Separador para clareza
    
    # Mostra o saldo final após todas as operações.
    minha_conta.ver_saldo()