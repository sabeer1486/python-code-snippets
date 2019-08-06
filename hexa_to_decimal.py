# Takes user input as a sting
n = str(input('Enter a hexa number: '))

# declearing symbols from A-G
dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16}

# Creating a list of numbers form 1-9
num_list = [str(i) for i in range(0,10)]

# Creating a list of alphabets form a-g and coverting to uppercase
al_list = [chr(i).upper() for i in range(97, 97 + 7)]
result = 0
power = 0

# checking list in reverse order
for i in n[::-1]:
    if i in num_list:
        result = result + int(i) * 16**power
    elif i in al_list:
        result = result + dic[i] * 16**power
    power = power + 1

print(result)
    
