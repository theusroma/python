nomes = ['matheus', 'matheus', 'joao', 'arthur', 'rebeca', 'rebeca', 'rebeca']
print(nomes)

print(nomes.count('matheus'))
print(nomes.count('joao'))
print(nomes.count('arthur'))
print(nomes.count('rebeca'))

print()
print()
print()

x={
    'matheus': nomes.count('matheus'), 
    'joao': nomes.count('joao'), 
    'arthur': nomes.count('arthur'), 
    'rebeca': nomes.count('rebeca')
    }

print('matheus', x['matheus'])
print('joao', x['joao'])
print('arthur', x['arthur'])
print('rebeca', x['rebeca'])
