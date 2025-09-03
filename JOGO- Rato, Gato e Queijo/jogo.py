import copy

# --- Configuração das Regras e Hóspedes ---

# Dicionário de regras de vizinhança entre os hóspedes.
# A chave representa um hóspede e a lista associada contém os hóspedes
# com os quais ele não pode ser vizinho (acima, abaixo, esquerda ou direita).
REGRAS_DE_VIZINHANCA = {
    'R': ['G', 'Q'],  # Rato não pode ficar ao lado de Gato ou Queijo.
    'G': ['R', 'C'],  # Gato não pode ficar ao lado de Rato ou Cão.
    'C': ['O', 'G'],  # Cão não pode ficar ao lado de Osso ou Gato.
    'O': ['C'],       # Osso não pode ficar ao lado de Cão.
    'Q': ['R']        # Queijo não pode ficar ao lado de Rato.
}

# Dicionário que mapeia a abreviação do hóspede para seu nome completo.
HOSPEDES_INFO = {
    'G': 'GATO',
    'C': 'CÃO',
    'R': 'RATO',
    'O': 'OSSO',
    'Q': 'QUEIJO'
}

# Lista de dicionários, onde cada dicionário representa uma fase do jogo.
# Cada fase tem um nome, um layout de tabuleiro e os hóspedes a serem alocados.
# ' ' representa um quarto livre e '#' um quarto indisponível.
FASES_DO_JOGO = [
    {
        "nome": "Fase 1",
        "tabuleiro": [
            [' ', '#'],
            [' ', ' ']
        ],
        "hospedes_para_alocar": ['R', 'G']
    },
    {
        "nome": "Fase 2",
        "tabuleiro": [
            [' ', ' ', ' '],
            ['#', ' ', ' ']
        ],
        "hospedes_para_alocar": ['C', 'C', 'O']
    },
    {
        "nome": "Fase 3",
        "tabuleiro": [
            [' ', '#'],
            [' ', ' '],
            [' ', ' ']
        ],
        "hospedes_para_alocar": ['G', 'R', 'O']
    },
    {
        "nome": "Fase 4",
        "tabuleiro": [
            [' ', ' ', '#'],
            ['#', ' ', ' '],
            [' ', '#', ' ']
        ],
        "hospedes_para_alocar": ['Q', 'Q', 'O']
    }
]

# --- Funções do Jogo ---

def exibir_tabuleiro(tabuleiro_atual):
    """Exibe o tabuleiro do jogo de forma clara e formatada."""
    num_colunas = len(tabuleiro_atual[0])
    
    # Imprime os números das colunas para orientação do jogador.
    print("   " + " ".join(str(i) for i in range(1, num_colunas + 1)))
    print(" " + "----" * num_colunas)

    # Itera sobre cada linha e exibe seu conteúdo, junto com o número da linha.
    for i, linha in enumerate(tabuleiro_atual):
        print(f"{i+1} | " + " | ".join(celula for celula in linha) + " |")
    print()

def verificar_regras(tabuleiro_atual):
    """
    Verifica se a disposição atual dos hóspedes no tabuleiro
    viola alguma das regras de vizinhança.
    """
    num_linhas = len(tabuleiro_atual)
    num_colunas = len(tabuleiro_atual[0])

    # Percorre cada célula do tabuleiro.
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            hospede_atual = tabuleiro_atual[linha][coluna]
            
            # Se a célula está vazia ou o hóspede não tem regras, passa para a próxima.
            if hospede_atual not in REGRAS_DE_VIZINHANCA:
                continue
            
            # Obtém a lista de hóspedes proibidos de serem vizinhos do hóspede atual.
            hospedes_proibidos = REGRAS_DE_VIZINHANCA[hospede_atual]
            
            # Define as posições dos vizinhos (acima, abaixo, esquerda, direita).
            posicoes_vizinhas = [
                (linha - 1, coluna), 
                (linha + 1, coluna), 
                (linha, coluna - 1), 
                (linha, coluna + 1)
            ]
            
            # Itera sobre cada vizinho.
            for vizinho_linha, vizinho_coluna in posicoes_vizinhas:
                # Verifica se a posição do vizinho está dentro dos limites do tabuleiro.
                if 0 <= vizinho_linha < num_linhas and 0 <= vizinho_coluna < num_colunas:
                    vizinho = tabuleiro_atual[vizinho_linha][vizinho_coluna]
                    # Se o vizinho está na lista de proibidos, retorna False, indicando violação.
                    if vizinho in hospedes_proibidos:
                        return False
                        
    # Se o loop termina sem encontrar violações, a disposição é válida.
    return True

def jogar_fase(informacao_da_fase):
    """Controla o fluxo de uma única fase do jogo."""
    
    # Cria uma cópia do tabuleiro da fase para que as alterações do jogador
    # não afetem o layout da próxima fase.
    tabuleiro_da_fase = copy.deepcopy(informacao_da_fase["tabuleiro"])
    hospedes_restantes = informacao_da_fase["hospedes_para_alocar"]
    num_linhas = len(tabuleiro_da_fase)
    num_colunas = len(tabuleiro_da_fase[0])

    print("-" * 30)
    print(f"Bem-vindo à {informacao_da_fase['nome']}!")
    hospedes_nomes_completos = [HOSPEDES_INFO[h] for h in hospedes_restantes]
    print(f"Você precisa alocar os seguintes hóspedes: {', '.join(hospedes_nomes_completos)}")
    print("-" * 30)
    
    # Loop principal para alocar cada hóspede da fase.
    for hospede_a_alocar in hospedes_restantes:
        exibir_tabuleiro(tabuleiro_da_fase)
        print(f"Onde você quer alocar o {HOSPEDES_INFO[hospede_a_alocar]} ({hospede_a_alocar})?")
        
        # Loop para garantir que o jogador insira uma posição válida.
        while True:
            try:
                # O jogador insere a posição (linha e coluna), subtraímos 1
                # para converter para o índice da lista (que começa em 0).
                linha_escolhida = int(input(f" Digite a linha (1-{num_linhas}): ")) - 1
                coluna_escolhida = int(input(f" Digite a coluna (1-{num_colunas}): ")) - 1

                # Valida se a posição está dentro dos limites do tabuleiro
                # e se o quarto está vazio (' ').
                if not (0 <= linha_escolhida < num_linhas and 0 <= coluna_escolhida < num_colunas):
                    print("Posição inválida! Fora do tabuleiro. Tente novamente.")
                elif tabuleiro_da_fase[linha_escolhida][coluna_escolhida] != ' ':
                    print("Este quarto não está disponível! Escolha outro.")
                else:
                    # Aloca o hóspede na posição escolhida.
                    tabuleiro_da_fase[linha_escolhida][coluna_escolhida] = hospede_a_alocar
                    break  # Sai do loop de entrada, pois a posição é válida.
            except ValueError:
                # Captura erro se o usuário não digitar um número.
                print("Entrada inválida. Por favor, digite apenas números.")
    
    print("\nSua disposição final para esta fase foi:")
    exibir_tabuleiro(tabuleiro_da_fase)
    
    # Chama a função de verificação para determinar o resultado da fase.
    if verificar_regras(tabuleiro_da_fase):
        print("Parabéns! Você passou de fase com êxito!")
        return True
    else:
        print("Que pena! A disposição dos hóspedes viola as regras.")
        return False

def iniciar_jogo():
    """Função principal que gerencia o fluxo de todas as fases do jogo."""
    
    # Exibe as regras do jogo no início.
    print("Rato não pode ficar ao lado do Gato ou Queijo")
    print("Gato não pode ficar ao lado do Rato ou Cão")
    print("Cão não pode ficar ao lado do Osso ou Gato")
    print("Osso não pode ficar ao lado do Cão")
    print("Queijo não pode ficar ao lado do Rato")
    print("\nRegras de vizinhança: ", REGRAS_DE_VIZINHANCA)
    print("-" * 30)
    
    # Itera sobre cada fase do jogo.
    for fase in FASES_DO_JOGO:
        sucesso = jogar_fase(fase)
        # Se uma fase não for concluída com sucesso, o jogo termina.
        if not sucesso:
            print("\nVocê perdeu!")
            break
    else:
        # O bloco `else` do loop `for` é executado apenas se o loop
        # for concluído sem interrupção (`break`). Isso significa
        # que o jogador venceu todas as fases.
        print("\nVOCÊ GANHOU! Parabéns por resolver todos os desafios do hotel!")

# --- Início da Execução do Programa ---

# O `if __name__ == "__main__":` garante que o código dentro
# deste bloco só será executado quando o script for rodado diretamente.
if __name__ == "__main__":
    iniciar_jogo()
