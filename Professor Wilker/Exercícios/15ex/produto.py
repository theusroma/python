class Produto:
    def __init__(self, nome, preco, estoque=0):
        # VALIDAÇÃO: Garante que preço e estoque não sejam negativos.
        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque não podem ser negativos.")
        self.nome = nome
        self.preco = float(preco)
        self.estoque = int(estoque)

    def __str__(self):
        """Retorna uma representação em string do produto."""
        return f"{self.nome} - R$ {self.preco:.2f} | Estoque: {self.estoque} unidades"

    def aplicar_desconto(self, porcentagem):
        """
        Calcula e retorna o preço com um desconto aplicado.
        Não altera o preço original do produto.
        """
        # VALIDAÇÃO: Garante que o desconto seja um valor plausível.
        if not 0 <= porcentagem <= 100:
            print("Erro: A porcentagem de desconto deve estar entre 0 e 100.")
            return self.preco # Retorna o preço original em caso de erro.
        
        desconto = self.preco * (porcentagem / 100)
        return self.preco - desconto

    # MÉTODO ADICIONADO: Para simular a venda de produtos.
    def vender(self, quantidade=1):
        """Decrementa o estoque se houver quantidade suficiente."""
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"Venda de {quantidade} unidade(s) de '{self.nome}' realizada.")
            return True
        else:
            print(f"Falha na venda: estoque insuficiente ou quantidade inválida.")
            return False

    # MÉTODO ADICIONADO: Para repor o estoque.
    def repor_estoque(self, quantidade):
        """Incrementa o estoque do produto."""
        if quantidade > 0:
            self.estoque += quantidade
            print(f"{quantidade} unidade(s) de '{self.nome}' adicionada(s) ao estoque.")
            return True
        else:
            print("Erro: A quantidade para reposição deve ser positiva.")
            return False

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    # Cria a instância do produto.
    notebook = Produto("Notebook Gamer", 5000, 10)
    print(f"Estado inicial: {notebook}\n")

    # 1. Calcula o preço com desconto.
    print("--- Calculando desconto ---")
    preco_com_desconto = notebook.aplicar_desconto(15)
    print(f"Preço original: R$ {notebook.preco:.2f}")
    print(f"Preço com 15% de desconto: R$ {preco_com_desconto:.2f}")
    print(f"O estoque permanece o mesmo: {notebook.estoque} unidades\n")

    # 2. Simula uma venda.
    print("--- Simulando vendas ---")
    notebook.vender(3)
    notebook.vender(10) # Tentativa de venda com estoque insuficiente.
    print(f"Estado após vendas: {notebook}\n")

    # 3. Repõe o estoque.
    print("--- Repondo estoque ---")
    notebook.repor_estoque(5)
    print(f"Estado final: {notebook}")