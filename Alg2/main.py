from pilha import Pilha
from fila import Fila



pilha = Pilha()
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)
print (pilha.exibir())

pilha.desempilhar()
print(pilha.exibir())



fila = Fila()
fila.enfileirar(50)
fila.enfileirar(60)
fila.enfileirar(70)
fila.enfileirar(80)
print(fila.exibir())

fila.desenfileirar()
print(fila.exibir())