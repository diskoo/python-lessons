import random

v = ['камень', 'ножницы', 'бумага']

user_count = computer_count = 0

game = True

while game:

    user = input("Введите: 'камень', 'ножницы', 'бумага'\n")

    if user in v:
        computer = random.choice(v)
        
        print(user, computer)

        if user == computer:
            print('Ничья:/')
        elif user == v[0] and computer == v[1]:
            print('Победа!')
            user_count += 1
        elif user == v[0] and computer == v[2]:
            print('Лошарик!')
            computer_count += 1
        elif user == v[1] and computer == v[2]:
            print('Победа!')
            user_count += 1
        elif user == v[1] and computer == v[0]:
            print('Лошарик!')
            computer_count += 1
        elif user == v[2] and computer == v[0]:
            print('Победа!')
            user_count += 1
        elif user == v[2] and computer == v[1]:
            print('Лошарик!')
            computer_count += 1

        print(f'Игрок {user_count} : Машина {computer_count}')

        print('=' * 40)

        if user_count > computer_count + 1 or computer_count > user_count + 1:
            print('Игра закончена, ЛОШАРИК!')
            # break
            game = False

    else:
        print('Ты сломал меня полностью!')