import random
import sys


# check for errorsN
if len(sys.argv) < 2:
  sys.exit('few arguments passed')

# the main code to run
for arg in sys.argv[1:]:
  print('Hello', arg)

number = 10
print(f"{number:03}")