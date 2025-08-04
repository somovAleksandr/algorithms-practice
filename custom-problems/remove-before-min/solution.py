from random import randint

numbers = [randint(10,99) for i in range(10)]
min_num = min(numbers)
index_min = numbers.index(min_num)
result = numbers[index_min:]
print(numbers)

print('Min:', min_num)
print('Index min:', index_min)
print('Список:', result)