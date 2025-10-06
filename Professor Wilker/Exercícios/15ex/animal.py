# Superclasse (ou classe-mãe)
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        """Método genérico a ser sobrescrito pelas subclasses."""
        return "O animal emite um som."

# Subclasse 1: Gato
class Gato(Animal): # 'Gato' herda de 'Animal'.
    def falar(self): # Sobrescreve o método 'falar' da classe Animal.
        return "Miau!"

# Subclasse 2: Cachorro
class Cachorro(Animal): # 'Cachorro' também herda de 'Animal'.
    def falar(self):
        """
        Sobrescreve E ESTENDE o método 'falar' da classe Animal.
        A função super() chama o método da classe-pai (Animal.falar).
        """
        som_base = super().falar()
        return f"{som_base} Especificamente, ele late: Au au!"

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":

    # Instância da classe-mãe
    animal_generico = Animal("Criatura")
    
    # Instâncias das subclasses
    rex = Cachorro("Rex")
    felix = Gato("Felix")
    
    # Chamando o método 'falar' para cada objeto
    print(f"{animal_generico.nome}: {animal_generico.falar()}")
    print(f"{felix.nome}: {felix.falar()}") # Executa o método sobrescrito de Gato
    print(f"{rex.nome}: {rex.falar()}")   # Executa o método estendido de Cachorro