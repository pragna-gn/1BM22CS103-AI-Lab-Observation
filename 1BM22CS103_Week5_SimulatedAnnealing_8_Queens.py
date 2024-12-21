import random
import math

def calculate_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def simulated_annealing(board, max_steps=1000, initial_temp=100, cooling_rate=0.99):
    current_conflicts = calculate_conflicts(board)
    temperature = initial_temp
    n = len(board)

    for step in range(max_steps):
        if current_conflicts == 0:
            return board

        col = random.randint(0, n - 1)
        new_row = random.randint(0, n - 1)

        new_board = board[:]
        new_board[col] = new_row
        new_conflicts = calculate_conflicts(new_board)

        delta = new_conflicts - current_conflicts
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperature):
            board = new_board
            current_conflicts = new_conflicts

        temperature *= cooling_rate

    return None

def main():
    n = int(input("Enter the number of queens (default is 8): ") or 8)
    print(f"Enter the positions of the queens as an array of size {n}:")
    print(f"(Example: 0,4,7,5,2,6,1,3 or space-separated values)")
    input_str = input().strip()

    if ',' in input_str:
        board = list(map(int, input_str.split(',')))
    else:
        board = list(map(int, input_str.split()))

    if len(board) != n:
        print("Error: The number of positions must match the number of queens.")
        return

    solution = simulated_annealing(board)

    if solution:
        print("\nSolution found:")
        for row in range(n):
            line = ['.'] * n
            line[solution[row]] = 'Q'
            print(" ".join(line))
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
