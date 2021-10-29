def greet():
    print('---------------')
    print('      Игра     ')
    print('крестики-нолики')
    print('---------------')
    print('   ввод: x у   ')
    print('   x - строка  ')
    print('   у - солбец  ')
    print(' ')

def show():
    print('  0 1 2')
    for i, j in enumerate(field):
        str = ' '.join(j)
        print(f'{i} {str}')

def ask():
    while True:
        hod=input('     Ваш ход: ').split()

        if len(hod)!=2:
            print('Введите 2 координаты')
            continue
        x,y = hod

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа')
            continue
        x, y = int(x), int(y)

        if not(0<=x<=2) or not(0<=y<=2):
            print('Координаты вне поля')
            continue

        if field[x][y] != ' ':
            print('Клетка занята')
            continue

        return x, y

def chek():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for i in range(3):
        symb = []
        for j in range(3):
            symb.append(field[i][j])
        if symb == ['X', 'X', 'X']:
            print("Выиграл X")
            return True
        if symb == ["O", "O", "O"]:
            print("Выиграл O")
            return True

    for i in range(3):
        symb = []
        for j in range(3):
            symb.append(field[j][i])
        if symb == ['X', 'X', 'X']:
            print("Выиграл X")
            return True
        if symb == ["O", "O", "O"]:
            print("Выиграл O")
            return True

    symb = []
    for i in range(3):
        symb.append(field[i][i])
    if symb == ['X', 'X', 'X']:
        print("Выиграл X")
        return True
    if symb == ["O", "O", "O"]:
        print("Выиграл O")
        return True

    symb = []
    for i in range(3):
        symb.append(field[i][2-i])
    if symb == ['X', 'X', 'X']:
        print("Выиграл X")
        return True
    if symb == ["O", "O", "O"]:
        print("Выиграл O")
        return True

    return False

num=0
field = [[' ']*3for i in range(3)]
greet()
while True:
    num += 1
    show()
    if num%2 == 1:
        print('-------')
        print('Ходит X')
    else:
        print('-------')
        print('Ходит О')

    x, y = ask()

    if num%2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if chek():
        break

    if num==9:
        print('Ничья')
        break