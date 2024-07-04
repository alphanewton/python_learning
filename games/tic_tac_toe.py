matrix = [['   ','   ','   '], ['   ','   ','   '], ['   ','   ','   ']]

won = False

def printMat():
    for i in range(3):
        if i != 0:
            print('-----------')
        for j in range(3):
            if j != 0:
                print('|', end='')
            print(matrix[i][j], end='')
            if j == 2:
                print()

def isGameOver():
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != '   ' or matrix[i][0] == matrix[i][1] == matrix[i][2] != '   ':
            return True
    
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != '   ' or matrix[0][2] == matrix[1][1] == matrix[2][0] != '   ':
        return True

count = 0

#intro
print('Welcome to the Tic Tac Toe game built by Newton!')
print('''
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
''')
print('player1 = X and player2 = O. Enter slots from 1 to 9')

while count<9:
    if isGameOver():
        break
    print()
    printMat()
    if count%2 == 0:
        player = 'Player1'
        symbol = ' X '
    else:
        player = 'Player2'
        symbol = ' O '

    slot = int(input(f'{player} its ur turn. Enter an unoccupied slot from 1 to 9 -> '))
    i = (slot-1)//3
    j = (slot-1)%3
    if matrix[i][j] != '   ':
        print('Enter an empty slot!')
        continue
    matrix[i][j] = symbol
    
    count+=1

printMat()
print('GAMEOVER!')