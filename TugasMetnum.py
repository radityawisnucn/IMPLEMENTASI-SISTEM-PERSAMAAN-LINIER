#Raditya Wisnu Cahyo Nugroho_21120122130039_Metode Numerik A_Tugas Implementasi Sistem Persamaan Linier

def transpose(matrix):
   return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(matrix1, matrix2):
   return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

def matrix_inverse(matrix):
   det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - \
      matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + \
      matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
      
   invdet = 1 / det
   inverse = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
   inverse[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) * invdet
   inverse[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) * invdet
   inverse[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) * invdet
   inverse[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) * invdet
   inverse[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) * invdet
   inverse[1][2] = (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) * invdet
   inverse[2][0] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) * invdet
   inverse[2][1] = (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) * invdet
   inverse[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) * invdet
   return inverse

def lu_decomposition(matrix): 
   size = len(matrix)
   L = [[0.0] * size for _ in range(size)] 
   U = [[0.0] * size for _ in range(size)]
   
   for i in range(size):
        L[i][i] = 1.0

   for i in range(size):
        for j in range(i, size):
            total = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = matrix[i][j] - total
        for j in range(i + 1, size):
            total = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (matrix[j][i] - total) / U[i][i]

   return L, U

def solve_using_inverse(A, b): 
    A_inv = matrix_inverse(A)
    x = matrix_multiply(A_inv, [b])[0] 
    return x

def solve_using_lu(A, b):
    L, U = lu_decomposition(A) 
    y = [0.0] * len(b)
    x = [0.0] * len(b)

    for i in range(len(b)):
            y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    for i in range(len(b) - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, len(b))))/ U[i][i]

    return x

def solve_using_crout(A, b):
    L, U = lu_decomposition(A)
    y = [0.0] * len(b)
    x = [0.0] * len(b)

    for i in range(len(b)):
            y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    for i in range(len(b) - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, len(b)))) / U[i][i]

    return x

def input_matrix(size): 
    matrix = []
    for i in range(size):
            row = list(map(float, input(f"Masukkan Baris Ke-{i+1} (pisahkan dengan Spasi): ").split()))
            matrix.append(row) 
    return matrix

def input_vector(size):
    vector = list(map(float, input("Masukkan Vektor B (pisahkan dengan spasi): ").split()))
    return vector

def main():
    print("Masukkan Ukuran Matriks A:")
    n = int(input())
    print("Masukkan Isi Matriks A:")
    A = input_matrix(n) 
    print("Masukkan Isi Vektor b:")
    b = input_vector(n)

    print("\nPilih Metode yang Diinginkan:") 
    print("1. Metode Matriks Balikan")
    print("2. Metode Dekomposisi LU Gauss") 
    print("3. Metode Dekomposisi Crout") 
    choice = int(input("Pilihan: "))

    if choice == 1:
        x = solve_using_inverse(A, b)
        method = "Metode Matriks Balikan"
    elif choice == 2:
        x = solve_using_lu(A, b)
        method = "Metode Dekomposisi LU Gauss" 
    elif choice == 3:
        x = solve_using_crout(A, b)
        method = "Metode Dekomposisi Crout" 
    else:
        print("Pilihan Tidak Valid.") 
        return

    print(f"\nSolusi Menggunakan : {method}:") 
    for i in range(len(x)):
        print(f"x_{i+1} = {x[i]}")

if __name__ == "__main__":
    main()
