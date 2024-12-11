import threading
import time
import random
import matplotlib.pyplot as plt

def worker(task_id, data, operation, results, semaphore, latency=False):
    """Função que representa um nó do cluster."""
    if latency:
        time.sleep(random.uniform(5, 15))  # Simula latência

    if operation == "sum":
        partial_result = sum(data)
    elif operation == "fibonacci":
        partial_result = calculate_fibonacci_range(data[0], data[1])
    elif operation == "fibonacci_single":
        partial_result = calculate_fibonacci_single(data)
    elif operation == "integral":
        func, start, end, step = data
        partial_result = calculate_integral(func, start, end, step)
    else:
        raise ValueError("Operação desconhecida.")

    print(f"Thread {task_id} - resultado parcial: {partial_result}")

    with semaphore:
        results[task_id] = partial_result  # Atualiza o resultado parcial

def central_server(n, results, operation, final_result):
    """Função que representa o servidor central consolidando resultados."""
    if operation == "sum":
        total_result = sum(results)
    elif operation in ["fibonacci", "fibonacci_single", "integral"]:
        total_result = sum(results, []) if operation == "fibonacci" else results[0]
    else:
        raise ValueError("Operação desconhecida.")

    final_result[0] = total_result
    print("\nServidor Central - Resultados consolidados:")
    print(results, f"= {total_result}")

def calculate_fibonacci_range(start, count):
    """Calcula os termos da série de Fibonacci a partir de um índice inicial."""
    fib = [0, 1]
    for _ in range(2, start + count):
        fib.append(fib[-1] + fib[-2])
    return fib[start:start + count]

def calculate_fibonacci_single(n):
    """Calcula o enésimo termo da série de Fibonacci diretamente."""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculate_integral(func, start, end, step):
    """Calcula a integral de uma função usando o método dos retângulos."""
    area = 0
    x = start
    while x < end:
        area += func(x) * step
        x += step
    return area

def execute_parallel_task(n, operation, data_chunks, simulate_latency=False):
    """Executa uma tarefa paralela com base na operação especificada."""
    threads = []
    results = [0] * n
    semaphore = threading.Semaphore(1)

    start_time = time.time()

    # Criando threads
    for i in range(len(data_chunks)):
        thread = threading.Thread(
            target=worker, 
            args=(i, data_chunks[i], operation, results, semaphore, simulate_latency)
        )
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    # Consolidando resultados
    final_result = [0]
    central_server(n, results, operation, final_result)

    end_time = time.time()

    return final_result[0], end_time - start_time

def execute_sequential_task(operation, data_chunks):
    """Executa uma tarefa sequencialmente com base na operação especificada."""
    start_time = time.time()

    if operation == "sum":
        total_result = sum(sum(chunk) for chunk in data_chunks)
    elif operation == "fibonacci":
        total_result = []
        for chunk in data_chunks:
            total_result.extend(calculate_fibonacci_range(chunk[0], chunk[1]))
    elif operation == "fibonacci_single":
        total_result = calculate_fibonacci_single(data_chunks[0])
    elif operation == "integral":
        total_result = sum(calculate_integral(func, start, end, step) for func, start, end, step in data_chunks)
    else:
        raise ValueError("Operação desconhecida.")

    end_time = time.time()

    return total_result, end_time - start_time

if __name__ == "__main__":
    # Parâmetros
    n_threads = 100

    print("Escolha a operação: 1 - Soma, 2 - Fibonacci (série), 3 - Integral, 4 - Fibonacci (termo único)")
    choice = int(input("Operação: "))

    if choice == 1:
        operation = "sum"
        numbers = list(range(1, 1001))  # Lista de números inteiros de 1 a 1000
        chunk_size = len(numbers) // n_threads
        data_chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    elif choice == 2:
        operation = "fibonacci"
        kk = 100  # Número de termos
        chunk_size = kk // n_threads
        data_chunks = [(i * chunk_size, chunk_size) for i in range(n_threads)]
    elif choice == 3:
        operation = "integral"
        func = lambda x: x**2  # Exemplo: função quadrática
        a, b = 0, 10
        step = (b - a) / 1000
        chunk_size = (b - a) / n_threads
        data_chunks = [(func, a + i * chunk_size, a + (i + 1) * chunk_size, step) for i in range(n_threads)]
    elif choice == 4:
        operation = "fibonacci_single"
        term = int(input("Digite o índice do termo desejado na série de Fibonacci: "))
        data_chunks = [term]  # Apenas um dado, pois é cálculo único
    else:
        raise ValueError("Escolha inválida.")

    if operation == "fibonacci_single":
        print("Executando cálculo do termo único de Fibonacci...")
        result, exec_time = execute_sequential_task(operation, data_chunks)
        print(f"Resultado: O termo F({term}) da série de Fibonacci é {result}")
    else:
        print("Executando tarefa paralela...")
        parallel_result, parallel_time = execute_parallel_task(n_threads, operation, data_chunks, simulate_latency=True)

        print("\nExecutando tarefa sequencial...")
        sequential_result, sequential_time = execute_sequential_task(operation, data_chunks)

        print("\nResultados:")
        print(f"Resultado paralelo: {parallel_result}, Tempo: {parallel_time:.4f}s")
        print(f"Resultado sequencial: {sequential_result}, Tempo: {sequential_time:.4f}s")

        # Gráficos de comparação de tempo
        plt.bar(["Paralelo", "Sequencial"], [parallel_time, sequential_time], color=["blue", "green"])
        plt.xlabel("Método")
        plt.ylabel("Tempo (s)")
        plt.title("Comparação de Tempos de Execução")
        plt.show()
