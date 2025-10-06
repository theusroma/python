# Importa o módulo 'math' para ter acesso a constantes e funções matemáticas, como PI.
import math

class Circulo:
    # Em vez de um atributo de instância, PI é uma constante para todos os círculos.
    # Usar math.pi é a forma mais precisa e recomendada.
    pi = math.pi

    def __init__(self, raio):
        # Validação para garantir que o raio seja um número positivo.
        if raio <= 0:
            # Lançar um erro é uma forma robusta de lidar com dados inválidos.
            raise ValueError("O raio deve ser um número positivo.")
        self.raio = raio
    
    def calcular_area(self):
        """Calcula a área do círculo usando a fórmula: PI * raio^2"""
        # O operador '**' realiza a exponenciação.
        # A palavra-chave 'return' envia o resultado de volta.
        return self.pi * (self.raio ** 2)

    # MÉTODO ADICIONADO: para calcular o perímetro (circunferência).
    def calcular_perimetro(self):
        """Calcula o perímetro do círculo usando a fórmula: 2 * PI * raio"""
        return 2 * self.pi * self.raio

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    # Cria uma instância de Circulo com raio 5.
    c1 = Circulo(5) 
    
    # Chama os métodos e armazena os valores retornados.
    area = c1.calcular_area()
    perimetro = c1.calcular_perimetro()
    
    print(f"--- Círculo com raio {c1.raio} ---")
    
    # A formatação ':.2f' limita a saída a duas casas decimais.
    print(f"A área é: {area:.2f}")
    print(f"O perímetro é: {perimetro:.2f}")

    # Exemplo com outro círculo
    c2 = Circulo(10)
    print(f"\n--- Círculo com raio {c2.raio} ---")
    print(f"A área é: {c2.calcular_area():.2f}")
    print(f"O perímetro é: {c2.calcular_perimetro():.2f}")