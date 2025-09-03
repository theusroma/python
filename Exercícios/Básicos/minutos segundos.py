tempo = int(input("Digite o tempo em segundos: "))



horas = tempo // 3600; # Calcula quantas horas inteiras cabem nos segundos (1 hora = 3600 segundos)

resto = tempo % 3600; # Calcula o restante dos segundos que sobraram após tirar as horas


minutos = resto // 60; # Com o restante, calcula quantos minutos inteiros cabem (1 minuto = 60 segundos)


segundos = resto % 60; # E o que sobrou disso são os segundos finais


print("Horas: ", horas);
print("Minutos: ", minutos);
print("Segundos: ", segundos);




 
