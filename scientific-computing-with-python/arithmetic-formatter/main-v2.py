VALID_OPERATORS = ["+", "-"]
SPACE_BETWEEN_PROBLEMS = " " * 4

def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  problems = list(problem.split() for problem in problems)

  for left, operator, right in problems:
    if operator not in VALID_OPERATORS:
      return "Error: Operator must be '+' or '-'."

    if not left.isdigit() or not right.isdigit():
      return "Error: Numbers must only contain digits."

    if len(left) > 4 or len(right) > 4:
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
