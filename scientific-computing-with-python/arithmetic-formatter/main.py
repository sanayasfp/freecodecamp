VALID_OPERATORS = ["+", "-"]
SPACE_BETWEEN_PROBLEMS = " " * 4

def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  problems = list(problem.split() for problem in problems)

  left_operand_str = ""
  right_operand_str = ""
  dash_str = ""
  answer_str = ""

  for index, (left, operator, right) in enumerate(problems):
    if index > 0:
      left_operand_str += SPACE_BETWEEN_PROBLEMS
      right_operand_str += SPACE_BETWEEN_PROBLEMS
      dash_str += SPACE_BETWEEN_PROBLEMS
      answer_str += SPACE_BETWEEN_PROBLEMS

    if operator not in VALID_OPERATORS:
      return "Error: Operator must be '+' or '-'."

    if not left.isdigit() or not right.isdigit():
      return "Error: Numbers must only contain digits."

    if len(left) > 4 or len(right) > 4:
      return "Error: Numbers cannot be more than four digits."

    most_large_operand = max(len(left), len(right))
    num_chars = most_large_operand + 2

    left_operand_str += f'{left:>{num_chars}}'
    right_operand_str += f'{operator} {right:>{most_large_operand}}'
    dash_str += '-' * num_chars

    if show_answers:
      if operator == "+":
        answer = int(left) + int(right)
      elif operator == "-":
        answer = int(left) - int(right)

      answer_str += f'{answer:>{num_chars}}'

  problems = f"{left_operand_str}\n{right_operand_str}\n{dash_str}{f'\n{answer_str}' if show_answers else ''}"
    
  return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
