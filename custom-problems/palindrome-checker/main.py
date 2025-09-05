def find_palindromes(words):
    """
    Возвращает список палиндромов из переданного списка слов.
    
    Палиндром — слово, которое читается одинаково в обоих направлениях.
    
    :param words: список строк
    :return: список палиндромов
    """
    return list(filter(lambda element: element == element[::-1], words))


if __name__ == "__main__":
    words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
    result = find_palindromes(words)
    print("Все слова:", words)
    print("Палиндромы:", result)