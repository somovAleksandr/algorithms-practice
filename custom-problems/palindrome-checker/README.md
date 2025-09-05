# Palindrome Checker

Простая утилита на Python, которая находит палиндромы в списке слов.

## Описание

Палиндром — слово, фраза или последовательность, которая читается одинаково в обоих направлениях (например, `madam`, `mom`).

Этот скрипт использует `filter()` и `lambda`, чтобы найти все палиндромы в заданном списке.

## Использование

```python
from main import find_palindromes

words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
result = find_palindromes(words)
print(result)  # ['madam', 'mom']
```
