# Sistema Distribuído Simulado com Threads

Este projeto implementa um sistema distribuído simulado em Python, utilizando threads para a execução paralela de tarefas. O programa permite calcular soma de listas, termos da sequência de Fibonacci (parcial ou único), ou integrais de funções simples, destacando os benefícios do paralelismo em comparação à execução sequencial.

---

## Funcionalidades

1. **Soma de Lista:**
   - Divide uma lista de números inteiros entre threads para calcular a soma parcial de cada pedaço.

2. **Cálculo de Fibonacci:**
   - **Série Parcial:** Calcula um conjunto de termos da sequência de Fibonacci divididos entre threads.
   - **Termo Único:** Calcula diretamente um termo específico da sequência de Fibonacci.

3. **Cálculo de Integral:**
   - Utiliza o método dos retângulos para calcular a integral de uma função definida em um intervalo.

4. **Comparativo de Desempenho:**
   - Exibe o tempo total de execução paralela e sequencial para destacar os benefícios do paralelismo.

---

## Requisitos do Sistema

- Python 3.6 ou superior.
- Biblioteca padrão do Python (é utilizada a biblioteca `threading`, `time` e `random`).

---

## Como Usar

1. Execute o programa principal:
   ```bash
   python nome_do_arquivo.py
   ```

2. Escolha a operação desejada no menu interativo:
   - **1:** Soma de Lista.
   - **2:** Cálculo da Série de Fibonacci (parcial).
   - **3:** Cálculo de Integral.
   - **4:** Cálculo de um Termo Único da Sequência de Fibonacci.

3. Insira os parâmetros solicitados, como o índice desejado na sequência de Fibonacci.

4. O programa exibirá:
   - Resultados parciais de cada thread.
   - Resultado final consolidado pelo servidor central.
   - Tempos de execução paralela e sequencial.

---

## Exemplo de Uso

### Soma de Lista
- Entrada:
  - Lista de 1 a 1000.
  - 10 threads.
- Saída:
  - Resultado final: 500500.
  - Tempo paralelo: 0.01s.
  - Tempo sequencial: 0.03s.

### Fibonacci
- Entrada:
  - Cálculo dos primeiros 100 termos.
  - 10 threads.
- Saída:
  - Resultado final: [0, 1, 1, 2, 3, ...].
  - Tempo paralelo: 0.05s.
  - Tempo sequencial: 0.12s.

### Integral
- Entrada:
  - Função: \(f(x) = x^2\).
  - Intervalo: [0, 10].
  - 10 threads.
- Saída:
  - Resultado final: 333.333 (aproximado).
  - Tempo paralelo: 0.02s.
  - Tempo sequencial: 0.04s.

### Fibonacci (Termo Único)
- Entrada:
  - Termo: 1000.
- Saída:
  - Resultado final: 4.346655768693743e+208 (aproximado).
  - Tempo sequencial: 0.05s.

---

## Personalização

- **Latência Simulada:** O programa simula latência nas threads com:
  ```python
  time.sleep(random.uniform(0.5, 1.5))
  ```
  Você pode ajustar os valores para alterar o tempo de espera.

- **Tarefas:** Adicione novas funções seguindo o padrão das existentes e integre com as threads.

---

