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
        else:
            self.baixa.inserir_no_fim(proc)
            
    def desbloquear_um(self):
        desbloq = self.bloqueados.remover_do_inicio()
        if desbloq:
            print(f"   >> desbloqueando {desbloq.nome}")
            self.adicionar_processo(desbloq)

    def escolher_proximo(self):
        # regra anti-inanição
        if self.contador_alta >= 5:
            p = self.media.remover_do_inicio()
            if p is None:
                p = self.baixa.remover_do_inicio()
            self.contador_alta = 0
            if p:
                return p
        # ordem normal
        p = self.alta.remover_do_inicio()
        if p:
            self.contador_alta += 1
            return p
        p = self.media.remover_do_inicio()
        if p:
            return p
        p = self.baixa.remover_do_inicio()
        return p

    def executar_ciclo(self, ciclo_num):
        print(f"\n===== CICLO {ciclo_num} =====")
        # desbloqueia primeiro
        self.desbloquear_um()

        proc = self.escolher_proximo()
        if not proc:
            print("Nenhum processo disponível (fim?).")
            return False

        # se precisa de disco e ainda não bloqueou antes
        if proc.recurso == "DISCO" and not proc.ja_bloqueou:
            print(f"{proc.nome} pediu DISCO, vai pra bloqueados...")
            proc.ja_bloqueou = True
            self.bloqueados.inserir_no_fim(proc)
        else:
            print(f"Rodando {proc.nome} (ciclos restantes: {proc.ciclos})")
            proc.ciclos -= 1
            if proc.ciclos > 0:
                self.adicionar_processo(proc)
            else:
                print(f"   >> {proc.nome} terminou!")



