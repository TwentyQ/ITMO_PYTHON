import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
import random



@lru_cache()
def fact_recursive_cache(n):
    return n * fact_recursive_cache(n-1) if n else 1


def fact_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)

def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n, repeat=100):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=100, repeat=repeat)
    return min(times)



def main():
    # фиксированный набор данных
    random.seed(42)
    test_data = list(range(10, 30, 2))

    res_recursive_cache = []
    res_recursive = []
    res_iterative = []

    for n in test_data:
      fact_recursive_cache.cache_clear()
      res_iterative.append(benchmark(fact_iterative, n))
      res_recursive_cache.append(benchmark(fact_recursive_cache, n))
      res_recursive.append(benchmark(fact_recursive, n))

    # Визуализация 1 графика
    plt.subplot(1, 2, 1)
    plt.plot(test_data, res_recursive_cache, label="Рекурсивный с кэшем")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Рекурсия c мемоизацией и итеративность")
    plt.legend()

    # Визуализация 2 графика
    plt.subplot(1, 2, 2)
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Рекурсия и итеративность")
    plt.legend()

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()