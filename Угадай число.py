import random

print('Отгадай число')

random_num = random.randint(1, 5)
user_num = input('Высри число (от 1 до 5): ')

if int(user_num) == random_num:
    print('Вы угадали!')
    print(f'Было задано число {random_num}')
else:
    print('Ты не угадал :(')
    print(f'Было задано число {random_num}')