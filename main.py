<<<<<<< HEAD
from vetor import Vetor
vetor = Vetor(5)
vetor.inserir (10)
vetor.inserir (20)
vetor.inserir (30)
vetor.exibir()
print ("Busca:", vetor.buscar(20))
vetor.remover(1)
vetor.exibir()
=======
from lista_dupla import ListaDuplamenteEncadeada
from lista_simples import ListaEncadeada
from lista_circular import ListaCircular


playlist = ListaEncadeada()
playlist.inserir_fim("Musica 1")
playlist.inserir_fim("Musica 2")
playlist.inserir_fim("Musica 3")
playlist.exibir()

historico = ListaDuplamenteEncadeada()
historico.inserir_fim("pagina1.html")
historico.inserir_fim("pagina2.html")
historico.exibir_do_fim()

turnos = ListaCircular()
turnos.inserir_fim("Jogador A")
turnos.inserir_fim("Jogador B")
turnos.inserir_fim("Jogador C")
turnos.percorrer_n_voltas(2)
>>>>>>> main
