'''
program
'''
try:
    QWE = 2
    number = int(input('Введите число: '))
    def plus_two(a,num):
        '''
        program
        '''
        print(f'Ответ: {a + num}')
    plus_two(QWE, number)
except ValueError:
    print("Ожидаемый тип данных— число!")
