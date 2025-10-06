# Define a classe 'Cachorro'.
class Cachorro:
    """
    Representa um cachorro e utiliza um atributo de classe
    para contar o número total de instâncias criadas.
    """
    
    # 'numero_de_cachorros = 0' é um ATRIBUTO DE CLASSE.
    # Ele pertence à classe como um todo, não a um objeto individual.
    # Será compartilhado por todas as instâncias da classe.
    numero_de_cachorros = 0

    # O construtor é chamado toda vez que um novo cachorro é criado.
    def __init__(self, nome):
        # 'self.nome = nome' é um ATRIBUTO DE INSTÂNCIA, único para cada cachorro.
        self.nome = nome
        
        # 'Cachorro.numero_de_cachorros += 1' incrementa o atributo da CLASSE.
        # Usamos 'Cachorro.' para garantir que estamos acessando o atributo de classe.
        # Isso garante que o contador aumente a cada novo objeto criado.
        Cachorro.numero_de_cachorros += 1

    # MÉTODO DE CLASSE ADICIONADO:
    # O decorador '@classmethod' indica que este método opera na classe, não na instância.
    # Ele recebe a própria classe ('cls') como primeiro argumento, em vez de 'self'.
    @classmethod
    def get_total_cachorros(cls):
        """Retorna o valor do atributo de classe 'numero_de_cachorros'."""
        return cls.numero_de_cachorros

# --- Exemplo de uso ---
if __name__ == "__main__":
    
    # Imprime o valor do atributo de classe ANTES de qualquer objeto ser criado.
    # Podemos acessá-lo diretamente pela classe.
    print(f"Cachorros criados (antes): {Cachorro.numero_de_cachorros}")
    
    print("\n--- Criando cachorros ---")
    # 'c1 = Cachorro("Rex")' cria a primeira instância. O __init__ é chamado e o contador vai para 1.
    c1 = Cachorro("Rex")
    print(f"'{c1.nome}' foi criado.")
    
    # 'c2 = Cachorro("Totó")' cria a segunda instância. O __init__ é chamado e o contador vai para 2.
    c2 = Cachorro("Totó")
    print(f"'{c2.nome}' foi criado.")

    print("\n--- Verificando o total ---")
    
    # Imprime o valor final do atributo de classe, que agora é 2.
    # Acessando diretamente pela classe:
    print(f"Total (acesso direto): {Cachorro.numero_de_cachorros}")
    
    # Também podemos acessar o atributo de classe através de uma instância.
    # O valor será o mesmo, pois é compartilhado.
    print(f"Total (acesso via instância c1): {c1.numero_de_cachorros}")

    # Usando o método de classe que criamos. Esta é a forma mais elegante.
    print(f"Total (via classmethod): {Cachorro.get_total_cachorros()}")
