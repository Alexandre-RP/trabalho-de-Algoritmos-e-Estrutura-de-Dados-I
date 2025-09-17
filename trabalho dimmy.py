# scheduler_meio_bagunçado.py

# --- Estrutura básica de Processo ---
class Processo:
    def __init__(self, id, nome, prioridade, ciclos, recurso=None):
        self.id = id
        self.nome = nome
        self.prioridade = prioridade  # 1 = alta, 2 = média, 3 = baixa
        self.ciclos = ciclos
        self.recurso = recurso
        self.ja_bloqueou = False  # flagzinha tosca pra saber se já foi pro bloqueados

    def __str__(self):
        return f"{self.nome}(id={self.id}, prio={self.prioridade}, ciclos={self.ciclos}, recurso={self.recurso})"
         --- Nó e Lista Encadeada improvisada ---
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaDeProcessos:
    def __init__(self):
        self.head = None

    def esta_vazia(self):
        return self.head is None

    def inserir_no_fim(self, proc):

    def inserir_no_fim(self, proc):
        novo = Node(proc)
        if self.head is None:
            self.head = novo
        else:
            atual = self.head
            while atual.prox is not None:  # isso é O(n), mas paciência
                atual = atual.prox
            atual.prox = novo

     def remover_do_inicio(self):
        if self.head is None:
            return None
        p = self.head.valor
        self.head = self.head.prox
        return p

    def __iter__(self):  
        atual = self.head
        while atual:
            yield atual.valor
            atual = atual.prox

    def to_list(self):  # só pra debug/imprimir bonito
        itens = []
        atual = self.head
        while atual:
            itens.append(str(atual.valor))
            atual = atual.prox
        return itens
        # --- O Scheduler principal ---
class Scheduler:
    def __init__(self):
        self.alta = ListaDeProcessos()
        self.media = ListaDeProcessos()
        self.baixa = ListaDeProcessos()
        self.bloqueados = ListaDeProcessos()
        self.contador_alta = 0

    def adicionar_processo(self, proc):
        if proc.prioridade == 1:
            self.alta.inserir_no_fim(proc)
        elif proc.prioridade == 2:
            self.media.inserir_no_fim(proc)



