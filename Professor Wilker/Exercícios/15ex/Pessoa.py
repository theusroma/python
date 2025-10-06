# A palavra-chave 'class' inicia a definição de uma nova classe chamada 'Pessoa'.
# Uma classe é um "molde" para criar objetos.
class Pessoa:
    """
    Representa uma pessoa com nome e idade, e sabe como se apresentar.
    """
    
    # 'def __init__(self, nome, idade):' define o método construtor da classe.
    # Este método é chamado automaticamente sempre que um novo objeto da classe é criado.
    # 'self' é uma referência à instância do objeto que está sendo criada.
    # 'nome' e 'idade' são os parâmetros que o construtor receberá.
    def __init__(self, nome, idade):
        
        # 'self.nome = nome' cria um atributo de instância chamado 'nome'.
        # Ele armazena o valor do parâmetro 'nome' dentro do objeto 'self'.
        self.nome = nome
        
        # 'self.idade = idade' cria um atributo de instância chamado 'idade'.
        # Ele armazena o valor do parâmetro 'idade' dentro do objeto 'self'.
        self.idade = idade

    # 'def apresentar(self):' define um método chamado 'apresentar'.
    # Métodos são funções que pertencem a uma classe e operam nos dados do objeto.
    # 'self' permite que este método acesse os atributos do objeto (como self.nome).
    def apresentar(self):
        """
        Exibe uma mensagem de apresentação usando os atributos do objeto.
        """
        # 'print(...)' é uma função que exibe uma mensagem na tela.
        # O 'f' antes das aspas indica uma "f-string", que facilita a inserção de variáveis.
        # '{self.nome}' e '{self.idade}' inserem os valores dos atributos do objeto na string.
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# --- Criando um objeto e usando o método ---
# A boa prática é colocar o código que será executado dentro deste bloco.
if __name__ == "__main__":
    
    # 'pessoa1 = Pessoa("Carlos", 30)' cria uma nova instância (objeto) da classe Pessoa.
    # "Carlos" é passado como o argumento 'nome' e 30 como 'idade' para o construtor __init__.
    # O novo objeto é armazenado na variável 'pessoa1'.
    pessoa1 = Pessoa("Carlos", 30)
    
    # 'pessoa1.apresentar()' chama o método 'apresentar' do objeto 'pessoa1'.
    # O método usará os atributos ('Carlos' e 30) que foram definidos quando o objeto foi criado.
    pessoa1.apresentar()

    # Podemos criar outros objetos a partir do mesmo molde.
    pessoa2 = Pessoa("Ana", 25)
    pessoa2.apresentar()