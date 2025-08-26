def get_positive_num(prompt: str) -> int:
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if num <= 0:
                print("Нужно ввести число больше нуля...")
                continue
            return num
        except ValueError:
            print("Пожалуйста, введите целое число.")


def get_student_names_and_scores(qty_students):
    students = {}
    for i in range(1, qty_students + 1):
        student_name = input(f"{i}-й студент: ")
        score = get_positive_num("Балл: ")
        students[student_name] = score
    return students


def calculate_average(students_dict):
    return sum(students_dict.values()) / len(students_dict)


def find_greater_than_average(students_dict, average):
    return {name: score for name, score in students_dict.items() if score > average}


def print_students_score(students_dict):
    for name, score in students_dict.items():
        print(name, '->', score)


def start_program():
    qty_students = get_positive_num("Введите количество студентов: ")
    students = get_student_names_and_scores(qty_students)
    average = round(calculate_average(students))
    result = find_greater_than_average(students, average)
    print(f"Средний балл: {average}. Студенты с баллом выше среднего:")
    print_students_score(result)


if __name__ == "__main__":
    start_program()