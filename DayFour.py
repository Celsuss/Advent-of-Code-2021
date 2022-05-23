import numpy as np

def getData(path):
    def getNextMoves(lines, index):
        moves = []
        line = lines[index]
        while line != '\n':
            line = line.split('\n')[0]
            moves.extend(line.split(','))
            index += 1
            line = lines[index]
        return moves, index

    def getNextBoard(lines, index):
        board = []
        line = lines[index]
        while line != '\n':
            line = line.split('\n')[0].split(' ')
            while '' in line:
                line.remove('')
            board.append(line)
            index += 1
            if index >= len(lines):
                break
            line = lines[index]
        return board, index

    moves = []
    boards = []
    with open(path, 'r') as f:
        lines = f.readlines()
        i = 0

        moves, i = getNextMoves(lines, i)
        i += 1
        
        while i < len(lines):
            board, i = getNextBoard(lines, i)
            boards.append(board)
            i += 1
    
    return moves, boards

def processMove(move, boards_dict, boards_score):
    for board_dict, board_score in zip(boards_dict, boards_score):
        if move in board_dict:
            position = board_dict[move]
            board_score[position[0]-1, position[1]-1] += 1

    return

def getHorizontalScore():
    return

def getVerticalScore():
    return

def detectBingo(boards_dict, boards_score):
    for index, (board_dict, board_score) in enumerate(zip(boards_dict, boards_score)):
        for row in board_score:
            if np.sum(row) == board_score.shape[0]:
                # Bingo in a row detected
                print('Bingo!')
                return board_dict, board_score, index

        for i in range(board_score.shape[1]):
            if np.sum(board_score[:,i]) == board_score.shape[1]:
                print('Bingo!')
                return board_dict, board_score, index

        continue

    return None, None, None

def getSumOfUnmarkedNumbers(winning_board_dict, winning_board_score):
    sum = 0
    for key in winning_board_dict:
        position = winning_board_dict[key]
        if winning_board_score[position[0]-1, position[1]-1] == 0:
            sum += int(key)

    return sum

def generateBoardScore(boards):
    board_score = np.zeros((len(boards), len(boards[0]), len(boards[0][0])))
    return board_score

def createBoardDict(board):
    board_dict = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_dict[board[i][j]] = (i, j)

    return board_dict

def createBoardsDicts(boards):
    boards_dicts = []
    for board in boards:
        boards_dicts.append(createBoardDict(board))

    return boards_dicts

def playBingo(moves, boards, n_winning_boards=1):
    boards_score = generateBoardScore(boards)
    boards_dict = createBoardsDicts(boards)
    n_current_winning_boards = 0
    
    for move in moves:
        processMove(move, boards_dict, boards_score)
        winning_board_dict, winning_board_score, index = detectBingo(boards_dict, boards_score)
        if winning_board_dict is None:
            continue

        n_current_winning_boards += 1
        if n_current_winning_boards >= n_winning_boards:
            return winning_board_dict, winning_board_score, int(move)

        del boards_dict[index]
        np.delete(boards_score, index, 0)
        winning_board_dict = None
        winning_board_score = None

        continue

    return None, None, None

def main():
    # Part one test
    moves, boards = getData('data/4-test.txt')
    winning_board_dict, winning_board_score, winning_move = playBingo(moves, boards)
    sum = getSumOfUnmarkedNumbers(winning_board_dict, winning_board_score)
    assert sum == 188
    assert winning_move == 24
    final_product = sum * winning_move
    assert final_product == 4512

    # Part one
    moves, boards = getData('data/4.txt')
    winning_board_dict, winning_board_score, winning_move = playBingo(moves, boards)
    sum = getSumOfUnmarkedNumbers(winning_board_dict, winning_board_score)
    final_product = sum * winning_move
    print('Part one:', final_product)

    # Part two test
    moves, boards = getData('data/4-test.txt')
    winning_board_dict, winning_board_score, winning_move = playBingo(moves, boards, n_winning_boards=len(boards))
    sum = getSumOfUnmarkedNumbers(winning_board_dict, winning_board_score)
    assert sum == 148
    assert winning_move == 13
    final_product = sum * winning_move
    assert final_product == 1924

    return

if __name__ == '__main__':
    main()
