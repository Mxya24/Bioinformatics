import sys

input = sys.argv[1:]

try:
    zahl = int(input[0])
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)

if zahl == 1:
    print("1 is not a prime number.")
    sys.exit(1)

zahl2= int(zahl/2)
primzahl = True

for x in range(2, zahl2):
  if(zahl%x==0):
    primzahl= False
    print( zahl,' ist keine Primzahl. Sie ist durch mindestens ', x ,'teilbar.')
    break
  
if (primzahl==True):
    print( zahl,' ist eine Primzahl. Sie ist nur durch 1 und sich selbst teilbar.')



