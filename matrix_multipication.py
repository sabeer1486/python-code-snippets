from numpy import zeros

#  prompting user for row and col values
print("\n*****first matrix column no. and second matrix row no. need to be same*****\n")
first_row_no = int(input("enter no.of rows for first matrix: "))
first_col_no = int(input("enter no. cols for first matrix: "))
second_row_no = int(input("enter no. rows for first matrix: "))
second_col_no = int(input("enter no. cols for first matrix: "))

# Initialising arrays
array1 = zeros((first_row_no, first_col_no), int)
array2 = zeros((second_row_no, second_col_no), int)
array3 = zeros((first_row_no, second_col_no), int)

# Filling first matrix with user values
if first_col_no == second_row_no:
    print(f"enter {first_row_no * first_col_no} values into first matrix: ")
    for i in range(first_row_no):
        for j in range(first_col_no):
            array1[i][j] = int(input())

    # Filling second matrix with user values
    print(f"enter {second_row_no * second_col_no} values into first matrix: ")
    for i in range(second_row_no):
        for j in range(second_col_no):
            array2[i][j] = int(input())

    #  Multiplication logic
    for i in range(first_row_no):
        for j in range(second_col_no):
            for k in range(first_col_no):
                array3[i][j] = array3[i][j] + array1[i][k] * array2[k][j]
    # printing resultant matrix
    print("\nHere is your resultant matrix:\n")
    for i in range(first_row_no):
        for j in range(second_col_no):
            print(array3[i][j], end=' ')
        print()
    print("Bingo ^_^ !")
else:
    print("matrix multiplication not possible *_* !")