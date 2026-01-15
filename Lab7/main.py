from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class SudokuGenerator:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]
    
    def is_valid(self, row, col, num):
        # Check row
        if num in self.board[row]:
            return False
        
        # Check column
        if num in [self.board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True
    
    def generate(self, difficulty=40):
        # Generate complete board
        self.solve()
        
        # Remove numbers based on difficulty
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        
        for i, j in cells[:difficulty]:
            self.board[i][j] = 0
        
        return self.board

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    difficulty = int(request.json.get('difficulty', 40))
    generator = SudokuGenerator()
    board = generator.generate(difficulty)
    return jsonify({'board': board})

@app.route('/validate', methods=['POST'])
def validate():
    board = request.json.get('board')
    
    # Check if board is valid
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                generator = SudokuGenerator()
                generator.board = [row[:] for row in board]
                if not generator.is_valid(row, col, num):
                    return jsonify({'valid': False, 'message': 'Invalid board'})
                board[row][col] = num
    
    return jsonify({'valid': True, 'message': 'Board is valid!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
