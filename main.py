def arithmetic_arranger(problems, solve=False):
    arranged_problems = []
    print('')

    for problem in problems:
        switch = False
        num1 = ""
        num2 = ""
        operator = ""
        result = 0

        for c in problem:
            if switch:
                num2 += c
            if c == '+' or c == '-':
                operator = c
                switch = True
            if not switch:
                num1 += c

        if len(num1) >= len(num2):
            spacing = len(operator) + 1 + len(num1)
        else:
            spacing = len(operator) + 1 + len(num2)

        if solve:
            if operator == '+':
                result = int(num1) + int(num2)
            elif operator == '-':
                result = int(num1) - int(num2)
            problem_str = f"{num1:>{spacing}}\n{operator} {num2:>{spacing - 2}}\n{'-' * spacing}\n{result:>{spacing}}\n"

        else:
            problem_str = f"{num1:>{spacing}}\n{operator} {num2:>{spacing - 2}}\n{'-' * spacing}\n"
        arranged_problems.append(problem_str)
        # print(problem_str)

    for solution in arranged_problems:
        print(solution)

    return arranged_problems


if __name__ == "__main__":
    problem_list = []

    num_of_problems = 0
    while True:
        num_of_problems = int(input("Enter number of problems: "))

        if num_of_problems > 5:
            print("Error: Too many problems\n")
        else:
            print('\n')
            break

    # check for certain conditions
    index = 0
    while True:
        if index <= len(problem_list):
            index = len(problem_list)

        if index == num_of_problems:
            break
        problem = input("Enter an arithmetic problem: ")

        # remove all spaces for condition checks
        temp = problem.replace(" ", "")
        updated_problem = temp

        # check if multiplication/division operator is in problem
        if '*' in temp or '/' in temp:
            print("Error: Operator must be '+' or '-'\n")
            index -= 1
            continue

        # count how many times a  +/- appears (should be only once)
        count = 0
        for c in temp:
            if c == '+' or c == '-':
                count += 1
        if count == 1:
            num1 = ""
            num2 = ""
            switch = False

            for c in temp:
                if switch:
                    num2 += c
                if c == '+' or c == '-':
                    switch = True
                if not switch:
                    num1 += c

            if len(num1) > 4 or len(num2) > 4:
                print("Error: Numbers cannot be more than four digits.\n")
                index -= 1
                continue

            if '+' in temp:
                temp = temp.replace("+", "")
            elif '-' in temp:
                temp = temp.replace("-", "")
        else:
            print("Error: Too many operators.\n")
            index -= 1
            continue

        try:
            temp = int(temp)
            problem_list.append(updated_problem)
            # print(problem_list[index], '\n')
            index += 1
        except ValueError:
            print("Error: Numbers must only contain digits\n")
            index -= 1

    arithmetic_arranger(problem_list, True)
