rows = 5
cols = 5

board = [['?' for x in range(cols)] for y in range(rows)]

print('\n'.join(' '.join(map(str, row)) for row in board))