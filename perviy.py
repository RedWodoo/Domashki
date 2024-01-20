
try:
    qwe = 2
    number = int(input('Введите число: '))
    def plus_two(a,num):
        print(f'Ответ: {a + num}')
    plus_two(qwe, number)
except ValueError:
    print("Ожидаемый тип данных— число!")