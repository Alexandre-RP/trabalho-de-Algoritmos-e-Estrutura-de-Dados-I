# Escalonador com Listas de Prioridade (Trabalho P1)
Disciplina:Algoritmo e Estrutura de dados 1
Prof(a):Dimmy Magalhães
Integrantes/matricula:
Alexandre Rodrigues Prado Filho -> 0030604
Caio Rafael Veloso de Carvalho -> 0030170
Leoncio do Rêgo Monteiro Filho -> 0030771

Projeto da disciplina **Algoritmos e Estrutura de Dados I**.  
Implementação de um escalonador de processos do zero, sem usar listas prontas.  
Feito no modo "humano": tem gambiarras, uns prints de debug e nada de perfeição industrial.

---

## ⚙️ Como rodar

1. **Pré-requisitos:**
   - Python 3 instalado (testado na versão 3.10, mas deve rodar em outras).
   - Ter o arquivo `scheduler_meio_bagunçado.py` na pasta.

2. **Crie o arquivo de entrada `processos.csv`:**

   Exemplo de conteúdo:
1,ProcA,1,4,DISCO
2,ProcB,2,3,
3,ProcC,3,2,
4,ProcD,1,1,

Cada linha é:id,nome,prioridade(1=alta,2=media,3=baixa),ciclos,recurso

Obs: o recurso pode ficar vazio.

3. **Rodando:**
```bash
python scheduler_meio_bagunçado.py
Saída esperada:

A cada ciclo, ele mostra:

Qual processo rodou.

Quem está em cada lista (alta, média, baixa).

Quem foi para bloqueados.

Quem terminou.

Exemplo de saída (simplificada):

===== CICLO 1 =====
ProcA pediu DISCO, vai pra bloqueados...
 Alta: []
 Média: ['ProcB(...)']
 Baixa: ['ProcC(...)']
 Bloqueados: ['ProcA(...)']


