#!/usr/bin/env python3

"""
1 Download dos dados FASTA.
2 Extração de atributos (features) "kmer 2X2" (assumindo skip=2).
3 Redução de dimensionalidade com PCA (300 componentes).
4 Teste de algoritmos de clustering (KMeans, etc.).
5 Avaliação com métricas internas e externas (F1-Score).
6 Análise de correlação e sugestão de melhor modelo.
"""

import requests
import io
import numpy as np
import pandas as pd
from Bio import SeqIO
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    f1_score, 
    silhouette_score, 
    davies_bouldin_score, 
    calinski_harabasz_score
)
from sklearn.cluster import (
    KMeans, 
    AgglomerativeClustering, 
    Birch, 
    DBSCAN, 
    MeanShift
)
from sklearn.feature_selection import VarianceThreshold # <-- CORREÇÃO 1: Importação
from scipy.stats import pearsonr
import warnings
from sklearn.exceptions import ConvergenceWarning

# --- Configurações Globais ---

# URL do banco de dados FASTA
URL = "https://scop.berkeley.edu/downloads/scopeseq-2.08/astral-scopedom-seqres-gd-sel-gs-bib-40-2.08.fa"

# Aminoácidos padrão (20)
AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'

# --- PARÂMETRO CRÍTICO ---
# ATENÇÃO: Assumindo "kmer 2X2" como um par de aminoácidos com 2 "skips"
# Ex: AxxC. Se o significado for outro, (ex: skip=1), mude esta variável.
SKIP_SIZE = 2

# Componentes Principais para o PCA
PCA_COMPONENTS = 300


def download_data(url):
    """
    Baixa e processa o arquivo FASTA.
    Extrai sequências e rótulos de classe (ex: 'a.1.1.1').
    """
    print(f"Iniciando download dos dados de: {url}")
    try:
        response = requests.get(url, verify=False) # Permite acesso sem SSL
        response.raise_for_status()  # Verifica se houve erro no download
        
        fasta_data = io.StringIO(response.text)
        
        sequences = []
        labels = []
        
        # Processa o arquivo FASTA com BioPython
        for record in SeqIO.parse(fasta_data, "fasta"):
            try:
                # O header é: >d1a1aa_ a.1.1.1 (A:) ...
                # O rótulo (classe) é o segundo elemento
                full_label = record.description.split(' ')[1] # Ex: 'a.1.1.1'
                
                # --- INÍCIO DA CORREÇÃO 2 ---
                # Vamos usar apenas a classe principal (o primeiro caractere)
                class_label = full_label.split('.')[0] # Pega 'a' de 'a.1.1.1'
                # --- FIM DA CORREÇÃO 2 ---

                sequences.append(str(record.seq).upper())
                labels.append(class_label)
            except IndexError:
                pass # Ignora headers mal formatados

        print(f"Processamento concluído. {len(sequences)} sequências carregadas.")
        
        # Codifica os rótulos de texto para números (para o F1-Score)
        le = LabelEncoder()
        y_true = le.fit_transform(labels)
        true_labels_names = le.classes_
        
        print(f"Encontradas {len(true_labels_names)} classes únicas.")
        
        return sequences, labels, y_true, true_labels_names

    except requests.exceptions.RequestException as e:
        print(f"Erro fatal ao baixar o arquivo: {e}")
        return None, None, None, None

def extract_features(sequences, skip_size):
    """
    Cria a matriz binária de presença/ausência de pares de aminoácidos
    com base no SKIP_SIZE definido.
    """
    print(f"Iniciando extração de atributos (skip={skip_size})...")
    
    # 1. Criar um mapa de todos os features (colunas)
    feature_map = {}
    idx = 0
    for aa1 in AMINO_ACIDS:
        for aa2 in AMINO_ACIDS:
            feature_map[f"{aa1}-{aa2}"] = idx
            idx += 1

    n_features = len(feature_map)
    n_sequences = len(sequences)

    # 2. Inicializar a matriz binária (usar int8 para economizar memória)
    binary_matrix = np.zeros((n_sequences, n_features), dtype=np.int8)

    # 3. Preencher a matriz
    for i, seq in enumerate(sequences):
        # Janela móvel
        # O último índice válido é len(seq) - skip_size - 2
        for j in range(len(seq) - skip_size - 1):
            aa1 = seq[j]
            aa2 = seq[j + skip_size + 1]
            
            # Ignora aminoácidos não-padrão (X, B, Z, etc.)
            if aa1 in AMINO_ACIDS and aa2 in AMINO_ACIDS:
                feature_name = f"{aa1}-{aa2}"
                col_idx = feature_map[feature_name]
                binary_matrix[i, col_idx] = 1 # Marca presença

    print("Matriz binária criada.")
    print(f"Dimensões da Matriz de Atributos (bruta): {binary_matrix.shape}")

    # --- INÍCIO DA CORREÇÃO 1 (lugar correto) ---
    # Remove features (colunas) com variância zero
    # (ou seja, pares que nunca apareceram em nenhuma sequência)
    selector = VarianceThreshold()
    binary_matrix_filtered = selector.fit_transform(binary_matrix)
    
    if binary_matrix.shape[1] != binary_matrix_filtered.shape[1]:
        n_removed = binary_matrix.shape[1] - binary_matrix_filtered.shape[1]
        print(f"Removidas {n_removed} features com variância zero (sem ocorrências).")
    
    print(f"Dimensões da Matriz de Atributos (filtrada): {binary_matrix_filtered.shape}")
    
    # Retorna a matriz filtrada
    return binary_matrix_filtered
    # --- FIM DA CORREÇÃO 1 ---

def run_pca(matrix, n_components):
    """
    Aplica o PCA para reduzir a dimensionalidade da matriz.
    """
    print(f"Iniciando cálculo do PCA (n_components={n_components})...")
    
    # Verifica se n_components é válido (não pode ser maior que o n_features)
    if n_components > matrix.shape[1]:
        print(f"Aviso: N de componentes ({n_components}) é maior que o n de features ({matrix.shape[1]}).")
        n_components = matrix.shape[1]
        print(f"Ajustando n_components para {n_components}.")

    pca = PCA(n_components=n_components, random_state=42)
    pca_matrix = pca.fit_transform(matrix)
    
    explained_variance = np.sum(pca.explained_variance_ratio_)
    print("PCA calculado.")
    print(f"Dimensões da Matriz PCA: {pca_matrix.shape}")
    print(f"Variância explicada pelos {n_components} componentes: {explained_variance:.2%}")
    
    return pca_matrix

def run_clustering_analysis(data, y_true, true_labels_names):
    """
    Testa múltiplos algoritmos de clustering, calcula métricas
    e analisa os resultados.
    """
    print("\n--- Iniciando Testes de Clustering ---")
    
    n_real_clusters = len(true_labels_names)
    
    # ATENÇÃO: Escolha uma faixa razoável. 
    # Testar muitos 'k' pode ser lento.
    # Vamos testar 3 valores de 'k' (número de clusters)
    
    # Ajuste da faixa de 'k' para ser razoável (ex: de 5 a 15)
    # Usar n_real_clusters (que agora será ~10) como base
    k_range = [n_real_clusters - 2, n_real_clusters, n_real_clusters + 2]
    k_range = [k for k in k_range if k > 1] # Garante k > 1
    
    print(f"Número de classes reais: {n_real_clusters}")
    print(f"Testando k (n_clusters) em: {k_range}")

    # Definindo os algoritmos que precisam de 'k'
    clustering_k_models = {
        'KMeans': KMeans(n_init=10, random_state=42),
        'Agglomerative': AgglomerativeClustering(),
        'Birch': Birch(),
    }
    
    results = []

    # Ignora avisos de convergência do KMeans
    warnings.filterwarnings("ignore", category=ConvergenceWarning)

    # --- Teste 1: Algoritmos que exigem 'k' ---
    for k in k_range:
        print(f"\n--- Testando com k = {k} ---")
        
        for name, algorithm in clustering_k_models.items():
            try:
                algorithm.set_params(n_clusters=k)
                y_pred = algorithm.fit_predict(data)
                
                # Calcular Métricas
                silhouette = silhouette_score(data, y_pred)
                davies_bouldin = davies_bouldin_score(data, y_pred)
                calinski_harabasz = calinski_harabasz_score(data, y_pred)
                f1 = f1_score(y_true, y_pred, average='weighted')
                
                # Armazena os resultados
                results.append({
                    'Algorithm': name,
                    'k': k,
                    'F1_Score': f1,
                    'Silhouette': silhouette,
                    'Davies_Bouldin': davies_bouldin,
                    'Calinski_Harabasz': calinski_harabasz
                })
                
                print(f"  {name} (k={k}): F1={f1:.4f}, Silhouette={silhouette:.4f}")

            except Exception as e:
                print(f"  Erro ao rodar {name} com k={k}: {e}")

    # (Opcional: Adicionar algoritmos que não precisam de 'k', como DBSCAN)
    # print("\n--- Testando algoritmos sem 'k' (ex: DBSCAN) ---")
    # try:
    #     dbscan = DBSCAN(eps=0.5) # 'eps' é o parâmetro mais difícil de acertar
    #     y_pred = dbscan.fit_predict(data)
    #     # ... (cálculo de métricas similar, mas 'k' será o n_de_clusters_encontrado)
    # except Exception as e:
    #     print(f"  Erro ao rodar DBSCAN: {e}")

    # --- Análise dos Resultados ---
    if not results:
        print("Nenhum resultado de clustering foi gerado.")
        return

    results_df = pd.DataFrame(results)
    
    print("\n--- Resultados Finais (DataFrame) ---")
    print(results_df.to_string()) # .to_string() para imprimir tudo

    # --- Análise de Correlação (Pearson) ---
    print("\n--- Correlação (Pearson) com F1-Score ---")
    # Tenta correlacionar métricas internas com a externa (F1)
    # Valores próximos de 1 (positivo) ou -1 (negativo) são bons.
    # Davies-Bouldin é "quanto menor, melhor", então esperamos correlação negativa.
    try:
        corr_sil = pearsonr(results_df['F1_Score'], results_df['Silhouette'])
        corr_db = pearsonr(results_df['F1_Score'], results_df['Davies_Bouldin'])
        corr_ch = pearsonr(results_df['F1_Score'], results_df['Calinski_Harabasz'])

        print(f"Correlação F1 vs Silhouette:       {corr_sil[0]:.4f} (p-value: {corr_sil[1]:.4f})")
        print(f"Correlação F1 vs Davies-Bouldin:  {corr_db[0]:.4f} (p-value: {corr_db[1]:.4f})")
        print(f"Correlação F1 vs Calinski-Harabasz: {corr_ch[0]:.4f} (p-value: {corr_ch[1]:.4f})")
    except ValueError as e:
        print(f"Não foi possível calcular a correlação (pontos de dados insuficientes?): {e}")


    # --- Sugestão da Melhor Configuração ---
    print("\n--- Sugestão de Melhor Configuração ---")
    
    # Opção 1: Melhor F1-Score (se o objetivo é replicar as classes reais)
    best_f1 = results_df.loc[results_df['F1_Score'].idxmax()]
    print(f"\nMelhor configuração (baseada no F1-Score - Métrica Externa):\n{best_f1}")
    
    # Opção 2: Melhor Métrica Interna (ex: Silhouette, que "quanto maior, melhor")
    best_silhouette = results_df.loc[results_df['Silhouette'].idxmax()]
    print(f"\nMelhor configuração (baseada na Silhouette - Métrica Interna):\n{best_silhouette}")
    
    # Opção 3: Melhor Métrica Interna (ex: Davies-Bouldin, que "quanto menor, melhor")
    best_db = results_df.loc[results_df['Davies_Bouldin'].idxmin()]
    print(f"\nMelhor configuração (baseada no Davies-Bouldin - Métrica Interna):\n{best_db}")


def main():
    """Função principal para executar o pipeline."""
    
    print("Iniciando pipeline de análise de proteínas...")
    
    sequences, labels, y_true, true_labels_names = download_data(URL)
    
    # Só continua se o download for bem-sucedido
    if sequences:
        binary_matrix = extract_features(sequences, SKIP_SIZE)
        
        # Verifica se a matriz não está vazia após a filtragem
        if binary_matrix.shape[0] > 0 and binary_matrix.shape[1] > 0:
            pca_matrix = run_pca(binary_matrix, PCA_COMPONENTS)
            run_clustering_analysis(pca_matrix, y_true, true_labels_names)
        else:
            print("Erro: A matriz de atributos ficou vazia após a filtragem.")
    
    print("\nPipeline concluído.")

if __name__ == "__main__":
    main()
