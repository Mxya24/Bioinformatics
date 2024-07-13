import sys

input = sys.argv[1:]

try:
    DNA = input[0]
except ValueError:
    print("Please enter a valid string.")
    sys.exit(1)

output=''
n= len(DNA)
for x in range(n - 1, -1, -1):
    output += DNA[x]

print(output)
