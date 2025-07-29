def get_nums():
    """
    Запрашивает ввод двух значений.
    Если хотя бы одно из них не является числом, то выполняется конкатенация строк.
    В остальных случаях числа суммируются.
    """
    while True:
        first_input = input("Введите первое значение: ").strip()
        
        if not first_input:
            print("Поле не может быть пустым")
            continue
        
        try:
            first_num = int(first_input)
            
            while True:
                second_input = input("Введите второе значение: ").strip()
                
                if not second_input:
                    print("Поле не может быть пустым")
                    continue
                
                try:
                    second_num = int(second_input)
                    return first_num + second_num
                except ValueError:
                    return str(first_num) + second_input
            
        except ValueError:
            second_input = input("Введите второе значение: ").strip()
            return first_input + second_input


if __name__ == "__main__":
    result = get_nums()
    print(result)