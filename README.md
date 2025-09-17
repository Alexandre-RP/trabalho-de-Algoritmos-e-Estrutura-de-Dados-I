# trabalho-de-Algoritmos-e-Estrutura-de-Dados-I
# Escalonador com Listas de Prioridade (Trabalho P1)

Projeto da disciplina **Algoritmos e Estrutura de Dados I**.  
Implementação de um escalonador de processos do zero, sem usar listas prontas.  
Feito no modo "humano": tem gambiarras, uns prints de debug e nada de perfeição industrial.

---

## 👨‍💻 Como rodar

### 1. Pré-requisitos
- Python 3 instalado (testado na versão 3.10, mas deve rodar em outras).
- Ter o arquivo `scheduler_meio_bagunçado.py` na pasta.

### 2. Arquivo de entrada
Crie um arquivo chamado **`processos.csv`** no mesmo diretório do código.  
Cada linha representa um processo no formato: id,nome,prioridade(1=alta,2=media,3=baixa),ciclos,recurso

Exemplo:
1,ProcA,1,4,DISCO
2,ProcB,2,3,
3,ProcC,3,2,
4,ProcD,1,1,

> Obs: `recurso` pode ser vazio. Se for "DISCO", o processo vai ser bloqueado na primeira vez que tentar rodar.

### 3. Executando
No terminal:
bash
python scheduler_meio_bagunçado.py

4. Saída esperada

A cada ciclo, o programa mostra:

Qual processo está rodando.

Quais estão nas filas de alta, média e baixa.

Quem foi para bloqueados.

Quem terminou.

Exemplo (resumido):
===== CICLO 1 =====
ProcA pediu DISCO, vai pra bloqueados...
 Alta: []
 Média: ['ProcB(...)']
 Baixa: ['ProcC(...)']
 Bloqueados: ['ProcA(...)']




