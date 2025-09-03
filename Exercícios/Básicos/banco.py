reais = int(input("Digite um numero: "))
cem = 100;
cinquenta = 50; 
dez = 10;
um = 1;

contadorcem = reais // cem       # quantas de 100
reais = reais % cem              # sobra

contadordez = reais // dez       
reais = reais % dez              
  
contadorcinquenta = reais // cinquenta
reais = reais % cinquenta              
    
contadorum = reais // um    
reais = reais % um              
    
print("Notas de 100: ", contadorcem)
        
print("Notas de 50: ", contadorcinquenta)

print("Notas de 10: ", contadordez)

print("Notas de 1: ", contadorum)

    

