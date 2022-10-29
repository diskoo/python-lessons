#Дебильный калькулятор
a = float(input('Введите первое число: '))
operation = input('Что сделать? (+, -): ')
b = float(input('Введите второе число: '))
result = 0

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
else:
    print('Что то пошло не так')
        #break не робiт

print(f'Результат: {result}')