#MATHEUS SILVA DOS SANTOS
#TRABALHO DE ANÁLISE DE DADOS -PROTEINAS - CLUSTER/KMEANS

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
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr
import warnings
from sklearn.exceptions import ConvergenceWarning

#conf globais dos aminoacidos
URL = "https://scop.berkeley.edu/downloads/scopeseq-2.08/astral-scopedom-seqres-gd-sel-gs-bib-40-2.08.fa"
AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'

# skip de 2 em 2
SKIP_SIZE = 2
PCA_COMPONENTS = 300


def download_data(url):
    #baixa e processa os dados
    print(f"Iniciando download dos dados de: {url}")
    try:
        # precisei pular a verificacao"
        response = requests.get(url, verify=False)
        response.raise_for_status()
        
        fasta_data = io.StringIO(response.text)
        
        sequences = []
        labels = []
        
        for record in SeqIO.parse(fasta_data, "fasta"):
            try:
                full_label = record.description.split(' ')[1]
                
                # calsse real sao os prmeiros caracteres, (a ou b), reduziu o problema para apenas 7 classes
                class_label = full_label.split('.')[0]

                # converti tudo pra upper pra evitar problemas
                sequences.append(str(record.seq).upper())
                labels.append(class_label)
            except IndexError:
                pass

        print(f"Processamento concluído. {len(sequences)} sequências carregadas.")
        
        #usei o label encoder para transformar as classes em letrsa, para poder usar o f1 SCORE
        le = LabelEncoder()
        y_true = le.fit_transform(labels)
        true_labels_names = le.classes_
        
        print(f"Encontradas {len(true_labels_names)} classes únicas.")
        
        return sequences, labels, y_true, true_labels_names

    except requests.exceptions.RequestException as e:
        print(f"Erro fatal ao baixar o arquivo: {e}")
        return None, None, None, None

def extract_features(sequences, skip_size):
    #(segunda parte da metodologia) transformando sequencia de texto em numero
    print(f"Iniciando extração de atributos (skip={skip_size})...")
    
    feature_map = {}
    idx = 0
    ##criando todas as combinacaoes possiveis de aminoacidos 20x20(400) 
    for aa1 in AMINO_ACIDS:
        for aa2 in AMINO_ACIDS:
            feature_map[f"{aa1}-{aa2}"] = idx
            idx += 1

    n_features = len(feature_map)
    n_sequences = len(sequences)

    binary_matrix = np.zeros((n_sequences, n_features), dtype=np.int8)

    #esse for aponta para todaas as 15000 sequencias e marca 1(presença) pra cada par que ele encontra com aminoacido de skip 2
    for i, seq in enumerate(sequences):
        for j in range(len(seq) - skip_size - 1):
            aa1 = seq[j]
            aa2 = seq[j + skip_size + 1]
            
            if aa1 in AMINO_ACIDS and aa2 in AMINO_ACIDS:
                feature_name = f"{aa1}-{aa2}"
                col_idx = feature_map[feature_name]
                binary_matrix[i, col_idx] = 1

    print("Matriz binária criada.")
    print(f"Dimensões da Matriz de Atributos (bruta): {binary_matrix.shape}")

    # variavel selector aponta pra classe, filtro de remover colunas com variancia 0 (quebrariam o PCA)
    selector = VarianceThreshold()
    binary_matrix_filtered = selector.fit_transform(binary_matrix)
    
    if binary_matrix.shape[1] != binary_matrix_filtered.shape[1]:
        n_removed = binary_matrix.shape[1] - binary_matrix_filtered.shape[1]
        print(f"Removidas {n_removed} features com variância zero (sem ocorrências).")
    
    print(f"Dimensões da Matriz de Atributos (filtrada): {binary_matrix_filtered.shape}")
    
    return binary_matrix_filtered

def run_pca(matrix, n_components):
    #Com a matriz pronta (15000 x 400), rodando o PCA pra reduzir a dimensionlidade
    print(f"Iniciando cálculo do PCA (n_components={n_components})...")
    
    if n_components > matrix.shape[1]:
        print(f"Aviso: N de componentes ({n_components}) é maior que o n de features ({matrix.shape[1]}).")
        n_components = matrix.shape[1]
        print(f"Ajustando n_components para {n_components}.")

    pca = PCA(n_components=n_components, random_state=42)
    pca_matrix = pca.fit_transform(matrix)
    
    explained_variance = np.sum(pca.explained_variance_ratio_)
    print("PCA calculado.")
    print(f"Dimensões da Matriz PCA: {pca_matrix.shape}")
    
    # variancia a ser mostrada no terminal"
    print(f"Variância explicada pelos {n_components} componentes: {explained_variance:.2%}")
    
    return pca_matrix

def run_clustering_analysis(data, y_true, true_labels_names):
    print("\n--- Iniciando Testes de Clustering ---")
    
    n_real_clusters = len(true_labels_names)
    
    #defini a faixa de 'k' que ia testar, baseada no número real de classes, que é 7
    k_range = [n_real_clusters - 2, n_real_clusters, n_real_clusters + 2]
    k_range = [k for k in k_range if k > 1]
    
    print(f"Número de classes reais: {n_real_clusters}")
    print(f"Testando k (n_clusters) em: {k_range}")

    # algoritmos comparados
    clustering_k_models = {
        'KMeans': KMeans(n_init=10, random_state=42),
        'Agglomerative': AgglomerativeClustering(),
        'Birch': Birch(),
    }
    
    results = []

    warnings.filterwarnings("ignore", category=ConvergenceWarning)

    #rodando os algoritmos
    for k in k_range:
        print(f"\n--- Testando com k = {k} ---")
        
        for name, algorithm in clustering_k_models.items():
            try:
                algorithm.set_params(n_clusters=k)
                y_pred = algorithm.fit_predict(data)
                
                #calculo de metricas para cada um:(Silhouette, DB, CH)
                silhouette = silhouette_score(data, y_pred)
                davies_bouldin = davies_bouldin_score(data, y_pred)
                calinski_harabasz = calinski_harabasz_score(data, y_pred)
                f1 = f1_score(y_true, y_pred, average='weighted')
                
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

    if not results:
        print("Nenhum resultado de clustering foi gerado.")
        return

    #colocando tudo no panda pra melhorar a visualização
    results_df = pd.DataFrame(results)
    
    print("\n--- Resultados Finais (DataFrame) ---")
    print(results_df.to_string())

    
    # correlação Pearson para checar qual se parecia com o score(F1)"
    print("\n--- Correlação (Pearson) com F1-Score ---")
    try:
        corr_sil = pearsonr(results_df['F1_Score'], results_df['Silhouette'])
        corr_db = pearsonr(results_df['F1_Score'], results_df['Davies_Bouldin'])
        corr_ch = pearsonr(results_df['F1_Score'], results_df['Calinski_Harabasz'])

        # aponta para o p, só o Silhouette teve correlação significativa. interna mais confiavel
        print(f"Correlação F1 vs Silhouette:       {corr_sil[0]:.4f} (p-value: {corr_sil[1]:.4f})")
        print(f"Correlação F1 vs Davies-Bouldin:  {corr_db[0]:.4f} (p-value: {corr_db[1]:.4f})")
        print(f"Correlação F1 vs Calinski-Harabasz: {corr_ch[0]:.4f} (p-value: {corr_ch[1]:.4f})")
    except ValueError as e:
        print(f"Não foi possível calcular a correlação (pontos de dados insuficientes?): {e}")


    print("\n--- Sugestão de Melhor Configuração ---")
    
    #vemos o melhor F1-Score: KMeans com k=7, que é o número real de classes."
    best_f1 = results_df.loc[results_df['F1_Score'].idxmax()]
    print(f"\nMelhor configuração (baseada no F1-Score - Métrica Externa):\n{best_f1}")
    
    #vemos o melhor Silhouette: KMeans com k=5."
    #KMeans foi o melhor algoritmo em ambos os cenários."
    best_silhouette = results_df.loc[results_df['Silhouette'].idxmax()]
    print(f"\nMelhor configuração (baseada na Silhouette - Métrica Interna):\n{best_silhouette}")
    
    best_db = results_df.loc[results_df['Davies_Bouldin'].idxmin()]
    print(f"\nMelhor configuração (baseada no Davies-Bouldin - Métrica Interna):\n{best_db}")


def main():
    
    print("Iniciando pipeline de análise de proteínas...")
    
    sequences, labels, y_true, true_labels_names = download_data(URL)
    
    if sequences:
        binary_matrix = extract_features(sequences, SKIP_SIZE)
        
        if binary_matrix.shape[0] > 0 and binary_matrix.shape[1] > 0:
            pca_matrix = run_pca(binary_matrix, PCA_COMPONENTS)
            run_clustering_analysis(pca_matrix, y_true, true_labels_names)
        else:
            print("Erro: A matriz de atributos ficou vazia após a filtragem.")
    
    print("\nPipeline concluído.")

if __name__ == "__main__":
    main()
