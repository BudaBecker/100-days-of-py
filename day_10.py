#Easy python calculator

art = '''
 _____________________
|  _________________  |
| | Easy Python     | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(art)

def calculate(first_num: float, operator: str, second_num: float) -> float:
    match operator:
        case '+':
            return first_num+second_num
        case '-':
            return first_num-second_num
        case '*':
            return first_num*second_num
        case '/':
            return first_num/second_num

end = False
first_numb = float(input("What's the first number?: "))
while not end:
    print("+\n-\n*\n\\")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = calculate(first_numb, operation, second_number)
    print(f"{first_numb} {operation} {second_number} = {result}")
    if input(f"Type 'y' to continue calculating with {result}, or 'n' to leave: ").lower() == 'n':
        end = True
        print("Bye.")
    else:
        first_numb = result