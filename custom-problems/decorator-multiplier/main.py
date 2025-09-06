def multiply(a):
    """
    Декоратор, который умножает результат функции на заданное число.

    :param a: Число, на которое будет умножен результат функции.
    :type a: int or float
    :return: Декоратор, оборачивающий целевую функцию.
    :rtype: function

    Пример:
        @multiply(3)
        def return_num(num):
            return num

        return_num(5)  # Выведет: "Результат: 15", вернёт 15
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            multiplied = a * result
            print(f"Результат: {multiplied}")
            return multiplied
        return wrapper
    return decorator