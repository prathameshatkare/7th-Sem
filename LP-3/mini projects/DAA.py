import threading
import random

MAX = 4

matA = [[random.randint(0, 9) for _ in range(MAX)] for _ in range(MAX)]
matB = [[random.randint(0, 9) for _ in range(MAX)] for _ in range(MAX)]
matC = [[0 for _ in range(MAX)] for _ in range(MAX)]

def multiply_row(row):
    for j in range(MAX):
        matC[row][j] = sum(matA[row][k] * matB[k][j] for k in range(MAX))

def display_matrix(mat, name):
    print(f"\n{name}:")
    for row in mat:
        print("\t".join(str(x) for x in row))

def main():
    print("===== MATRIX MULTIPLICATION USING MULTITHREADING =====")
    display_matrix(matA, "Matrix A")
    display_matrix(matB, "Matrix B")
    threads = []
    for i in range(MAX):
        t = threading.Thread(target=multiply_row, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    display_matrix(matC, "Resultant Matrix (A x B)")
    print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")

if __name__ == "__main__":
    main()
