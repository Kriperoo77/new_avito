# функции
def add(x, y):
    return x + y


def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc

new = newfunc(100)
new(200)

def func(a, b, c=2): # c - необязательный параметр
    return a + b + c


def func2(*args):
    return args

def func_with_kwargs(**kwargs):
    return kwargs

# анонимные функции lambda
func = lambda x,y: x + y
func(1,2)

try:
    number = int(input('Введите число'))
except ValueError:
    print('Вы ввели не число')

# остаток от деление %
for line in f:
    ints.append(int(line))

    print('Это не число. Выходим.')
else:
    print('Всё хорошо')
    print('Я закрыл файл')

# Мененджер контекста
with open('newfile.txt', 'w', encoding='uft-8') as g:
    d = int(input())
    print('1 / {}'. format(d, 1 / d), file=g)

#Генераторы списков