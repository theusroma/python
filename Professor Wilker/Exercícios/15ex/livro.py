# Define o molde para objetos 'Livro'.
class Livro:
    # O método __init__ é o construtor da classe. Ele é chamado
    # automaticamente quando um novo objeto é criado.
    def __init__(self, titulo, autor, paginas):
        # Atributos de instância: cada objeto 'Livro' terá sua própria cópia destes dados.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # MÉTODO ADICIONADO: __str__
    # Este método especial retorna uma representação em string do objeto.
    # É o que o `print()` usa por padrão para exibir o objeto.
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, {self.paginas} páginas."

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    # 1. Criando instâncias (objetos) da classe Livro.
    #    Cada chamada a Livro() executa o método __init__.
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
    livro2 = Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 208)

    # 2. Acessando os atributos dos objetos diretamente.
    print("--- Acessando atributos individualmente ---")
    print(f"Título do Livro 1: {livro1.titulo}")
    print(f"Autor do Livro 2: {livro2.autor}\n")

    # 3. Imprimindo os objetos.
    #    O Python automaticamente chama o método __str__ que definimos.
    print("--- Exibindo informações completas usando print() ---")
    print(f"Livro 1: {livro1}")
    print(f"Livro 2: {livro2}")