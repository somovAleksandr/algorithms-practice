def get_qty():
    
    while True:
        qty = input("Введите количество ворон (ЧИСЛОМ): ")
        
        try:
            qty = int(qty)
            
            if qty <= 0:
                print("Число ворон должно быть больше нуля")
                continue
            
            return qty
        except ValueError:
            print("Ошибка! Нужно ввести кол-во ворон ЧИСЛОМ.")
            

def get_word(num):
    
    if num % 10 == 1 and num != 11:
        return f"На ветке {num} ворона"
    
    if num not in [12, 13, 14] and (num % 10 == 2 or num % 10 == 3 or num % 10 == 4):
        return f"На ветке {num} вороны"
    
    if num % 10 in [5, 6, 7, 8, 9] or num >= 10 and num <= 20:
        return f"На ветке {num} ворон"
        
    
my_num = get_qty()

result = get_word(my_num)

print(result)

    

