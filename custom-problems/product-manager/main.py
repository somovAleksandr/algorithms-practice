def get_product_number():
    """Запрашивает у пользователя номер товара.
    Возвращает целое число. Не проверяет диапазон."""
    while True:
        try:
            num = int(input("Введите номер товара: "))
            if num < 0:
                print("Номер товара не может быть отрицательным.")
                continue
            return num
        except ValueError:
            print("Ошибка! Введите число.")


def get_quantity():
    """Запрашивает у пользователя новое количество товара.
    Возвращает неотрицательное целое число."""
    while True:
        try:
            qty = int(input("Количество: "))
            if qty < 0:
                print("Количество не может быть меньше нуля.")
                continue
            return qty
        except ValueError:
            print("Ошибка! Введите количество числом.")


def print_product_list(products):
    """Выводит список товаров с нумерацией."""
    print("\nСписок товаров:")
    for i, p in enumerate(products, start=1):
        print(f"{i}) {p['name']} - {p['qty']} шт. по {p['price']} руб")


def start_program():
    """Основная логика программы."""
    products = [
        {"name": "Core-i3-4330",   "qty": 9,  "price": 4500},
        {"name": "Core i5-4670K",  "qty": 3,  "price": 8500},
        {"name": "AMD FX-6300",    "qty": 6,  "price": 3700},
        {"name": "Pentium G3220",  "qty": 8,  "price": 2100},
        {"name": "Core i5-3450",   "qty": 5,  "price": 6400},
    ]

    print_product_list(products)

    while True:
        num = get_product_number()

        if num == 0:
            print("\nРабота завершена.")
            break

        index = num - 1  # переводим номер в индекс

        if index >= len(products) or index < 0:
            print("Такого номера товара нет. Попробуйте ещё раз.")
            continue

        qty = get_quantity()
        products[index]['qty'] = qty
        print(f"Количество обновлено: {products[index]['name']} — {qty} шт.\n")

    print_product_list(products)


if __name__ == "__main__":
    start_program()