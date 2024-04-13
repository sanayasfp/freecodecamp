import string

VALID_OPERATOR = ["+", "-"]
DIGITS = string.digits
SPACE_BETWEEN_PROBLEMS = " " * 4

def isValidOperator(operators):
    return all(
        operator in VALID_OPERATOR for operator in operators
    )

def isDigits(operands):
    return all(digit in DIGITS for operand in operands for digit in operand)

def isOperandLength(operands):
    return all(len(operand) <= 4 for operand in operands)

def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    problems = list(problem.split() for problem in problems)
    operators = list(operator for _, operator, _ in problems)

    if not isValidOperator(operators):
        return "Error: Operator must be '+' or '-'."

    left_operand = list(operand for operand, _, _ in problems)
    right_operand = list(operand for _, _, operand in problems)

    if not isDigits(left_operand) or not isDigits(right_operand):
      return "Error: Numbers must only contain digits."

    if not isOperandLength(left_operand) or not isOperandLength(right_operand):
        return "Error: Numbers cannot be more than four digits."

    left_operand_display = []
    right_operand_display = []
    dash_display = []
    answer_display = []

    for left, operator, right in problems:
        most_large_operand = max(len(left), len(right))
        num_chars = most_large_operand + 2

        left_operand_display.append(f'{left:>{num_chars}}')
        right_operand_display.append(f'{operator} {right:>{most_large_operand}}')
        dash_display.append('-' * num_chars)

        if show_answers:
            if operator == "+":
                answer = int(left) + int(right)
            elif operator == "-":
                answer = int(left) - int(right)

            answer_display.append(f'{answer:>{num_chars}}')

    # Join each individual list into a string with each element separated by a newline
    left_operand_str = SPACE_BETWEEN_PROBLEMS.join(left_operand_display)
    right_operand_str = SPACE_BETWEEN_PROBLEMS.join(right_operand_display)
    dash_str = SPACE_BETWEEN_PROBLEMS.join(dash_display)
    answer_str = SPACE_BETWEEN_PROBLEMS.join(answer_display)

    # Now join these strings into the final formatted string, separating each "column" by SPACE_BETWEEN_PROBLEMS
    if show_answers:
        problems = f"{left_operand_str}\n{right_operand_str}\n{dash_str}\n{answer_str}"
    else:
        problems = f"{left_operand_str}\n{right_operand_str}\n{dash_str}"


    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
