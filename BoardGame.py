from flask import Flask, render_template, jsonify
app = Flask(__name__)

# Game state
board = ['' for _ in range(9)]  # 3x3 Tic-Tac-Toe board
current_player = 'X'

# Helper functions
def check_winner():
    # List of win conditions (indexes of the board)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return board[condition[0]]
    return None

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<int:index>/<player>', methods=['GET'])
def move(index, player):
    global current_player
    if board[index] == '':
        board[index] = player
        winner = check_winner()
        current_player = 'O' if player == 'X' else 'X'
        return jsonify({'status': 'valid', 'winner': winner})
    return jsonify({'status': 'invalid', 'winner': None})

@app.route('/reset')
def reset():
    global board
    board = ['' for _ in range(9)]
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
