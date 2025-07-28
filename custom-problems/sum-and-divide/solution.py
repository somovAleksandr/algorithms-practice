my_nums = [int(input(f"Введите {i + 1}-е число: ")) for i in range(4)]

sum_one = 0
sum_two = 0

for i in range(len(my_nums)):
    if i < 2:
        sum_one += my_nums[i]
    else:
        sum_two += my_nums[i]

print("Результат:", round(sum_one / sum_two, 2))