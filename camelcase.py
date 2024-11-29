def main():
  camel_case_name = input('Enter a name: ')
  snake_case_name = convert_to_snake_case(camel_case_name)
  print(snake_case_name)

def convert_to_snake_case(name):
  snake_case_name = ''

  for letter in name:
    if letter.isupper(): 
      # add underscore before the capital letter in the name.  
      snake_case_name += '_'
    snake_case_name += letter.lower()
  return snake_case_name

if __name__ == "__main__":
  main()


