# 101124255 Jonathan Seltzer
import random
import math

# # Part A
try:
    # Open the Score.txt file in read mode to check if it contains anything
    with open("Score.txt", "r") as f:
        contents = f.read().strip()
    # Check if the file is empty or not
    if not contents:
        print("Welcome to your Math Game!")
    else:
        # If the file is not empty, assume it contains a single integer score value
        score = int(contents)
        print(f"I am happy to meet you again! Your last score was {score}!")
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Score.txt file not found. Starting a new game...")
except ValueError:
    # Handle the case where the file contains something other than an integer score
    print("Score.txt file contains invalid data. Starting a new game...")

# Global score
maxScore = 0


def myMathTest():
    global maxScore
    # Array of operators
    random_op = ["+", "-", "*"]
    # Randomly grabs one the operators
    random_operator = random_op[random.randint(0, len(random_op) - 1)]
    var_a = random.randint(1, 10)
    var_b = random.randint(1, 10)
    # If the operator is equal +, add the variables
    if random_operator == "+":
        answer = var_a + var_b
    # If the operator is equal +, multiply the variables
    if random_operator == "*":
        answer = var_a * var_b
    # If the operator is equal -, minus the variables
    if random_operator == "-":
        answer = var_a - var_b
    user_answer = input(f"What is the result of {var_a} {random_operator} {var_b}? ")
    # Displays the try if the input is same as answer
    try:
        if int(user_answer) == answer:
            print("Congratulations! You are Pro!")
            # Adds one to the global score
            maxScore += 1
        else:
            # Displays the correct answer if the input was not the answer
            correct_answer = var_a + var_b
            print(f"The correct answer is {correct_answer}. Let's try another question :)")
            # Minus one to the global score
            maxScore -= 1
    except ValueError:
        print("Invalid input. Please enter a number.")


while True:
    myMathTest()
    play_more = input("Do you want to continue? (Y to continue, any other character to Exit) ")
    if play_more.upper() != "Y":
        break


def fileScore():
    # Display messages and the score 150 than saves it in the file
    if maxScore == 150:
        print("Thank you for playing!")
        print("You got 150!")
        print("WOW!")
        with open("Score.txt", "w") as file:
            file.write(str(maxScore))
    # Display messages and the score than saves it in the file
    else:
        print("Thank you for playing!")
        print(f"You got {maxScore}!")
        print("WOW!")
        with open("Score.txt", "w") as file:
            file.write(str(maxScore))


# Part b

def discriminant():
    print("Welcome to Quadratic Equation Game!")
    print("aX^2 + bX + C = 0")
    while True:
        # Try except loop until user puts 3 numbers
        try:
            a = float(input("Please enter the value for a: "))
            b = float(input("Please enter the value for b: "))
            c = float(input("Please enter the value for c: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Displays the inputted numbers in the quadratic equation
    quadEquation = f"Your Quadratic Equation is: {a}X^2 + {b}X + {c} = 0"
    print(quadEquation)
    equation = b ** 2 - 4 * a * c
    # If else statement depending on the discriminant and displaying how many solutions there are
    if equation > 0:
        x1 = (-b + math.sqrt(equation)) / (2 * a)
        x2 = (-b - math.sqrt(equation)) / (2 * a)
        message = "We got two real solutions, which are {} and {}".format(x1, x2)
        print(message)
    elif equation == 0:
        x1 = (-b + math.sqrt(equation)) / (2 * a)
        message = "We got one solution, which is {}".format(x1)
        print(message)
    else:
        message = "The Discriminant is negative, we got a pair of Complex solutions."
        print(message)
    # Writes the equation of the inputted numbers and the solution of the equation.
    with open("QuadEqu.txt", "w") as file:
        file.write(str(quadEquation) + "\n" + str(message))


discriminant()
