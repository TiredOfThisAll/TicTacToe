x_wins = False
o_wins = False
Impossible = False
Draw = False
GameNotFinished = True

print("""
Current positions in the game
[1][3] [2][3] [3][3]
[1][2] [2][2] [3][2]
[1][1] [2][1] [3][1]
""")

xcount = 0
ocount = 0

str1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_cells():
    print("---------")
    print('|', str1[0], str1[1], str1[2], '|')
    print('|', str1[3], str1[4], str1[5], '|')
    print('|', str1[6], str1[7], str1[8], '|')
    print("---------")


def check_the_status():
    global x_wins
    global o_wins
    global GameNotFinished
    global Impossible
    global Draw
    if str1[0] == 'X' and str1[1] == 'X' and str1[2] == 'X' or str1[3] == 'X' and str1[4] == 'X' and str1[5] == 'X' \
            or str1[6] == 'X' and str1[7] == 'X' and str1[8] == 'X' or str1[0] == 'X' and str1[4] == 'X' \
            and str1[8] == 'X' or str1[2] == 'X' and str1[4] == 'X' and str1[6] == 'X' or str1[0] == 'X' \
            and str1[3] == 'X' and str1[6] == 'X' or str1[1] == 'X' and str1[4] == 'X' and str1[7] == 'X' \
            or str1[2] == 'X' and str1[5] == 'X' and str1[8] == 'X':
        x_wins = True
    if str1[0] == 'O' and str1[1] == 'O' and str1[2] == 'O' or str1[3] == 'O' and str1[4] == 'O' and str1[5] == 'O' \
            or str1[6] == 'O' and str1[7] == 'O' and str1[8] == 'O' or str1[0] == 'O' and str1[4] == 'O' and \
            str1[8] == 'O' or str1[2] == 'O' and str1[4] == 'O' and str1[6] == 'O' or str1[0] == 'O' and str1[3] == 'O' \
            and str1[6] == 'O' or str1[1] == 'O' and str1[4] == 'O' and str1[7] == 'O' or str1[2] == 'O' \
            and str1[5] == 'O' and str1[8] == 'O':
        o_wins = True
    if not x_wins and not o_wins and ("_" in str1 or " " in str1):
        GameNotFinished = True

    if (x_wins and o_wins) or ocount >= xcount + 2 or xcount >= ocount + 2:
        Impossible = True

    if not x_wins and not o_wins and "_" not in str1 and " " not in str1:
        Draw = True

    if Impossible:
        print("Impossible")
        Draw = False
        x_wins = False
        o_wins = False
        GameNotFinished = False
    if o_wins:
        GameNotFinished = False
        print("O wins")
    if x_wins:
        GameNotFinished = False
        print("X wins")
    if Draw:
        GameNotFinished = False
        print("Draw")
    if GameNotFinished:
        print("Game not finished")


def x_goes():
    while GameNotFinished:
        pos1, pos2 = input("Enter pos: ").split(' ')
        if pos1 == '1' and pos2 == '1':
            if str1[6] != 'X' and str1[6] != 'O':
                str1[6] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '1' and pos2 == '2':
            if str1[3] != 'X' and str1[3] != 'O':
                str1[3] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '1' and pos2 == '3':
            if str1[0] != 'X' and str1[0] != 'O':
                str1[0] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '1':
            if str1[7] != 'X' and str1[7] != 'O':
                str1[7] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '2':
            if str1[4] != 'X' and str1[4] != 'O':
                str1[4] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '3':
            if str1[1] != 'X' and str1[1] != 'O':
                str1[1] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '1':
            if str1[8] != 'X' and str1[8] != 'O':
                str1[8] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '2':
            if str1[5] != 'X' and str1[5] != 'O':
                str1[5] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '3':
            if str1[2] != 'X' and str1[2] != 'O':
                str1[2] = 'X'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        else:
            print("Type numbers from 1 to 3!")


def o_goes():
    while GameNotFinished:
        pos1, pos2 = input("Enter pos: ").split(' ')
        if pos1 == '1' and pos2 == '1':
            if str1[6] != 'X' and str1[6] != 'O':
                str1[6] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '1' and pos2 == '2':
            if str1[3] != 'X' and str1[3] != 'O':
                str1[3] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '1' and pos2 == '3':
            if str1[0] != 'X' and str1[0] != 'O':
                str1[0] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '1':
            if str1[7] != 'X' and str1[7] != 'O':
                str1[7] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '2':
            if str1[4] != 'X' and str1[4] != 'O':
                str1[4] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '2' and pos2 == '3':
            if str1[1] != 'X' and str1[1] != 'O':
                str1[1] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '1':
            if str1[8] != 'X' and str1[8] != 'O':
                str1[8] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '2':
            if str1[5] != 'X' and str1[5] != 'O':
                str1[5] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        elif pos1 == '3' and pos2 == '3':
            if str1[2] != 'X' and str1[2] != 'O':
                str1[2] = 'O'
                print_cells()
                check_the_status()
                break
            else:
                print("This cell is occupated!")
                continue
        else:
            print("Type numbers from 1 to 3!")


print("Fight!")


while GameNotFinished:
    x_goes()
    o_goes()