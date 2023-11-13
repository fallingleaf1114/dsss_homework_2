import random


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    """
    Random operator.
    """
    return random.choice(['+', '-', '*'])


def function_C(numb1, numb2, operator):
    """
    computations.
    """
    if operator == '+': result = numb1 + numb2
    elif operator == '-': result = numb1 - numb2
    else: result = numb1 * numb2
    problem = f"{numb1}{operator}{numb2}"
    return problem, result

def math_quiz():
    score = 0#initail score.
    total_questions = 3#can change the number, if we want to do more tests.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):#mission.
        numb1 = function_A(1, 10)
        numb2 = function_A(1, 5)
        operator = function_B()

        problem, answer = function_C(numb1, numb2, operator)
        print(f"\nQuestion: {problem}")

        while True :#Prevent errors when inputting letters and re-enter numbers.
            try:
                user_answer = float(input(f"Your answer for {problem}: "))
                break  # Break out of the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid number.")


        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
