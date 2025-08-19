def get_num_of_product(iterable_obj):
    while True:
        num_of_product = input("Введите номер товара: ")
        
        try:
            num_of_product = int(num_of_product)
            
            if num_of_product == 0:
                return False  # завершить
            
            index = num_of_product - 1  # перевод в индекс
            
            if index < 0 or index >= len(iterable_obj):
                print("Такого номера товара НЕТ.")
                continue
            
            return index
            
        except ValueError:
            print("Ошибка ввода! Нужно ввести номер товара ЧИСЛОМ")

def change_qty_product(lst, index):
    while True:
        qty_product = input("Введите кол-во продукта: ")
        
        try:
            qty_product = int(qty_product)
            
            if qty_product < 0:
                print("Кол-во продукта не может быть меньше нуля.")
                continue
            
            break
        except ValueError:
            print("Ошибка! Нужно ввести КОЛ-ВО ЧИСЛОМ.")
    
    lst[index][1] = qty_product

def print_lst(lst):
    for i in range(len(lst)):
        name, qty, price = lst[i]
        print(f"{i + 1}) {name} - {qty} шт. по {price}руб")

def start_program():
    products = [
        ["Core-i3-4330", 9, 4500],
        ["Core i5-4670K", 3, 8500],
        ["AMD FX-6300", 6, 3700],
        ["Pentium G3220", 8, 2100],
        ["Core i5-3450", 5, 6400]
    ]

    print_lst(products)

    while True:
        index = get_num_of_product(products)
        if index is False:
            break
        change_qty_product(products, index)

    print("\nОбновлённый список:")
    print_lst(products)

start_program()