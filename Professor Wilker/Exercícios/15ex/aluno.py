class Aluno:
    MEDIA_DE_CORTE = 7.0 # Um atributo de classe para definir a média para aprovação.

    def __init__(self, nome):
        self.nome = nome
        self.notas = [] # O atributo 'notas' é inicializado como uma lista vazia.
    
    def __str__(self):
        """Retorna uma representação em string do objeto Aluno."""
        # A função join é uma forma eficiente de formatar os itens de uma lista.
        notas_str = ", ".join(str(n) for n in self.notas)
        return f"Aluno: {self.nome} | Notas: [{notas_str}]"

    def adicionar_nota(self, nota):
        """Adiciona uma nota à lista do aluno, com validação."""
        # VALIDAÇÃO: Garante que a nota esteja entre 0 e 10.
        if 0 <= nota <= 10:
            self.notas.append(float(nota))
            print(f"Nota {nota} adicionada para {self.nome}.")
            return True
        else:
            print(f"Erro: A nota {nota} é inválida. Deve estar entre 0 e 10.")
            return False

    def calcular_media(self):
        """Calcula a média aritmética das notas do aluno."""
        # Verifica se a lista de notas está vazia para evitar erro de divisão por zero.
        if not self.notas:
            return 0.0
        # 'sum()' e 'len()' são funções nativas do Python para somar e contar itens.
        return sum(self.notas) / len(self.notas)

    # MÉTODO ADICIONADO: Para verificar a situação do aluno.
    def ver_situacao(self):
        """Retorna a situação do aluno (Aprovado/Reprovado) com base na média."""
        media = self.calcular_media()
        if media >= self.MEDIA_DE_CORTE:
            return "Aprovado"
        elif not self.notas:
            return "Indefinido (sem notas)"
        else:
            return "Reprovado"

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    aluno1 = Aluno("Carlos")
    print(f"--- Situação de {aluno1.nome} ---")
    print(aluno1)
    
    # Adicionando notas
    aluno1.adicionar_nota(8.5)
    aluno1.adicionar_nota(9.0)
    aluno1.adicionar_nota(7.0)
    aluno1.adicionar_nota(11) # Tentativa com nota inválida.
    
    print(f"\n{aluno1}")
    
    # Calculando a média e verificando a situação
    media_carlos = aluno1.calcular_media()
    situacao_carlos = aluno1.ver_situacao()
    
    print(f"A média de {aluno1.nome} é {media_carlos:.2f}")
    print(f"Situação: {situacao_carlos}")
    
    print("\n" + "="*30 + "\n")

    aluno2 = Aluno("Beatriz")
    print(f"--- Situação de {aluno2.nome} ---")
    aluno2.adicionar_nota(5.0)
    aluno2.adicionar_nota(6.5)
    
    print(f"\n{aluno2}")
    print(f"A média de {aluno2.nome} é {aluno2.calcular_media():.2f}")
    print(f"Situação: {aluno2.ver_situacao()}")