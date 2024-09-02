import random


def new_board():
    board = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]
    for i in range(1, 9):
        board.append([])
        for j in range(0, 8):
            if j == 0:
                board[i].append(i)
            board[i].append(" ")
    return board


def generate_board(board):
    for i in board:
        for j in i:
            print(" ", j, "|", end="")
        print("\n---------------------------------------------")


def losuj_pawn(board):
    a = random.randint(1, 8)
    b = random.randint(1, 8)
    pawn = [a, b]
    board[a][b] = 'P'
    return pawn


def losuj_queen(board, ilosc):
    for i in range(0, ilosc):
        c = random.randint(1, 8)
        d = random.randint(1, 8)
        while board[c][d] != " ":
            c = random.randint(1, 8)
            d = random.randint(1, 8)
        board[c][d] = 'K'


def position(pawn, board):
    x = 0
    n = 1
    while pawn[0]-n > 0:
        if board[pawn[0]-n][pawn[1]] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]], pawn[0]-n)
            break
        n += 1
    n = 0
    while pawn[0] + n < 9:
        if board[pawn[0]+n][pawn[1]] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]], pawn[0] + n)
            break
        n += 1
    n = 0

    while pawn[1] - n > 0:
        if board[pawn[0]][pawn[1]-n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]-n], pawn[0])
            break
        n += 1
    n = 0
    while pawn[1] + n < 9:
        if board[pawn[0]][pawn[1]+n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]+n], pawn[0])
            break
        n += 1
    n = 0

    while pawn[0]-n > 0 and pawn[1]-n > 0:
        if board[pawn[0]-n][pawn[1]-n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]-n], pawn[0]-n)
            break
        n += 1
    n = 0
    while pawn[0]+n < 9 and pawn[1]+n < 9:
        if board[pawn[0]+n][pawn[1]+n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]+n], pawn[0]+n)
            break
        n += 1
    n = 0
    while pawn[0]-n > 0 and pawn[1]+n < 9:
        if board[pawn[0]-n][pawn[1]+n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]+n], pawn[0]-n)
            break
        n += 1
    n = 0
    while pawn[0]+n < 9 and pawn[1]-n > 0:
        if board[pawn[0]+n][pawn[1]-n] == 'K':
            x += 1
            print("Hetman: ", board[0][pawn[1]-n], pawn[0]+n)
            break
        n += 1
    if x != 0:
        print("Ilość hetmanów mogących zbić pionka: ", x)
    else:
        print("Żaden hetman nie może zbić pionka.")


def usun(figura, board):
    board[figura[0]][figura[1]] = " "
    return board


def main():
    board = new_board()
    pawn = losuj_pawn(board)
    losuj_queen(board, random.randint(1, 5))
    generate_board(board)
    position(pawn, board)
    wybor = ''
    while wybor != '4':
        wybor = input("\nCo chcesz zrobić? \n\n"
                              "1 - Wylosować nową pozycję dla pionka \n"
                              "2 - Usunąć dowolnego hetmana \n"
                              "3 - Ponownie sprawdź bicia \n"
                              "4 - Koniec \n\n"
                              "Wybierz cyfrę: ")

        if wybor == '1':
            usun(pawn, board)
            pawn = losuj_pawn(board)
            print("Zmieniliśmy pozycję pionka.\n")
            generate_board(board)

        if wybor == '2':
            queen = [0,0]
            liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8]

            while board[queen[0]][queen[1]] != 'K':
                queen.clear()
                lista = input("Podaj pozycję hetmana do usunięcia: ")
                lista = lista.upper()
                lista = lista.replace(' ', '')
                for i in range(len(board[0])):
                    if lista[0] == board[0][i]:
                        queen.append(int(lista[1]))
                        queen.append(liczby[i])
            usun(queen, board)
            print("Usunęliśmy wskazanego hetmana.")
            generate_board(board)


        if wybor == '3':
            generate_board(board)
            position(pawn, board)


main()
