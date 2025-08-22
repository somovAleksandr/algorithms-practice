# Python Dictionary Utils

Простой модуль для работы с ключами словарей в Python. Позволяет безопасно переименовывать ключи.

## Функция `rename_key`

rename_key(dictionary, old_key, new_key)

Параметры:
dictionary (dict): словарь для изменения
old_key (str): старое имя ключа
new_key (str): новое имя ключа
Возвращает:
True, если ключ был переименован
False, если старый ключ не найден
Исключения:
TypeError, если dictionary не является словарём
