# 📐 Rectangle Closure

Простой, но мощный пример использования **замыканий (closures)** в Python для создания объекта-подобной структуры **без использования классов**.

## 🧩 Описание

Модуль `make_rectangle(a, b)` возвращает набор функций, связанных с прямоугольником:

- `perimeter()` — вычисляет периметр: `2*(a + b)`
- `area()` — вычисляет площадь: `a * b`
- `get_status()` — показывает, сколько раз были вызваны функции
- `reset_counts()` — сбрасывает счётчики

Внутри используется `nonlocal`, чтобы управлять состоянием (счётчиками вызовов) — демонстрируя **инкапсуляцию в функциональном стиле**.

## 🚀 Использование

```python
from main import make_rectangle

p, a, status, reset = make_rectangle(3, 4)

print(p())      # → 14
print(a())      # → 12
print(status()) # → Perimeter called 1 times, area called 1 times

reset()
print(status()) # → Perimeter called 0 times, area called 0 times
```
