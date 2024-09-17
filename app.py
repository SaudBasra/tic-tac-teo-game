from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # 'X' is the starting player
winning_cells = []
difficulty = 'medium'
game_mode = 'two-player'  # Default mode is set to two-player

def check_winner(board):
    global winning_cells
    winning_cells.clear()

    # Check rows for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winning_cells = [(i, 0), (i, 1), (i, 2)]
            return board[i][0]

    # Check columns for a win
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != '':
            winning_cells = [(0, j), (1, j), (2, j)]
            return board[0][j]

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != '':
        winning_cells = [(0, 0), (1, 1), (2, 2)]
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        winning_cells = [(0, 2), (1, 1), (2, 0)]
        return board[0][2]

    # Check for a draw
    if all(cell != '' for row in board for cell in row):
        return 'Draw'
    return None

def minimax(board, depth, alpha, beta, is_maximizing, difficulty):
    depth = adjust_depth(difficulty, depth)
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, False, difficulty)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, True, difficulty)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                move_val = minimax(board, 0, -float('inf'), float('inf'), False, difficulty)
                board[i][j] = ''
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def adjust_depth(difficulty, depth):
    if difficulty == 'easy':
        return depth + 2
    elif difficulty == 'hard':
        return depth - 2
    return depth

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/')
def index():
    winner = check_winner(board)
    return render_template('index.html', board=board, winning_cells=winning_cells, winner=winner, difficulty=difficulty, game_mode=game_mode)

@app.route('/move', methods=['POST'])
def move():
    global current_player
    try:
        row = int(request.form['row'])
        col = int(request.form['col'])

        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Invalid move")

        if board[row][col] == '' and check_winner(board) is None:
            board[row][col] = current_player
            winner = check_winner(board)

            if winner is None:
                if game_mode == 'bot' and current_player == 'X':
                    current_player = 'O'
                    ai_move = find_best_move(board)
                    if ai_move != (-1, -1):
                        board[ai_move[0]][ai_move[1]] = 'O'
                        winner = check_winner(board)
                    current_player = 'X'
                else:
                    # Switch between players in two-player mode
                    current_player = 'O' if current_player == 'X' else 'X'
    except Exception as e:
        return jsonify(error=str(e)), 400

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global board, current_player, winning_cells
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winning_cells.clear()
    return redirect(url_for('index'))

@app.route('/set-difficulty', methods=['POST'])
def set_difficulty():
    global difficulty
    difficulty = request.form['difficulty']
    return redirect(url_for('index'))

@app.route('/set-game-mode', methods=['POST'])
def set_game_mode():
    global game_mode
    game_mode = request.form['game_mode']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)