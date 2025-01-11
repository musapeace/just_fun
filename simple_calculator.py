# testing some understanding of match case 
number_1 = input("Enter the first number:")
number_2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
match number_1, number_2:
    case "+":
        print(int(number_1 + number_2))
    case "-":
        print(int(number_1 - number_2))
    case "*":
        print(int(number_1 * number_2))
    case "/":
        print(int(number_1 / number_2))           
