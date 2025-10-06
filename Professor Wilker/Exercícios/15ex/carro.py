# Componente 1: Motor
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def __str__(self):
        return f"Motor V8 de {self.potencia}cv"

    def ligar(self):
        print(f"Motor de {self.potencia}cv ligado. Vrum Vrum!")
    
    def desligar(self):
        print("Motor desligado.")

# Componente 2: Pneu
class Pneu:
    def __init__(self, aro):
        self.aro = aro
    
    def __str__(self):
        return f"Pneu aro {self.aro}"

# Classe principal (Container) que é COMPOSTA por outros objetos.
class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor # Composição: O Carro "tem um" Motor.
        
        # Composição "tem-muitos": O Carro "tem vários" Pneus.
        # Os pneus são criados dentro do próprio carro.
        self.pneus = [Pneu(18), Pneu(18), Pneu(18), Pneu(18)]

    def __str__(self):
        return f"Carro: {self.modelo} | {self.motor} | {len(self.pneus)} pneus"

    def ligar_carro(self):
        """Delega a ação de ligar para o seu componente motor."""
        print(f"Ligando o {self.modelo}...")
        self.motor.ligar()
    
    def desligar_carro(self):
        """Delega a ação de desligar para o seu componente motor."""
        print(f"Desligando o {self.modelo}...")
        self.motor.desligar()

# --- Exemplo de Uso (Código Completado) ---
if __name__ == "__main__":
    
    # 1. Cria a instância do componente Motor primeiro.
    motor_v8 = Motor("450")
    
    # 2. Passa a instância do motor para o construtor do Carro (Injeção de Dependência).
    meu_mustang = Carro("Mustang GT", motor_v8)
    
    # Exibe o estado do objeto Carro, que inclui informações de seus componentes.
    print("--- Composição do Carro ---")
    print(meu_mustang)
    
    print("\n--- Ações ---")
    # 3. Chama o método do Carro, que delega a ação para o Motor.
    meu_mustang.ligar_carro()
    meu_mustang.desligar_carro()