from time import perf_counter


def uppercase(func):
    """
    Декоратор, преобразующий возвращаемую строку функции в верхний регистр.
    
    Пример:
        @uppercase
        def say_hello():
            return "привет"
        
        print(say_hello())  # ПРИВЕТ
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper


def repeat(n):
    """
    Декоратор, вызывающий функцию n раз.
    
    Аргументы:
        n (int): количество вызовов
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


def qty_symbols(n):
    """
    Декоратор, обрамляющий вызов функции строкой из n символов '*'.
    
    Полезно для визуального выделения.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('*' * n)
            func(*args, **kwargs)
            print('*' * n)
        return wrapper
    return decorator


def timer(func):
    """
    Декоратор, измеряющий время выполнения функции.
    
    Выводит имя функции и длительность выполнения в секундах.
    """
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} выполнилась за {elapsed:.6f} секунд")
        return result
    return wrapper


def log_calls(func):
    """
    Декоратор, логирующий каждый вызов функции: имя и аргументы.
    
    Пример:
        @log_calls
        def greet(name, age=None):
            print(f"Привет, {name}!")
        
        greet("Анна", age=25)
        # Вывод: Вызов: greet('Анна', age=25)
    """
    def wrapper(*args, **kwargs):
        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(f"{k}={repr(v)}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"Вызов: {func.__name__}({all_args})")

        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f"Время выполнения: {elapsed:.6f} сек")

        return result
    return wrapper