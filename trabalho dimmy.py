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
