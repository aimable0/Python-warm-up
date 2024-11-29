def main():
  expression = input('Expression: ')
  
  # split the expression to exract its components
  expression = expression.split(' ')
  
  # check the operator sign and solve the expression
  operator = expression[1]
  match operator:
    case "+":
      print(float(expression[0]) + float(expression[2]))
    case "-":
      print(float(expression[0]) - float(expression[2]))
    case "*":
      print(float(expression[0]) * float(expression[2]))
    case "/":
      answer = float(expression[0]) / float(expression[2])
      # below'.1f' is a format specifier for limiting decimal places to output.
      print(f"{answer:.1f}")
  
main()